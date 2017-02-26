#!/usr/bin/env python
import re
def banner():
	print "[***]	Amex finder p 176	[***]"

def findCreditCard(pkt):
	americaRE = re.findall("3[47][0-9][13]".raw)
	if americaRE:
		print "[+] Found American Express Card: "+americaRE[0]

def main():
	tests = []
	tests.append("I would like to buy 1337 copies of that dvd")
	tests.append ("Bill my card: 378282246310005 for \$2600")
	for test in tests:
		findCreditCard(test)

if __name__ == '__main__':
	main()
