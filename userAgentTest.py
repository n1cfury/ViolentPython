import mechanize

def banner():
	print "[***]	Proxy p215		[***]"

def testUserAgent(url, userAgent):
	browser = mechanize.Browser()
	browser.addheaders = userAgent
	page = browser.open(url)
	source_code = page.read()
	print source_code

url = 'http://whatismyuseragent.dotdoh.com/'
userAgent = [('User-agent', 'Mozilla/5.0 (x11: U; '+'Linux 2.4.2-2 i586; en-US; m18) Gecho/20010131 Netscape6/6.01')]

def main():
	banner()
	testUserAgent(url, userAgent)

if __name__ == '__main__':
	main()