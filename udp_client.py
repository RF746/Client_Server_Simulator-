import socket

# Create the UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 12345)

filename = "sample_file.txt"  # File to send
print(f"Sending file '{filename}'...")
try:
    with open(filename, "rb") as file:
        data = file.read(1024)  # Read file in chunks of 1024 bytes
        while data:
            client_socket.sendto(data, server_address)  # Send each chunk
            data = file.read(1024)  # Read the next chunk

    # Send end-of-file marker
    client_socket.sendto(b"EOF", server_address)
    print("File sent successfully.")
finally:
    client_socket.close()
