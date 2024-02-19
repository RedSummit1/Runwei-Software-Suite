#!../bin/python3
import csv
import feedparser

class FeedParserPro:

    def __init__(self):
        print("Parser online") 

        try:
            with open("test.csv",'r') as file:
                self.csv_headers = csv.DictReader(file) 
                self.csv_headers = next(self.csv_headers).keys() #Get the headers from the file object
        except:
            pass            

    def fetch(self,xmlFeed):
        self.RSS = feedparser.parse(xmlFeed) #Fetch RSS feed
        while(not self.RSS["feed"]): # If it is not there ...

            try:
                raise ValueError ("\n--> No feed received.\n--> Please enter another RSS feed URL.\n")
            except ValueError as err:
                print(err)

            try:
                self.RSS = feedparser.parse(input("URL: ")) # Anothor attempt to send a request
            except KeyboardInterrupt:
                break

        # <!-- TODO I AM ASSUMING THAT THIS IS A VALID RSS URL, NEED TO PUT ADDITIONAL CHECKS LATER

    



#
#
#
#
#        while(not self.RSS["feed"]):
#            try:
#                if not self.RSS["feed"]:
#                    raise SyntaxError (f"{self.RSS['bozo_exception']}\n\tPlease input a valid url.")
#            except SyntaxError as err:
#                print(err)
#                self.RSS = feedparser.parse(input())
#        print("Response Aquired")
#
#    def 
#        
#
#
#



