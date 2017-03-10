from scapy.all import *
dnsRecords = {}

def banner():
	print "[***]	Detect Fast Flux p152		[***]"

def handlePkt(pkt):
	if pkt.haslayer(DNSRR):
		rrname = pkt.getlayer(DNSRR).rrname
		rdata = pkt.getlayer(DNSRR).rdata
		if dnsRecords.has_key(rrname):
			if radata not in dnsRecords[rrname]:
				dnsRecords[rrname].append(rdata)

def main():
	banner()
	pkts = rdpcap('fastFlux.pcap')
	for pkt in pkts:
		handlePkt(pkt)
	for item in dnsRecords:
		print '[+] '+item+' has '+str(len(dnsRecords[item]))+' unique IPs.'

if __name__ == '__main__':
	main()