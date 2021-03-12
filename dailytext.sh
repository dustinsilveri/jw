#!/usr/bin/env python3

#import needed modules
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, Back, Style


def daily_text():
    todaysdate = datetime.now().strftime("%Y/%m/%d")
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
    complete = Style.BRIGHT + Fore.RED + dailytext + Fore.RESET +  '\n' + verse_string

    print(complete + "\r")
    print(quote_page)
daily_text()
