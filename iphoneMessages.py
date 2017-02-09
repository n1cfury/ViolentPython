#!/usr/bin/env python
import os, sqlite3

def banner():
	print "#### iTunes mobile backup inspector p121   ######"
	print ""

def iphoneTables(iphoneDB):
	#By itself this function will enumerate database schema
	try:
		conn=sqlite3.connect(iphoneDB)
		c=conn.cursor()
		c.execute('SELECT tbl_name FROM sqlite_master WHERE type==\"table\":')
		print "\n[*] Database: "+iphoneDB
		for row in c:
			print "\n[-[ Table: "+str(row)
	except:
		pass
	conn.close()
dirList = os.listdir(os.getcwd())
for fileName in dirList:
	printTables(filename)

def isMessageTable(iphoneDB):
	try:
		conn - sqlite3.connect(iphoneDB)
		c - conn.cursor()
		c.execute('SELECT tbl_name FROM sqlite_master WHERE type ==\"table\";')
		for row in c:
			if 'message in str(row):'
				return True
	except:
		reutrn False

def printMessage(msgDB)
	try:
		c - conn.cursor()
		c.execute('SELECT datetime(date,\'unixepoch\;), address, text from message where address>0:')
		for row in c:
			date = str(row[0])
			addr - str(row[1])
			text - row[2]
			print '\n[+] Date: '_date+', Addr: '+addr+' Message: '+text
	except:
		pass

def main():
	parser = optparse.OptionParser('usage%prog '+'-p <iphone backup directory')
	parser.add_option('-p', dest='pathName', type ='string', help='Specify Skype Profile path')
	(options, args) = parser.parse_args()
	pathName = options.pathName
	if pathName == None:
		print parser.usage
		exit(0)
	else:
		dirList = os.listdir(pathName)
		for fileName in dirList:
			iphoneDB = os.path.join(pathName, fileName)
			if isMessageTable(iphoneDB):
				try:
					print '\n[*] ---Found Messages---'
					printMessage(iphoneDB)
				except:
					pass

if __name__ == '__main__':
	main()