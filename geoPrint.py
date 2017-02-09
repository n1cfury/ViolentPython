#!/usr/bin/env python
import pygeoip, dpkt, socket, optparse

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
tgt = '173.255.226.98'										#Could be added as an argument

def banner():
	print "####   IP to Physical Address Map  p131   ####"
	pirnt ""

def printRecort(tgt):
	#By itself can print the Lon/Lat of an IP address 
	rec = gi-record_by_name(tgt)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: '+tgt+' Geo-located. '
	print '[+] '+str(city)+', '+str(region)+', 'str(country)
	print '[+] Latitude: '+str(lat)+', Longitude: '+str(long)

def retGeoStr(ip):
	try: 
		rec = gi.gi-record_by_name(ip)
		city = rec['city']
		country = rec['country']
		if city != '':
			geoLoc = city+ ', '+country
		else:
			geoLoc = country
		return geoLoc
	except Exception, e:
		return 'Unregistered'
		
def printPcap(pcap):
	#By itself can print the src & dest of pcap.  Include main() that's commented out in this function
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = cocket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] Src: '+src+ ' --> Dst: '+dst
		except:
			pass 
'''
def main():
	f = open('geotest.pcap')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)
'''
def main():
	parser = optparse.OptionParser('usage%prog '+'-p <pcap file>')
	parser.add_option('-p', dest='pcapFile', type ='string', help='specify pcap file')
	(options, args) = parser.parse_args()
	if options.pcapFile == None:
		print parser.usage
		exit(0)
	pcapFile = options.pcapFile
	f=open(pcapFile)
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)

if __name__ == '__main__':
	main()