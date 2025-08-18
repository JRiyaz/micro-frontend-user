import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost and port
server_socket.bind(("localhost", 12345))

# Start listening for connections
server_socket.listen(10)

print("Server is waiting for connection...")

# Accept a connection
client_socket, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive and respond
while True:
    data = client_socket.recv(1024)  # Receive 1024 bytes
    if not data:
        break
    print("Client says:", data.decode())
    reply = input("Reply: ")
    client_socket.sendall(reply.encode())

# Close connection
client_socket.close()
