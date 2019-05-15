# Daily Text Email Script


This script will scrape the daily text off wol.jw.org and email it.
setup this up on a cron job to receive the daily text everyday.

Cron.d sytax: 1 17 * * * username /opt/daily-text-email.py

```
# Dependencies:
sudo apt install python3-pip -y
sudo pip3 install beautifulsoup4
```
