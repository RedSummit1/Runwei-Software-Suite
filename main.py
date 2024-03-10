#!../bin/python3
from RunweiRSSparser import FeedParserPro

parser = FeedParserPro()
url = "https://podcastfeeds.nbcnews.com/RPWEjhKq"
parser.fetch(url)
parser.write()

