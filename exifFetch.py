#!/usr/bin/env python
import urllib2, optparse
from ulrparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

def banner():
    print "#####  Read Metadata from Images p98  ####"
    print "##########################################"

def findImages(URL):
	print '[+] Finding images on '+url
	urlContent = ulrlib2.urlopen(url).read()
	soup = BeautifulSoup(urlContent)
	imgTags = soup.findAll('img')
	return imgTags

def downloadImage(imgTag):
	try:
		print '[+] Downloading image... '
		imgSrc = imgTag['src']
		imgContent = urllib2.urlopen(imgSrc).read()
		imgFileName = basename(urlspllit(imgSrc)[2])
		imgFile = open(imgFileName, 'wb')
		imfFile.write(imgContent)
		imgFile.close()
		return imgFileName
	except:
		return ''

def testForExit(imgFileName):
	try:
		exifData = {}
		imgFile = Image.open(imgFileName)
		info = imgFile._getexif()
		if info:
				for (tag, value) in info.items():
					decoded = TAGS.get(tag, tag)
					exifData[decoded] = value
					exifGPS = exifData['GPSInfo']
					if exifGPS:
						print '[*] '+imgFileName+' contains GPS MetaData'
	except:
		pass

def main():
	banner()
	parser = optparse.Optionparser("usage%prog"+"-u <target URL> ")
	parser.add_option('-u', dest='url', type='string', help='specify URL address')
	(optinos, args) = parser.parse_args()
	url = options.url
	if url == None:
		print parser.usage
		exit(0)
	else:
		imgTags = findImages(url)
		for imgTag in imgTags:
			imgFileName = downloadImage(imgTag)
			testForExit(imgFileName)

if __name__ == '__main__':
    main()