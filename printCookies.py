import mechanize, cookielib

def banner():
	print "### prints cookies p2016 ###"

def printCookies(url):
	browser = mechanize.Browser()
	cookie_jar = cookielib.LWPCookieJar()
	page = brownser.open(url)
	for cookie in cookie_jar:
		prink cookie
url = 'http://www.syngress.com/'
print Cookies(url)