import dpkt, optparse, socket
THRESH = 1000

def banner():
	print "[***]	Find DDoS p 142		[***]"

def findDownload(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
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
			src = socket.inet_ntoa(ip.src)
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
	pktCount = ()
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			tcp = ip.data
			dport = tcp.dport
			if dport == 80:
				stream = src+':'+dst
				if pktCount.has_key(stream):
					pktCount[stream] = pktCount[stream]+1
				else:
					pktCount[stream] = 1
		except:
			pass
	for stream in pktCount:
		pktsSent = pktCount[stream]
		if pktsSent > THRESH:
			src = stream.split(':')[0]
			dst = stream.split(':')[1]
			print '[+] '+src+' attacked '+dst+' with '+str(pktsSent)+' pkts.'

def main():
	parser = optparse.OptionParser('usage%prog '+'-p<pcap file> -t <thesh>>')
	parser.add_option('-p', dest ='pcapFile', type='string', help ='specify pcap filename')
	parser.add_option('-t', dest ='thresh', type='int', help ='specify threshold count')
	(options, args) = parser.parse_args()
	if options.pcapFile == None:
		print parser.usage
		exit(0)
	if options.thresh != None:
		THRESH = options.thresh
	pcapFile = options.pcapFile
	f = open(pcapFile)
	pcap = dpkt.pcap.Reader(f)
	findDownload(pcap)
	findHivemind(pcap)
	findAttack(pcap)

if __name__ == '__main__':
	main()