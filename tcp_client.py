import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

filename = "sample_file.txt"  # File to send
print(f"Sending file '{filename}'...")
with open(filename, "rb") as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

print("File sent successfully.")
client_socket.close()
