import socket
import threading

# AF_INET -> TCP/IP
# SOCK_STREAM -> Make a stream, vs discrete file
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Every server must live on a PORT, every process has a unique PORT.
# bind chooeses the port
HOSTNAME = '0.0.0.0' #socket.gethostname()
PORT = 7252
server_socket.bind((HOSTNAME, PORT))

# queue 
# number of clients that the socket can deal with at once.
server_socket.listen(5) 

def client_handle(client_socket):
    """
    TODO: need to handle losing a connection to a client, (or alternatively, 
    deliberately killing the client connection)
    """
    print("CLIENT HAS CONNECTED")
    print(client_socket.recv(1024)) # buffersize
    # can also send
    # on other end we can also send
    # 
    # recv -> need to sleep
    # 
    # if we need asynchronous communication, we need to develop a protocol
    # to figure out who's turn it is to send a message
    #
    # -- Start with recv loop to get all the initial information
    # 1) Client starts with a recv, sends, then sends done signal
    # -- Queues used for the threading (Queue.get sleep until needed)
    # -- Queue.put
    #
    #  For 'real' network communication, we need two threads a send and a receive
    #  and maybe use queue to send and receive messages fo the ports attached to
    #  the various parameter values which are sent over the network.

while True:
    # freeze program until client connects, then gets the address and opens a socket.
    # we can read to and write from the client_socket.
    client_socket, address = server_socket.accept()
    ct = threading.Thread(target=client_handle, args=(client_socket,))
    ct.start()
