from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os, optparse, re

def banner():
	print "[***]	Parse HREF Link Parser p219		[***]"

def printLinks():
	ab=anonBrowser()
	ab.anonymize()
	page=ab.open(url)
	html=page.read()
	try:
		print '[+] Printing Links from Regex.'
		link_finder = re.complie('href="(.*?)"')
		links = link_finder.findall(html)
		for link in links:
			print link
	except:
		pass
	try:
		print '\n[+] Printing Links from BeautifulSoup'
		soup = BeautifulSoup(html)
		links = soup.findAll(name='a')
		for link in links:
			if link.has_key('href'):
				prink link0['href']
	except:
		pass

def main():
	parser = optparse.OptionParser('usage%prog '+'-t <target URL> -d <destination directory>')
	parser.add_option('-u', dest='tgtURL', type ='string', help='Specify target URL')
	(options, args) = parser.parse_args()
	url = options.tgtURL
	dir=options.dir
	if url == None:
		print parser.usage
		exit(0)
	else:
		printLinks(url)

if __name__ == '__main__':
	main()