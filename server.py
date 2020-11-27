import socket
from _thread import *
serversocket = socket.socket()
host = "127.0.0.1"
port = 4581
threadCount = 0
c = []

serversocket.bind((host, port))
serversocket.listen(5)

def client_thread(a):
	while True:
		ca = a[0]
		cb = a[1]
		data = ca.recv(1024)
		cb.send(data)

while True:
	client, addr = serversocket.accept()
	c.append(client)
	if len(c) == 2:
		start_new_thread(client_thread, (c,))
	threadCount += 1
	print("threadCount" + str(threadCount))
		
serversocket.close() 