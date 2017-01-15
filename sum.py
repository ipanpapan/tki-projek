from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
LANGUAGE2 = "bahasa"
SENTENCES_COUNT = 3


def summari(urlAsli):
    url = urlAsli
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    final = []

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE2)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        final.append(sentence)

    return final
