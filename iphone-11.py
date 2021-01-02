import requests
import sys
from bs4 import BeautifulSoup
import pymsgbox

# get the urls for the specific sites
url_emag = 'https://www.emag.ro/telefon-mobil-apple-iphone-11-64gb-black-mwlt2rm-a/pd/D89ZX6BBM/?ref=fam#Negru'
url_altex = 'https://altex.ro/telefon-apple-iphone-11-64gb-black/cpd/SMTMWLT2RMA/'

# user agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}


# check price for both sites
def check_price():
    # get requests
    page_emag = requests.get(url_emag, headers=headers)
    page_altex = requests.get(url_altex, headers=headers)

    # parse the html
    soup_altex = BeautifulSoup(page_altex.content, 'html.parser')
    soup_emag = BeautifulSoup(page_emag.content, 'html.parser')

    # get price from specific classes
    get_price_altex = soup_altex.find(class_="Price-int").get_text()
    get_price_emag = soup_emag.find(class_="product-new-price").get_text()

    # convert to float
    price_emag = float(get_price_emag[:-7])
    price_altex = float(get_price_altex[:5])

    return price_emag, price_altex


# read the last prices
with open('iphoneprice.txt', 'r') as f1:
    str = f1.read()
    last_price_emag, last_price_altex = str.split()
    last_price_emag = float(last_price_emag)
    last_price_altex = float(last_price_altex)

# check the current price
curr_price_emag, curr_price_altex = check_price()


def check_low_price():
    # check for lower prices than last time
    ok = False
    if curr_price_emag < last_price_emag:
        pymsgbox.alert('The price on Emag is lower than last time', 'Warning')
        ok = True

    if curr_price_altex < last_price_altex:
        pymsgbox.alert(
            'The price on altex is lower than last time', 'Warning')
        ok = True
    if ok == False:
        pymsgbox.alert('Same price as last time', 'Warning')


check_low_price()


# write changes
with open('iphoneprice.txt', 'w') as f1:
    sys.stdout = f1
    print(curr_price_emag)
    print(curr_price_altex)
