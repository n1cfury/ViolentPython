from bluetooth import *

def banner():
	print "[***]	Bluetooth SDP scan p207		[***]"

def sdpBrowse(addr):
	services = find_service(address=addr)
	for service in services:
		name = service['name']
		proto = service['protocol']
		port = str(service['port'])
		print '[+] Found '+str(name)+' on '+str(proto)+':'+port

def main():
	banner()
	sdpBrowse(addr)		#addr = MAC address

if __name__ == '__main__':
	main()