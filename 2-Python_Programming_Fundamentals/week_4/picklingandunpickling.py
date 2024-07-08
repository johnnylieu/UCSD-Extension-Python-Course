"""3. In this assignment you are to create a Pickle function that will take pickle the following dictionary:

{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
You will then need to run a client/server socket to transfer the file from the client to the server using the following code:

               ClientSocket.py Download ClientSocket.py   SocketServer.py Download SocketServer.py       

Once the code is received by the server you will need to unpickle the file in order to recover the dictionary.

Show all of your work and results with screenshots."""

import pickle

def pickling():
    # Pickle the dictionary and save it to a file
    prov_dict = {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
    # class lectures are outdated, we should be using with open
    with open('provided_dict.pickle', 'wb') as file:
        pickle.dump(prov_dict, file)