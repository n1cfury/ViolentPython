#!/usr/bin/env python

import crypt

def banner():
	print "######################################"
	print "#  vP Password Cracker by: n1cfury   #"
	print "######################################"
	print ""

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt', 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
	print "[-] Password Not Found.\n"
	return

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
	#	if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password for: "+user
			testPass(cryptPass)
			
#		else:
#			print usage

if __name__ == "__main__":
	main()