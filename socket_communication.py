import socket

host = "example.com"
port = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"Hello, server!")
    data = s.recv(1024)

print(f"Received: {data.decode()}")
