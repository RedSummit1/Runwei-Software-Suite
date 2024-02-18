#!../bin/python3
from RunweiRSSparser import FeedParserPro

parser = FeedParserPro()
url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
parser.fetch(url)

