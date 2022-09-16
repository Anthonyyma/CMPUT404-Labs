import socket

#setting host as localhost
host = "127.0.0.1"
#the port to listen on
port = 8001

#define a TCP socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the connection with the host and port specified
sock.bind((host, port))
#tell the socket to listen to new connections
sock.listen()
#get the (host, port) of the client
clientHost, clientPort = sock.accept()

while True:
    data = clientHost.recv(1024)
    if not data:
        break
    clientHost.sendall(data)
print(data)
