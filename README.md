# btc_usd_price

Scrapes current bitcoin price (in usd) from http://bitcoinexchangerate.org

I email the price twice a day via cron on my mac like this:
0 6,18 * * * cd /Path/To/File && python btc_usd_price.py | mail -s BTC_Price my.email_address.com

Please consider donating a little bitcoin to bitcoinexchangerate.org if you do this regulary.
