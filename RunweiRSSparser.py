#!../bin/python3
import csv
import feedparser

class FeedParserPro:

    def __init__(self):
        print("Parser online") 

        try:
            with open("test.csv",'r') as rfile:
                self.csv_headers = csv.DictReader(rfile)
                self.csv_headers = set(next(self.csv_headers).keys()) #Get the headers from the file object
                self.writer_csv = open("test.csv",'a')
                self.writer_csv = csv.DictWriter(self.writer_csv,list(self.csv_headers))

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

        # <!-- TODO I AM ASSUMING THAT AT THIS POINT IT IS A VALID RSS URL, NEED TO PUT ADDITIONAL CHECKS LATER

        FeedParserPro._diff(self)

   
    def _diff(self):
        assert isinstance(self.csv_headers,set), "You need to fetch a RSS feed first"
        missing = (set(self.RSS.keymap) & self.csv_headers) ^ self.csv_headers
        print(missing)

    def write(self):
        csv = self.writer_csv
        print(type(csv))

                






































