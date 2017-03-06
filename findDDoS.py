import dpkt, optparse, socket
THRESH = 1000

def banner():
	print "[***]	Find DDoS p 142		[***]"

def findDownload(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip, src)
			tcp = ip.data
			http = dpkt.http.Request(tcp.data)
			if http.method == 'GET':
				url = http.url.lower()
				if '.zip' in url and 'loic' in url:
					print '[!] '+src+' Downloaded LOIC.'
		except:
			pass

def findHivemind(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip, src)
			tcp = ip.data
			dport = tcp.dport
			sport = tcp.sport
			if dport == 6667:
				if '!lazor' in tcp.data.lower():
					print '[] DDoS Hivemind issued by: '+src
					print '[] Target CMD: '+tcp.data
			if sport == 6667:
				if '!lazor' in tcp.data.lower():
					print '[!] DDoS Hivemind issued to: '+src
					print '[+] Target CMD: '+tcp.data
		except:
			pass

def findAttack(pcap):

def main():

if __name__ == '__main__':
	main()