#!../bin/python3
import csv
import feedparser
from chat import Chat
import os.path

class FeedParserPro:

    def __init__(self,append_file=False):
        print("Parser online") 

        if(append_file):
            notFile = True;
            while(notFile):
                try:
                    file = input("Please input a csv file to write to: ")
                    notFile = (not os.path.isfile(file)) or (".csv" not in file)
                except KeyboardInterrupt:
                    raise KeyboardInterrupt ("Abort program")

            with open(file,'r') as rfile:
                self.csv_headers = csv.DictReader(rfile)
                self.csv_headers = set(next(self.csv_headers).keys()) #Get the headers from the file object
                self.writer_csv = open("righthere.csv",'a')
                #self.writer_csv = csv.DictWriter(self.writer_csv,list(self.csv_headers))
        else:
            self.csv_headers = False
            self.missing = False

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

        if self.csv_headers: 
            FeedParserPro._diff(self)
        else:
            FeedParserPro._read_headers(self)
   
    def _diff(self):
        assert isinstance(self.csv_headers,set), "You need to fetch a RSS feed first"
        container = set()
        for l in self.RSS["entries"]:
            for l in l.keys():
                container.add(l)
        print(container)
        self.missing = (set(container) & self.csv_headers) ^ self.csv_headers

    def _read_headers(self):
        print("The headers are\n\n" + "\n".join(self.RSS.entries[0].keys()))
        self.csv_headers = list(self.RSS.entries[0].keys())

    def write(self,writeto=None):
        print("This is the write file")
        
        if self.missing:
            print("There is",len(self.missing),"label heade{} missing:".format("rs" if len(self.missing) > 1 else "r"),self.missing)
            
#            response = []
#            res = []
#            di = {}
#            if self.missing:
#                model = Chat()
#                print(self.missing)
#                for i,entry in enumerate(self.RSS["entries"][:1]):
#                    response.append(model.read("""
#
#                    Look through this RSS Feed channel response and give me a variable length record with the delimiter being a comma
#                    Example:{}
#
#                    Keys:{}
#                    xmlFeed:{}
#                    
#                    """.format("""
#                        (Key:value),\n
#                        """,self.missing,entry)))            
#
#                    response[i] = response[i].split('\n')
#                    print("Done")
#
#                #test = dict.fromkeys(list(self.missing),None);
#                response_list = (r.split('\n') for res in response for r in res)
#
#                #print("This is testing",testing)
#
#                entry_properties = {}
#                for i,lst in enumerate(response_list):
#                    var = lst[0].split(':')
#                    entry_properties.update({var[0]:var[1]})
#                    print("This is the entry right here\n",entry_properties)
#                    #print({var[0]:var[1] for var[0],var[1] in var})
#
#                self.writer_csv = csv.DictWriter(self.writer_csv,entry_properties.keys())
#                self.writer_csv.writerow(entry_properties)
#                print("WE ARE HERE")
#                
        else:
            print("Not missing")
            if not writeto:
                notFile = True
                while notFile:
                    try:
                        file = input("Please input a csv file to write to: ")
                        notFile = (not os.path.isfile(file)) or (".csv" not in file)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt ("Abort program")
                writeto = file
            with open(writeto, 'w') as file:
                self.writer_csv = csv.DictWriter(file,self.csv_headers)
                self.writer_csv.writeheader()
                for entry in self.RSS.entries:
                    self.writer_csv.writerow(entry)

            print("This is sooo cool!")




                




