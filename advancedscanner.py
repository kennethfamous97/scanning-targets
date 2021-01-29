#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		scok.connect((tgtHost, tgtPort))
		print ("[+] tcp open " + tgtPort)
	except: 
		print("[-] tcp closed " + tgtPort)
	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print("unknown host" + tgthost)
	try:
		tgtName = gethostbyaddr(tgtIP)
		print("[+] scan results for: " + tgtName[0])
	except: 
		print("[+] scan results for: " + tgtIP)
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()


def main():
	parser = optparse.OptionParser('usage of program: ' + '_H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify the host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
	(options, args) = parser.parse_args()
	tgtHost  = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print (parser.usage)
		exit(0)
	portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()
