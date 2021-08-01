import socket 
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7252
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect( (SERVER_IP, SERVER_PORT) )
client_socket.send(b'hey dude')

