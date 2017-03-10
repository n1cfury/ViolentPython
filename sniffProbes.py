from scapy.all import *
interface = 'mon0'
probeReqs = []

def banner():
	print "[***]	802.11 Probe Requests p187	[***]"

def sniffProbe(p):
	if p.haslayer(Dot11ProbeReq):
		netName = p.getlayer(Dot11ProbeReq).info
		if netName not in probeReqs:
			probeReqs.append(netName)
			print '[+] Detected New Probe Request: '+netName

def main():
	def banner()
	sniff(iface=interface, prn=sniffProbe)

if __name__ == '__main__':
	main()