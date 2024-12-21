# TCP/UDP Networking Project

## Overview
This project demonstrates the practical use of TCP and UDP protocols in a simple client-server application. It includes functionality for sending messages and transferring files, showcasing key differences between TCP and UDP.

## Features
1. **TCP Communication**:
   - Reliable, ordered message delivery between client and server.
   - File transfer functionality over TCP.
2. **UDP Communication**:
   - Fast, connectionless message delivery.
   - Example scenarios illustrating packet loss and out-of-order delivery.

## Technologies Used
- **Programming Language**: Python
- **Modules**: `socket`, `logging`

## Getting Started

### Prerequisites
1. Python 3.x installed on your machine.
2. Wireshark (optional) for monitoring network traffic.

### Project Files
- `tcp_server.py`: TCP server script.
- `tcp_client.py`: TCP client script.
- `udp_server.py`: UDP server script.
- `udp_client.py`: UDP client script.
- `sample_file.txt`: Example file for testing file transfer.

### Setup Instructions
1. Clone or download the project files into a directory.
2. Ensure all files are in the same directory.
3. Open a terminal and navigate to the project folder.

### Running the Project

#### TCP Communication
1. **Start the TCP Server**:
   ```bash
   python tcp_server.py
   ```
   - The server will start and listen on `127.0.0.1:12345`.
2. **Run the TCP Client**:
   ```bash
   python tcp_client.py
   ```
   - Messages will be sent to the server and echoed back.
   - For file transfer, ensure `sample_file.txt` exists in the client directory.

#### UDP Communication
1. **Start the UDP Server**:
   ```bash
   python udp_server.py
   ```
   - The server will start and listen on `127.0.0.1:12345`.
2. **Run the UDP Client**:
   ```bash
   python udp_client.py
   ```
   - Messages will be sent to the server. Observe potential packet loss or out-of-order delivery.

## Enhancements
1. Multi-client support for TCP using threading.
2. GUI-based client interface using `tkinter`.
3. Encryption for secure message transmission.
4. Performance metrics, such as transfer speed and packet loss rate.

## Real-World Applications
- TCP: Reliable data transfer for web applications, file downloads, and email.
- UDP: Low-latency communication for video streaming, VoIP, and gaming.

## Learning Outcomes
- Gained hands-on experience with the `socket` library in Python.
- Explored the differences and use cases of TCP and UDP.
- Developed an understanding of network protocols and their practical applications.

## Acknowledgments
- Python documentation for the `socket` module.
- Wireshark for network traffic monitoring.

## Contact
For questions or collaboration, please reach out to:
**[Your Name]**  
**Email**: [ryanfaxigue@gmail.com]  
**GitHub**: [RF746]

---

Thank you for exploring this project!

