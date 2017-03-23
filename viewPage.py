import mechanize

def banner():
	print "[***]	Page Viewer p213	[***]"

def viewPage(url):
	browser = mechanize.Browser()
	page = browser.open(url)
	source_code=page.read()
	print source_code

def main():
	banner()
	viewPage('http://www.syngress.com')

if __name__ == '__main__':
	main()