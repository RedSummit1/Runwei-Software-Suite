#!../bin/python3

import feedparser

class FeedParserPro:

    def __init__(self):
        print("Parser online")

    def fetch(self,xmlFeed):
        self.RSS = feedparser.parse(xmlFeed)
        print(self.RSS.keymap)
            
        


