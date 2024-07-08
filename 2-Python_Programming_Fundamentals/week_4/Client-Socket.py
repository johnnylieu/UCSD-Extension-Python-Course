import socket
import pickle
import picklingandunpickling as p

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('127.0.0.1', 1234))

p.pickling()

# Load the pickled file
with open('provided_dict.pickle', 'rb') as file:
    pickled_data = file.read()

# Send the pickled file to the server
client_socket.sendall(pickled_data)

# Close the connection
client_socket.close()