import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 12345))

while True:
    message = input("You: ")
    if message.lower() == "exit":
        break
    client_socket.sendall(message.encode())  # Send message
    data = client_socket.recv(1024)  # Receive response
    print("Server:", data.decode())

# Close connection
client_socket.close()
