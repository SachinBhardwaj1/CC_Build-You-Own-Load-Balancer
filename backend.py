# Using Multiprocessing

from flask import Flask
from multiprocessing import Process

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Congrats!!!! Backend Server is working\n", 200

    return app

def run_app(port):
    app = create_app()
    app.run(port=port)

if __name__ == "__main__":
    ports = [8080, 8081]

    processes = []
    for port in ports:
        p = Process(target=run_app, args=(port,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()