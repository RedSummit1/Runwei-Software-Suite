from AuthenticateGoogleSheet import authenticate
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build


def spreadsheet():
    try:
        service = build("sheets", "v4", credentials=authenticate())
        sheet = service.spreadsheets()
    except HttpError as err:
        print(err)

    else:
        return sheet
        

