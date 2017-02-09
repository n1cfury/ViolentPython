#!/usr/bin/env python

def banner():
	print "####    Firefox Parsing tool p 116    ####"
	print ""

def printDownloads(downloadDB):
	conn = sqlite3.connect(downloadDB)
	c = conn.cursor()
	c.execute('SELECT name, source, datetime(endTime/100000.'unixepoch\') FROM moz_downloads;')
	print '\n[*] ---Files Downloaded ---'
	for row in c:
		print '[+] File: '+str(row[0])+' from source: '+str(row[1])+' at: '+str(row[2])

def printCookies(cookiesDB):
	try:
		conn=sqlite3.connect(cookiesDB)
		c = conn.cursor()
		c.execute('SELECT host, name, value FROM moz_cookies')
		print '\n[*] --Found Cookies-- '
		for row in c:
			

def printHistory(palcesDB):

def printGoogle(placesDB):

def main():

if __name__ == '__main__':
	main()