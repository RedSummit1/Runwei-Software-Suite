#!../bin/python3
import csv
import feedparser
import os.path


class FeedParserPro:
    def __init__(self, append_file=False):
        print("Parser online") 

        if append_file: # If file not 
            notFile = True

            while notFile:
                try:
                    file = input("Please input a csv file to write to: ")
                    notFile = not (os.path.isfile(file) and file_path.endswith(".csv")) 
                except KeyboardInterrupt:
                    raise KeyboardInterrupt("Abort program")

            with open(file, "r") as readfile:
                self.csv_headers = csv.DictReader(readfile)
                self.csv_headers = set(next(self.csv_headers).keys())  # Get the headers from the file object
                self.writer_csv = open("righthere.csv", "a")
                # self.writer_csv = csv.DictWriter(self.writer_csv,list(self.csv_headers))
        else:
            self.csv_headers = False
            self.missing = False

    def fetch(self, xmlFeed):
        self.RSS = feedparser.parse(xmlFeed)  # Fetch RSS feed
        while not self.RSS["feed"]:  # If it is not there ...
            try:
                raise ValueError(
                    "\n--> No feed received.\n--> Please enter another RSS feed URL.\n"
                )
            except ValueError as err:
                print(err)

            try:
                self.RSS = feedparser.parse(input("URL: "))  # Anothor attempt to send a request
            except KeyboardInterrupt:
                break

        if self.csv_headers:
            FeedParserPro._diff(self)
        else:
            FeedParserPro._read_headers(self)

    def _diff(self):
        assert isinstance(self.csv_headers, set), "You need to fetch a RSS feed first"
        container = set()
        for l in self.RSS["entries"]:
            for l in l.keys():
                container.add(l)
        print(container)
        self.missing = (set(container) & self.csv_headers) ^ self.csv_headers

    def _read_headers(self):
        print("The headers are\n\n" + "\n".join(self.RSS.entries[0].keys()))
        self.csv_headers = list(self.RSS.entries[0].keys())

    def write(self, writeto=None):
            if not writeto:
                notFile = True
                while notFile:
                    try:
                        file = input("Please input a csv file to write to: ")
                        notFile = (not os.path.isfile(file)) or (".csv" not in file)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt("Abort program")
                writeto = file
            with open(writeto, "w") as file:
                self.writer_csv = csv.DictWriter(file, self.csv_headers)
                self.writer_csv.writeheader()
                for entry in self.RSS.entries:
                    self.writer_csv.writerow(entry)
