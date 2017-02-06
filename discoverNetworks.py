#!/usr/bin/env python
from _winreg import *

def val2addr(val):
	addr = ''
	for ch in val:
		addr += '%02x '% ord(ch)
	addr = addr.strip(' ').replace(' ', ':')[0:17]
	return addr

def printNets():
	net = "SOFTARE\Microsoft\Windows NT\CurrentVersion"+"\Networklist\Signatures\Unmanaged"
	key = OpenKey(HKEY_LOCAL_MACHINE, net)
	print '\n[*] Networks you ahve joined.'
	for i in range(100):
		try:
			guid = EnumKey(key, i)
			netKey - OpenKey(keh, str(guid))
			(n, addr, t) = EnumValue(netKey, 5)
			(n,name, t) = EnumValue(netKey, 4)
			macAddr = val2addr(addr)
			netName = str(name)
			print '[+] '+netName+' '+macAddr
			CloseKey(netKey)
		except:
			break

def main():
	printNets()

if __name__ == '__main__':
	main()