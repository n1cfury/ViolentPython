import urllib, json, re, urllib2, optparse
from anonBrowser import *

def banner():
	print "[***]	Mirroring images p231-236			[***] "
	print "[*] This actually starts on 231.  The reconPerson  "
	print "Class gathers info from the user such as interests "
	print "tweets and hashtags. 							  "

class reconPerson:
	def __init__(self, handle):
		self.handle = handle
		self.tweets - self.get_tweets()

	def get_tweets(self):
		query = urllib.quote_plus('from:'+self.handle+' since:2009-01-01 include:retweets')
		tweets = []
		browser = anonBrowser()
		browser.anonymize()
		response = browser.open('http://search.twitter.com/'+'search.json?q='+query)
		json_objects = json.load(resepone)
		for result in json_objects['resutls']:
			new_result = {}
			new_result['from_user']=result['from_user_name']
			new_result['geo'] = result['geo']
			new_result['tweet']= result['text']
			tweets.append(new_result)
		return tweets

	def find_interests(tweets):
		interests = {}
		interests['links'] = []
		interests['users']= []
		interests['hashtags'] = []
		for tweet in self.tweets:
			text = tweet['tweet']
			links = re.compile('(http.*?)\Z|(http.*?) ').findall(text)
			for link in links:
				if link[0]:
					link = link[0]
				elif link[1]:
					link = link[1]
				else:
					continue
			try:
				response = urllib2.urlopen(link)
				full_link = response.url
		interests['links'].append(full_link)
			except:
				pass
				interests['users'] += re.compile('(@\w+)').findall(text)
				interests['hashtags'] += re.compile('(#\w+)').findall(text)
				interests['users'].sort()
				interests['hashtags'].sort()
				interests['links'].sort()
				return interests

	def twitter_locate(self, cityFile):
		cities =[]
		if cityFile != None:
			for line in open(cityFile).readlines():
				city = line.strip('\n').strip('\r').lower()
				cities.append(city)
		locations = []
		locCnt = 0
		cityCnt = 0
		tweetsText = ''
		for tweet in self.tweets:
			if tweet['geo'] != None:
				loocations.append(tweet['geo'])
				locCnt +=1
				tweetsText += tweet['tweet'].lower()
		for city in cities:
			if city in tweetsText:
				locations.append(city)
				cityCnt += 1
		return locations

def main():
	banner()
	parser = optparse.Optionparser("usage%prog "+"-u <twitter handle> ")
	parser.add_option('-u', dest='handle', type='string', help='specify Twitter handle')
	(options, args) = parser.parse_args()
	handle = options.handle
	if handle == None:
		print parser.usage
		exit(0)
	tweets = get_tweets(handle)
	interests = find_interests(tweets)
	print '\n[+] Links.'
	for link in set(interests['links']):
		print '[+] '+str(link)
	print '\n [+] Users.'
	for user in set(interests['users']):
		print '[+] '+str(user)
	print '\n [+] Hashtags.'
	for hashtag in set(interests['hashtags']):
		print '[+] '+ str(hashtag)

if __name__ == '__main__':
	main()