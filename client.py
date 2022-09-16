import socket

#define a TCP socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to www.google.com using port 80
sock.connect(("www.google.com", 80))
#send out a GET request
sock.send(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")
#receive the response with a maximum message length of 4096
response = sock.recv(4096)
#close the socket connection
sock.close()
#print out the response after decoding it
print(response.decode())
