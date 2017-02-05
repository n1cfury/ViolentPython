

import ftplib

def banner():
	print "#####  Anonymous FTP Scanner  p57 #######"

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] '+str(hostname)+ 'FTP Anonymous Login Succeeded.'
		ftp.quit()
		return True
	except Exception e:
		print '\n[-] '+str(hostname)+ 'FTP Anonymous Login Failed.'
		return False

host = '192.168.95.179'
anonLogin(host)
