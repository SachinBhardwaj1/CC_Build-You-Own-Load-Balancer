# CC_Build-You-Own-Load-Balancer by John Crickett

# 🔀 Build Your Own HTTP Load Balancer with Health Checks

Welcome to a hands-on systems project that walks through how to **build a custom Layer 7 Load Balancer** using **Python** and **Flask**, capable of distributing HTTP requests across multiple backend servers with **health checks** and **concurrent client handling**.

---

## 📌 Overview

This project simulates a real-world application-layer load balancer — similar to what AWS ALB or Nginx does — but written from scratch using low-level socket programming. It's designed to:

- Distribute traffic using **Round Robin Scheduling**
- Ensure **high availability** via automated **health checks**
- Handle **server failures and recoveries**
- Manage **concurrent client connections**

---

## 🔧 Technologies Used

| Feature             | Tech/Method                  |
|---------------------|------------------------------|
| Language            | Python 3                     |
| Web Framework       | Flask                        |
| Networking          | `socket`, `requests`         |
| Concurrency         | `threading`, `multiprocessing` |
| Testing Tool        | `curl`, `urls.txt`           |

---

## 📁 Project Structure

```
.
├── Backend.py         # Launches Flask servers on multiple ports
├── LoadBalancer.py    # Load Balancer with request routing + health checks
├── urls.txt           # File with repeated URLs for load testing
├── README.md          # Project documentation
```

---

## 🧠 What I Learned

- Implemented **Round Robin Load Balancing**
- Built a **Layer 7 HTTP Router** using raw sockets
- Designed a **multi-threaded client handler** system
- Used **multiprocessing** to simulate scalable backend servers
- Implemented **real-time health checks** for fault tolerance
- Understood backend recovery using **dynamic server pools**

---

## 🚀 Features

✅ Distributes traffic across multiple backend servers  
✅ Health checks every 5 seconds (configurable)  
✅ Excludes dead backends from rotation  
✅ Re-adds backends when they recover  
✅ Supports multiple concurrent clients  
✅ Easy to extend with new features  

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/CC_Build-You-Own-Load-Balancer.git
cd CC_Build-You-Own-Load-Balancer
```

### 2. Start Backend Servers

```bash
python3 backend.py
```

This will launch two backend Flask servers on ports `8080` and `8081`.

### 3. Start the Load Balancer

```bash
python3 load_balancer.py
```

The load balancer will start listening on port `5001` and begin health checking backends.

---

## 🧪 Testing the Load Balancer

### Manual Request

```bash
curl http://localhost:5001/
```

Send a few requests and observe them alternate between the backends.

### Simulate Failure

Stop one backend server and confirm that all traffic is now routed to the other. Restart it and it will be auto-included again.

### Concurrent Requests with `urls.txt`

```txt
url = "http://localhost:5001/"
url = "http://localhost:5001/"
url = "http://localhost:5001/"
url = "http://localhost:5001/"
```

Run with:

```bash
curl --parallel --parallel-immediate --parallel-max 3 --config urls.txt
```

---

## 🧪 Output Demo (Sample)

```text
Load Balancer listening on port 5001...
Connection received from ('127.0.0.1', 55002)
Forwarding request to backend 127.0.0.1:8080
Response sent back to client.

Connection received from ('127.0.0.1', 55003)
Forwarding request to backend 127.0.0.1:8081
Response sent back to client.
```

---


## 🧩 Future Improvements

- [ ] Add **async I/O** support via `asyncio`
- [ ] Add **logging** for monitoring performance & metrics
- [ ] Introduce **Docker** for easy container-based testing
- [ ] Build a **GUI dashboard** to visualize server status
- [ ] Implement **weighted routing** or **least connection** algorithms

---


## 🙌 Acknowledgments

This project was inspired by the "Build Your Own Load Balancer" challenge from [Coding Challenges]([https://codingchallenges.fyi/](https://codingchallenges.fyi/challenges/challenge-load-balancer)) and was completed as part of my system design and backend development learning journey.

---

## 🪪 License

This project is licensed under the MIT License.
