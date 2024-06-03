import socket
import pickle

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind(('127.0.0.1', 1234))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening for incoming connections...")

while True:
    # Accept incoming connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Receive the pickled file from the client
    data = conn.recv(4096)

    # Unpickle the received data to recover the dictionary
    recovered_dict = pickle.loads(data)

    # Print or manipulate the recovered dictionary as needed
    print("Recovered Dictionary:", recovered_dict)

    # Close the connection
    conn.close()