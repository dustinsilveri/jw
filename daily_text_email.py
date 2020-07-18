#!/usr/bin/env python3

#import needed modules
from urllib.request import urlopen
import smtplib
from bs4 import BeautifulSoup
from datetime import datetime

todaysdate = datetime.now().strftime("%Y/%m/%d")

# sms settings
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('CHANGEME-USERNAME', 'CHANGEME-PASSWORD')

# where to send
sender = 'wol.jw.org'
receiver = 'CHANGEME-EMAILADDRESS'

#url for scraping
quote_page = 'https://wol.jw.org/en/wol/dt/r1/lp-e/' + todaysdate
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

# scrape todays verse
name_box = soup.find('p', attrs={'class': 'themeScrp'})
name = name_box.text.strip()
dailytext = name.replace("\u2019","'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\xa0", " ").replace("\u2018","'")

# scrape todays scripture body
verse_body = soup.find('p', attrs={'class': 'sb'})
verse_unformatted = verse_body.text.strip()
verse_string = verse_unformatted.replace("\u2019","'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\xa0", " ").replace("\u2018","'")

# format for email body
full_daily_text = dailytext + "\n" + "############################" + "\n" + verse_string
subject = "today's daily text for " + todaysdate
message =  "Subject: {}\n\n{}".format(subject, full_daily_text)

server.sendmail(sender, receiver, message)

