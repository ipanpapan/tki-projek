import urllib2
from bs4 import BeautifulSoup
from Stemmer.StemmerFactory import StemmerFactory

def StartStem(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page,"lxml")
	text = " ".join(map(lambda p: p.text, soup.find_all('p')))
	# create stemmer 
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()

	output   = stemmer.stem(text.encode('ascii','ignore'))
	return output
 