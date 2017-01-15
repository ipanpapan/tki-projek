from Stemming import StartStem

from Summarize.parsers.html import HtmlParser
from Summarize.parsers.plaintext import PlaintextParser
from Summarize.nlp.tokenizers import Tokenizer
from Summarize.summarizers.lsa import LsaSummarizer as Summarizer
from Summarize.nlp.stemmers import Stemmer
from Summarize.utils import get_stop_words

LANGUAGE = "indonesia"
SENTENCES_COUNT = 10

berita = StartStem(raw_input("Masukan URL: "))
print berita
# summarizer = Summarizer(berita)
# summarizer.stop_words = get_stop_words(LANGUAGE)
# for sentence in summarizer(parser.document, SENTENCES_COUNT):
#     print(sentence)
