# simple_http_server.py
import socket

HOST = '127.0.0.1'
PORT = 8080

def handle_request(request):
    return """HTTP/1.1 200 OK
Content-Type: text/html

<html><body><h1>Hello from My HTTP Server!</h1></body></html>
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server running on http://{HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            print(f"Request:\n{request}")
            response = handle_request(request)
            conn.sendall(response.encode())
