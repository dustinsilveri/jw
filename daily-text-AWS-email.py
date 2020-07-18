#!/usr/bin/python3

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



#################################################################
# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Examining the Scriptures Daily <dustin.silveri@gmail.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT1 = "shannondustin2003@yahoo.com"
RECIPIENT2 = "dustin.silveri@gmail.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
#CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-west-2"

# The subject line for the email.
SUBJECT = "Daily Text " + todaysdate

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Examining the Scriptures Daily\r\n" + verse + citation )
            
# The HTML body of the email.
BODY_HTML = ("<html><head></head><body><h2>" + verse + "</h2><p>" + citation + "</a>.</p></body>+</html>")

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# Try to send the email.
try:
    #Provide the contents of the email.
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT1,
                RECIPIENT2,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        # If you are not using a configuration set, comment or delete the
        # following line
        #ConfigurationSetName=CONFIGURATION_SET,
    )
# Display an error if something goes wrong.	
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])

