import feedparser
import ssl
import webbrowser
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# SSL-Verifizierung deaktivierenls
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# RSS-Feed einlesen
rss_url = "https://www.finanzen.net/rss/news"
feed = feedparser.parse(rss_url)

# Schleife durch jeden Feed-Eintrag
for entry in feed.entries:
    print("Titel:", entry.title)
    print("Beschreibung:", entry.description)
    print("Link:", entry.link)
    print("\n")
    webbrowser.open(entry.link)