#!/usr/bin/env python
import sqlite3, optparse, os


def banner():
	print "######    Skype DB Query p105  #######"
	print "__________-------------------_________"

def printProfile(skypeDB):

def printContacts(skypeDB):

def printCallLog(skypeDB):

def printMessages(skypeDB):


def main():
	parser = optparse.OptionParser('usage%prog '+'-p <Skype Profile Path>')
	parser.add_option('-p', dest='pathname', type ='string', help ='specify skype profile path')
	(options, args) = parser.parse_args()
	pathname = options.pathname
	if pathname == None:
		print parser.usage
		exit(0)
	elif os.path.isdir(pathName) == Fa;se:
		print '[!] Path Does not exist: '+pathname
		exit(0)
	else:
		skypeDB = os.path.join(pathname, 'main.db')
		if os.path.isfile(skypeDB):
			printProfile(skypeDB)
			printContacts(skypdDB)
			printCallLog(skypeDB)
			printMessages(skypeDB)
	else:
		print '[!] Skype Database '+'does not exist: '+skypeDB







if __name__ == '__main__':
	main()