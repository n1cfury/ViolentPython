from bluetooth import *

def banner():
	print "[***]	RFCOMM scan p 206	[***]"

def rfcommCon(addr, port):
	sock = BluetoothSocket(RFCOMM)
	try:
		sock.connect((addr, port))
		print '[+] RFCOMM Port '+str(port)+' open'
		sock.close()
	except Exception, e:
		print '[-] RFCOMM Port '+str(port)+ ' closed'

def main():
	for port in range(1,30):
	rfcommCon('00:16:38:DE:AD:11', port)

if __name__ == '__main__':
	main()