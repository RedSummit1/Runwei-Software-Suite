from AuthenticateGoogleSheet import authenticate
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

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
        return rows
    except:
        pass
        

        
        
        
        
        
        
        
        
        
# Create() function: Will return sheet object if user has ID, else it will create one and return the url
# wRite() function: Will write the resulting values from the parser to spreadsheet
# Update() function: 
# 
#
