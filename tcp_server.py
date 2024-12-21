import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)
print("TCP Server is listening...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

with open("received_file.txt", "wb") as file:
    print("Receiving file...")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print("File received and saved as 'received_file.txt'")
conn.close()
server_socket.close()
