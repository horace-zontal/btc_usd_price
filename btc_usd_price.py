from lxml import html

import requests

page = requests.get('http://bitcoinexchangerate.org')

tree = html.fromstring(page.content)

price = tree.xpath('//*[@id="result"]/text()')

print price[0]
