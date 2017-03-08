import mechanize
url = 'http://ip.nefsc.noaa.gov'
hideMeProxy = {'http':'216.155.139.115:3128'}

def banner():
	print "[***]	Anon Proxy p214		[***]"

def testProxy(url, proxy):
	browser = mechanize.Browser()
	browser.set_proxies(proxy)
	page = browser.open(url)
	source_code = page.read()
	print source_code

def main():
	banner()
	testProxy(url,hideMeProxy)

if __name__ == '__main__':
	main()