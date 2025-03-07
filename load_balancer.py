# Updating the load balancer to rotate requests across multiple backends

import socket
import threading
import itertools
import requests
import time


# List of backend servers
BACKENDS = [("127.0.0.1", 8080), ("127.0.0.1", 8081)]
healthy_backends = BACKENDS.copy()
  # Round-robin iterator
backend_iter = itertools.cycle(BACKENDS)
# Checking every 5 seconds
HEALTH_CHECK_INTERVAL = 5

def handle_client(client_socket):
    "Handles client requests and forwards them to a backend server."
    try:
        request = client_socket.recv(1024)
        print(f"Received request:\n{request.decode()}\n")

        # Select backend server using round robin
        backend_host, backend_port = next(backend_iter)
        print(f"Forwarding request to backend {backend_host}:{backend_port}")

        # Connect to backend server
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect((backend_host, backend_port))
        backend_socket.sendall(request)

        # Read response in a loop (fixes partial response issue)
        response = b""
        while True:
            part = backend_socket.recv(4096)
            if not part:  # If no more data, break loop
                break
            response += part

        backend_socket.close()

        # Send the full response to the client
        client_socket.sendall(response)
        client_socket.close()
        print("Response sent back to client.\n")

    except Exception as e:
        print(f"Error handling request: {e}")

def start_load_balancer():
    """Starts the load balancer."""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5001))
    server.listen(5)
    print("Load Balancer listening on port 5001...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection received from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_load_balancer()
    


# Adding health check, unhealthy servers from rotations
def health_check():
    "Periodically checks health of backend servers."
    global healthy_backends, backend_iter

    while True:
        new_healthy_backends = []
        for backend in BACKENDS:
            try:
                res = requests.get(f"http://{backend[0]}:{backend[1]}", timeout=2)
                if res.status_code == 200:
                    new_healthy_backends.append(backend)
            except:
                print(f"Server {backend} is DOWN")

        healthy_backends = new_healthy_backends
        backend_iter = itertools.cycle(healthy_backends)  # Update iterator
        print(f"Updated healthy backends: {healthy_backends}")
        time.sleep(HEALTH_CHECK_INTERVAL)

def start_health_check():
    "Runs health checks in a separate thread."
    health_thread = threading.Thread(target=health_check, daemon=True)
    health_thread.start()

if __name__ == "__main__":
    start_health_check()
    start_load_balancer()