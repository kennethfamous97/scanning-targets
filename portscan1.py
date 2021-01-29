#!/usr/bin/python

import socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] enter the host address ")
port =  int(input("[*] enter the port address "))

def portscanner(port):
	if sock.connect_ex((host, port)):
		print ("port," + str(port) + " is closed") 
	else:
		print ("port," + str(port) + " is closed") 
portscanner(port)

