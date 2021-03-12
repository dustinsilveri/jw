#!/usr/bin/python3

##################################################################
## Created by d_silv
## 
## This script will scrape the daily text off wol.jw.org and email it.  
## setup this up on a cron job to receive the daily text everyday.
## 
## Cron.d sytax: 1 17 * * * username /opt/daily-text-email.py
## 
## Dependancies: 
## sudo python3-pip -y
## sudo pip3 install beautifulsoup4 -y
##
##################################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

## Setup ########################################################
recipients_list = ['email@address1.com', 'email@address2.com']      # Receiving addresses go here
recipients = ','.join(recipients_list)                              # Do no change this line
password = "PASSWORD"                                               # Email Password goes here                                       
fromaddress = "sender@email.com"                                    # Sending email address
smtpserver = 'smtp.server.com: 587'                                 # SMTP server hostname and port

## SCRAPE ########################################################
## url prep for scraping
todaysdate = datetime.now().strftime("%Y/%m/%d")
quote_page = 'https://wol.jw.org/en/wol/dt/r1/lp-e/' + todaysdate
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

## scrape todays verse
verse = soup.find('p', attrs={'class': 'themeScrp'}).text.strip()
citation = soup.find('p', attrs={'class': 'sb'}).text.strip()
##################################################################

## EMAIL Setup ###################################################
## create message object instance
msg = MIMEMultipart()

## setup the parameters of the message
msg['From'] = fromaddress                               
msg['To'] = recipients
msg['Subject'] = "Daily Text for " + todaysdate 
 
## Create the body of the message (a plain-text and an HTML version).
#text = "" 
html = """
<html>
  <head></head>
  <body>
    <p><br>
      <b>""" + str(verse) + """ </b><br><br>
      """ + str(citation) + """
    </p>
  </body>
</html>
"""

## Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

## Attach parts into message container.
#msg.attach(part1)
msg.attach(part2)

## open connection to server and login
server = smtplib.SMTP(smtpserver)       
server.starttls()
server.login(msg['From'], password)
 
## send the message via the server and close the connection
server.sendmail(msg['From'], recipients_list, msg.as_string())
server.quit()

## no news is good news
print("successfully sent email to %s:" % (msg['To']))
