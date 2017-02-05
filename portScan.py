#Port Scanner, p 38

import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def banner():
	print "#####   Port Scanner p 38   #####"
	print ""

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send("ViolentPython\r\n")
		results = connSkt.recv(100)
		screenlock.acquire()
		print "[+]%d/tcp open" % tgtPort
		print "[+] " + str(resutls)
	except:
		screenLock.acquire()
		print "[-]%d/tcp closed" % tgtPort
	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host" % tgtHost
		return
	try:
		tgtName = gethostbyname(tgtHost)
		print "\n[+] Scan Results for: "+tgtName[0]
	except:
		print "\n[+] Scan Results for: "+tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args= (tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('useage%prog '+"-H <target hsot> -p <target port>")
	parser.add_option("-P, dest="tgtPort", type ="string", help = "specify target port[s] separated by comma"")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	thtPorts = str(options.tgtPort).split(", ")
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.useage
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == "__main__":
	main()

















