import requests

import re

res = requests.get('https://economictimes.indiatimes.com/hdfc-bank-ltd/stocks/companyid-9195.cms')
res = res.text
regexes = ['nse_tab mkt_cap tar.?>.*?<']
for i in regexes:
    new = re.findall(i, res)[0]
    value = re.findall('\d+\.\d+', new)
    print(new, value)
