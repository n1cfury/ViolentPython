import json, urllib
from anonBrowser import *

def banner():
	print "[***]	Mirroring images p227	[***]"

class reconPerson():
	def __init__(self, first_name, last_name):
		job = '', social_media={}:
		self.first_name = first_name
		self.last_name= last_name
		slef.job = jobs
		self.social_media = social_media

	def __repr__(self):
		return self.first_name+''+ self.last_name+'has job '+self.job

	def get_social(self, media_name):
		if self.social_media.has_key(media_name):
			return self.social_media[media_name]
		return None

	def query_twitter(self, query):
		query = urllib.quote_plus(query)
		results []
		browser= anonBrowser()
		response = browser.open('http://search.twitter.com/search.json?q='+query)
		json_objects = json.load(response)
		for result in json_objects['results']:
			new_result = {}
			new_result ['from_user'] = result ['text']
			new_result['geo'] = result['geo']
			new_result['tweet'] = result ['text']
			results.append(new_result)
		return results
ap= reconperson('Bookdock','Saint')
print ap.query_twitter('from:th3j34t5ter since:2010-01-01 include:retweets')		


def main():

if __name__ == '__main__':
	main()