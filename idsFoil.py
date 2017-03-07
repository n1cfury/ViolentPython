#!/usr/bin/env python
import optparse
from scapy.all import *
from random import randint


def banner():
	print "[***]	Intrusion Detection Bypass p 166	[***]"

def ddosTest(src, dst, iface, count):

def exploitTest(src, dst, iface, count):

def scanTest(src, dst, iface, count):

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

