#!/bin/python3
import socket
import argparse
import time
import sys
from threading import Thread

HOST = None
PORT = None

def send():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		try:
			s.bind((HOST, PORT))
		except OSError as e:
			print("Address already in use")
			exit()
		except Exception:
			print("Sorry Something Went Wrong!!")
			exit()
		s.listen()
		conn, addr = s.accept()
		with conn:
		    #print('Connected to', addr)
		    while True:
		        data = conn.recv(1024)
		        if not data:
		            break
		        conn.sendall(data)
		        
def receive():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.settimeout(5)
		try:
			s.sendall(b'T3cH_W1z4rD')
			data = s.recv(1024)
		except socket.timeout:
			exit()
	
	#print('Received', repr(data))
	if len(repr(data))>0:
		print("Port {} is Forwardable".format(PORT))
	else:
		print("Port {} is Not Forwardable".format(PORT))

def banner():
	print("\033[96m")
	print(r'''      :::::::::   ::::::::  ::::::::: :::::::::::        :::::::::  :::::::::   ::::::::  :::::::::  :::::::::: ::::::::: 
     :+:    :+: :+:    :+: :+:    :+:    :+:            :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+: 
    +:+    +:+ +:+    +:+ +:+    +:+    +:+            +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+        +:+    +:+  
   +#++:++#+  +#+    +:+ +#++:++#:     +#+            +#++:++#+  +#++:++#:  +#+    +:+ +#++:++#+  +#++:++#   +#++:++#:    
  +#+        +#+    +#+ +#+    +#+    +#+            +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+        +#+    +#+    
 #+#        #+#    #+# #+#    #+#    #+#            #+#        #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+#     
###         ########  ###    ###    ###            ###        ###    ###  ########  #########  ########## ###    ###    ''')
	print("\n\033[00m")

def scanner():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	print("")
	try:
		if args.host:
			ip=socket.gethostbyname_ex(args.host)[2][0]
		else:
			ip=args.ip
		if args.PORT:
			print("Scanning {} on {}".format(ip,args.PORT))
			for port in args.PORT.split():
				if s.connect_ex((ip,int(port)))==0:
					print("Port {} is OPEN".format(port))
				else:
					if args.a==True:
						print("Port {} is CLOSED".format(port))
					pass
				s.close()
		else:
				portrange=args.port
				print("Scanning {} for range {}".format(ip,portrange))
				for port in range(1,portrange):
					code=s.connect_ex((ip,port))
					if code==0:
						print("Port {} is OPEN".format(port))
					elif args.a==True:
						if code==11:
							print("Port {} is Filtered".format(port))
						else:
							print("Port {} is CLOSED".format(port))
	except socket.gaierror: 
		print("Unknown Host: ",ip)
	except KeyboardInterrupt:
		print("\nExiting...")
	finally:
		print("\nThank You")
	
if __name__=='__main__':
	banner()
	parser=argparse.ArgumentParser(description="Port Prober \n\nexample: python3 main.py -i 172.217.31.196 -p 1000\n         python3 main.py -H www.google.com -P \"21 22 53 80 443 445\" ",formatter_class=argparse.RawTextHelpFormatter)

	parser.add_argument('-i',"--ip",default="127.0.0.1",help='IP Address of Host (default: 127.0.0.1) ')
	parser.add_argument('-H',"--host",default="localhost",type=str,help='Host Name (default: secarmy.org) ')
	parser.add_argument('-p',"--port",type=int,default=1000,help='Range of Port')
	parser.add_argument('-a',action="store_true",help='Aggressive Scanning')
	parser.add_argument('-P',"--PORT",type=str,help='List of Particular Ports (Example: --PORT "21 22 80 443")')
	parser.add_argument("-v", "--version", help="Prints Version", action="store_true")
	parser.add_argument("-f", "--port-forwardable", dest='pf',type=int,help="To Check whether Open Port is Forwardable or not")
	args = parser.parse_args()
	count=4
	while count!=0:
		sys.stdout.write('\rStarting the Scanner |')
		time.sleep(0.1)
		sys.stdout.write('\rStarting the Scanner /')
		time.sleep(0.1)
		sys.stdout.write('\rStarting the Scanner -')
		time.sleep(0.1)
		sys.stdout.write('\rStarting the Scanner \\')
		time.sleep(0.1)
		count-=1
	sys.stdout.write('\rDone!                  ')
	print()
	if args.version==True:
			print("Version: 1.0.0")
			exit()
	elif args.pf:
			if args.host:
				ip=socket.gethostbyname_ex(args.host)[2][0]
			else:
				ip=args.ip
			HOST = ip
			PORT=args.pf
			print("Checking for Forwarding")
			Thread(target = send).start()
			Thread(target = receive).start()
	else:
		scanner()
