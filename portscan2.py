import socket 
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] enter the host address ")

def portscanner(port):
        if sock.connect_ex((host, port)):
                print ("port," + str(port) + " is closed", 'red') 
        else:
                print ("port," + str(port) + " is open", 'green') 
for port in range (1,100):
	
	portscanner(port)
