from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nsetools import Nse
import time
import re
driver = webdriver.Firefox()
driver.get('https://economictimes.indiatimes.com')
nse = Nse()
stocks = nse.get_stock_codes()
stocks.pop('SYMBOL')
time.sleep(2)
OFile = open("stock_et_codes.txt", 'w+')
OFile1 = open("no_stock_et_codes.txt", 'w+')
et_id = None
try :
    for stock in list(stocks.keys()):
        inputElement = driver.find_element_by_class_name("inputBox")
        time.sleep(0.5)
        inputElement.send_keys(stock)
        time.sleep(2)

        try:
            link = driver.find_element_by_xpath(xpath="//ul[@class='searchListAll']/li[2]/a").get_attribute("href")
        except Exception as err:
            print("Unable to find link")
            OFile1.write(str(stock) + str(err) + '\n')
            inputElement.clear()

            continue
        OFile.write(str(link) + '\n')
        inputElement.clear()

        try:
            et_id = re.findall(r'companyid-(.*).cms', link)[0]

        except:
            print("unable to get et_id...")
            continue
        print(stock, et_id, link)
        inputElement.send_keys(Keys.ENTER)
except Exception as err:
    print("unable to get link")
    OFile1.write(str(stock) + str(err) + '\n')
