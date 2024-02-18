#!../bin/python3
import csv
import feedparser

class FeedParserPro:

    def __init__(self,*args,csv_file,**kwargs):
        print("Parser online")
#        try:
#            with open(csv_file,'a') as file:
#                self.csv_file = file
#        except:
#            pass            

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


        






