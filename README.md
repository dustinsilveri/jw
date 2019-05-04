# jw

# Created by van6uard


This script will scrape the daily text off wol.jw.org and email it.
setup this up on a cron job to receive the daily text everyday.

Cron.d sytax: 1 17 * * * username /opt/daily-text-email.py

# Dependancies:
sudo python3-pip -y
sudo pip3 install beautifulsoup4 -y

