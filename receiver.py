import socket
clientsocket = socket.socket()
host = "127.0.0.1"
port = 4581



try:
	clientsocket.connect((host, port))
	print("connection established...")
except socket.error as e:
	print(str(e))

while True:
	Response = clientsocket.recv(1024)
	print(Response.decode("utf-8"))
	
clientsocket.close()