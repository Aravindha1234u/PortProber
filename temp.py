import socket
from threading import Thread

global HOST 
global PORT 

def send():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
		    print('Connected to', addr)
		    while True:
		        data = conn.recv(1024)
		        if not data:
		            break
		        conn.sendall(data)
		        
def receive():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'Hello, world')
		data = s.recv(1024)

	print('Received', repr(data))
	
if __name__ == '__main__':
	global HOST,PORT
	HOST = '127.0.0.1' 
	PORT = 65432
	Thread(target = send).start()
	Thread(target = receive).start()
