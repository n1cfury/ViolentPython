#!/usr/bin/env python
import ftplib

def banner():
	print "#### Find Webpages on FTP Server p59 ######"

def returnDefault(ftp):
	try:
		dirList = ftp.nlist()
	excetp:
		dirList = []
		print '[-] Could not list directory contents.'
		print '[-] Skipping To Next Target.'
		return
	retList = []
	for fileName in dirList:
		fn = fileName.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn:
			print '[+] Found default page: '+fileName
			retList.append(fileName)
		return retList

host = '192.168.95.179'
userName = 'guest'
passWord = 'guest'
ftp = ftplib.FTP9host()

ftp.login(userName, passWord)
returnDefault(ftp)