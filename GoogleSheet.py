from AuthenticateGoogleSheet import authenticate
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from RunweiRSSparser import FeedParserPro

def create():

    title = input("What is the name of the new spreadsheet? ")
    try:
        service = build("sheets", "v4", credentials=authenticate())
        spreadsheet = {'properties':{"title":title}}
        spreadsheet = (service.spreadsheets().create(body=spreadsheet,fields="spreadsheetId").execute())
        spreadSheetId = spreadsheet.get("spreadsheetId") 
        print("The url of the new spreadsheet is",f"https://docs.google.com/spreadsheets/d/{spreadSheetId}/edit#gid=0")
        return spreadSheetId

    except HttpError as err:
        print(err)
        
def writeValues(spreadSheetId:str):
    try:
        service = build("sheets","v4",credentials=authenticate())        
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadSheetId,range="TestData!A2:A")
            .execute()
        ) 
        rows = result.get("values",[])

        values = [] # Values to be written

#               Code that needs to be reviewed
#<------------------------------------------------------------------------>
        parser = FeedParserPro()

        #print(rows[0][0])
        #print(rows[1][0])
        #print(rows[2][0])
        #print(rows[3][0])
        #print(rows[4][0])
        #print(rows[5][0])

        #parser.fetch(rows[0][0])
        #parser.fetch(rows[4][0])
        #print(parser.csv_headers)
        csvheaders = ["title", "link", "summary", "published", "author"]
        csvheaders = {k : [] for k in csvheaders}
        for row in rows:
            parser.csv_headers = None
            parser.fetch(row[0])
            item = parser.RSS.items().mapping["entries"][0]
            #print("This is the item here",item,"\n\n\n\n")
            for k in csvheaders:
                csvheaders[k].append(item.get(k,None))
        values.append(list(csvheaders.keys()))
        print(values)
        #print(c for c in csvheaders.values())
        again = [*csvheaders.values()] 
        #print("\n\n\nTesting",again)
        print("Again",again)
        t = zip(*again)
        values.extend(list(z) for z in t)
        print(values)

#        for _ in values:
#            print(len(_),"\n")
#        

#        #values = [values[0].append(header) for header in csvheaders]
#        for row in rows:
#            parser.csv_headers = None
#            #breakpoint()
#            parser.fetch(rows[0][0])
#            print(parser.RSS.entries[0])
#            for k,v in parser.RSS.entries[0].items():
#                csvheaders[k].append("Testing") 
#
#        print(len(csvheaders.keys()) == len(csvheaders.values()))
#        #print(csvheaders.values())
#        values.extend([[*csvheaders.keys()]])
#        #print(len(csvheaders.values()))
#        for v in csvheaders.values():
#            values.append(v)
#        values = list(map(lambda x: x[:8],values))
#        print(len(values))
#
        #print(values[0])
        #values.extend(v for v in csvheaders.values())
#,[csvheaders.values()])

#<------------------------------------------------------------------------>

#        for _ in range(5):
#            values.append(list(range(0,5)))
#        print(values)
#
        print(values)
        body = {"values":values}
        print(len(body["values"]))
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId = spreadSheetId,
                range="B1:F7",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        return result

        #parser = FeedParserPro()
        #for i,valu











    except:
        pass
        

        
        
        
        
        
        
        
        
        
# Create() function: Will return sheet object if user has ID, else it will create one and return the url
# wRite() function: Will write the resulting values from the parser to spreadsheet
# Update() function: 
# 
#
