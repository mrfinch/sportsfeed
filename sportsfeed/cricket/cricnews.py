from bs4 import BeautifulSoup
import urllib2

def getnews():
	url = "http://www.espncricinfo.com/rss/content/story/feeds/0.rss"
	req = urllib2.urlopen(url)
	resp = req.read()
	soup = BeautifulSoup(resp,"xml")
	all_news = []
	for n in soup.find_all('item'):
		news = {'title':n.title.get_text(),'description':n.description.get_text(),
				'link':n.guid.get_text(),'date':n.pubDate.get_text()}
		all_news.append(news)		
	return all_news