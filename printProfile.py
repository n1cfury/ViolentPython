#!/usr/bin/env python
import sqlite3, optparse, os


def banner():
	print "######    Skype DB Query p105  #######"
	print "__________-------------------_________"

def printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
	for row in c:
		print '[*] --Found Account--'
		print '[+] User: '+str(row[0])
		print '[+] Skype Username: '+str(row[1])
		print '[+] Location: '+str(row[2])+','+str(row[3])
		print '[+] Profile Date: '+str(row[4])

def printContacts(skypeDB):
	conn - sqlite3.connect(skypeDB)
	c = conn.cursor
	c.execure("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
	for row in c:
		print '\n[*] --Found Contact--'
		print '[+] User 	: '+str(row[0])
		print '[+] Skype Name 	: '+str(row[1])
		if str(row[2]) != '' and str(row[2]) != None:
			print '[+] Location 	: '+str(row[2])
		print '[+] User 	: '+str(row[0])
		print '[+] User 	: '+str(row[0])

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