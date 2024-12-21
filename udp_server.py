import socket

# Create and bind the UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))
print("UDP Server is listening...")

# Open file to save the received data
with open("received_file.txt", "wb") as file:
    print("Receiving file...")
    while True:
        data, addr = server_socket.recvfrom(1024)  # Receive up to 1024 bytes
        if data == b"EOF":  # End-of-file marker
            print("File transfer complete.")
            break
        file.write(data)  # Write data to file

server_socket.close()
print("File saved as 'received_file.txt'")
