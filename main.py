#!../bin/python3
from RunweiRSSparser import FeedParserPro
from GoogleSheet import create,writeValues

SAMPLE_SPREADSHEET_ID = "1l8f0nm4qQ2HLelE_iPC_MPSFTJUx0S8ifGi2b0Yq-0c"
SAMPLE_RANGE_NAME = "TestData!A1:C"

#parser = FeedParserPro() 
#parser.fetch(url)
#parser.write()
#url = "https://podcastfeeds.nbcnews.com/RPWEjhKq"

#sheetId = create()

print(writeValues(SAMPLE_SPREADSHEET_ID))

#print(writeValues(SAMPLE_SPREADSHEET_ID))
