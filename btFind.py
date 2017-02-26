#!/usr/bin/env python
import time
from bluetooth import *

def banner():
	print "[***]	Bluetooth Detector p201	[***]"

def lookup_name(device):
	devList =discover_devices()
	for device in devList:
		name = str(lookup_name(device))
		print "[+] Found Bluetooth Device "+str(name)
		print "[+] MAC address: "+str(devices)
		alreadyFound.append(addr)
	while True:
		findDevs()
		time.sleep(5)

def findDevs():
	foundDevs = discover_devices(lookup_names = True)
	for (addr,name)



'''

def main():

if __name__ == '__main__':
	main()
'''
