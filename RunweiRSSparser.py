#!../bin/python3

import feedparser

class FeedParserPro:

    def __init__(self):
        print("Parser online")

    def fetch(self,xmlFeed):
        self.RSS = feedparser.parse(xmlFeed)
        while(not self.RSS["feed"]):
            try:
                if not self.RSS["feed"]:
                    raise SyntaxError (f"{self.RSS['bozo_exception']}\n\tPlease input a valid url.")
            except SyntaxError as err:
                print(err)
                self.RSS = feedparser.parse(input())

        print("Response Aquired")

        






