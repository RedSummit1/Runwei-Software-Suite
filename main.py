#!../bin/python3
from RunweiRSSparser import FeedParserPro

parser = FeedParserPro(True)
url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
parser.fetch(url)
parser.write()

