from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from Summarize.parsers.html import HtmlParser 
from Summarize.parsers.plaintext import PlaintextParser
from Summarize.nlp.tokenizers import Tokenizer
from Summarize.summarizers.lsa import LsaSummarizer as Summarizer
from Summarize.nlp.stemmers import Stemmer
from Summarize.utils import get_stop_words


def summary(LANGUAGE, urlAsli, SENTENCES_COUNT):
	url = urlAsli
	parser = HtmlParser.from_url(url, Tokenizer("english"))
	# or for plain text files
	# parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	final = []
	
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		final.append(sentence)
	return final
