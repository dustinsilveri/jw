import boto3
from botocore.exceptions import ClientError
from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup

## SCRAPE ########################################################
## url prep for scraping
todaysdate = datetime.now().strftime("%Y/%m/%d")
quote_page = 'https://wol.jw.org/en/wol/dt/r1/lp-e/' + todaysdate
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

## scrape todays verse
verse = soup.find('p', attrs={'class': 'themeScrp'}).text.strip()
citation = soup.find('p', attrs={'class': 'sb'}).text.strip()

textmessage = "Examining the Scriptures Daily for " + todaysdate
textmessage += "\r\n\r\n"
textmessage += verse
textmessage += "\r\n\r\n" 
textmessage += citation



sns_client = boto3.client('sns')

response = sns_client.publish(
    PhoneNumber='+CHANGEME-PHONE',
    Message=textmessage,
)

print(response)


    #TopicArn='string', (Optional - can't be used with PhoneNumer)
    #TargetArn='string', (Optional - can't be used with PhoneNumer)
    #Subject='string', (Optional - not used with PhoneNumer)
    #MessageStructure='string' (Optional)

