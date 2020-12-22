import requests
import sys
from bs4 import BeautifulSoup
import pymsgbox

# get the urls for the specific sites
url_emag = 'https://www.emag.ro/laptop-apple-macbook-air-13-inch-true-tone-procesor-apple-m1-8-nuclee-cpu-si-7-nuclee-gpu-8gb-256gb-gold-int-kb-mgnd3ze-a/pd/DY6BL7MBM/'
url_istyle = 'https://istyle.ro/macbook-air-13-3-m1-chip-8-core-cpu-256gb-ssd-space-grey.html'

# user agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}


# check price for both sites
def check_price():
    # get requests
    page_emag = requests.get(url_emag, headers=headers)
    page_istyle = requests.get(url_istyle, headers=headers)

    # parse the html
    soup_istyle = BeautifulSoup(page_istyle.content, 'html.parser')
    soup_emag = BeautifulSoup(page_emag.content, 'html.parser')

    # get price from specific classes
    get_price_istyle = soup_istyle.find(class_="price").get_text()
    get_price_emag = soup_emag.find(class_="product-new-price").get_text()

    # convert to float
    price_emag = float(get_price_emag[:-7])
    price_istyle = float(get_price_istyle[:-7].replace(" ", "."))

    return price_emag, price_istyle


# read the last prices
with open('/home/cristic/Projects/Track_Price_WebScraper/lastprice.txt', 'r') as f1:
    str = f1.read()
    last_price_emag, last_price_istyle = str.split()
    last_price_emag = float(last_price_emag)
    last_price_istyle = float(last_price_istyle)

# check the current price
curr_price_emag, curr_price_istyle = check_price()


def check_low_price():
    # check for lower prices than last time
    if curr_price_emag < last_price_emag:
        pymsgbox.alert('The price on Emag is lower than last time', 'Warning')
        return

    if curr_price_istyle < last_price_istyle:
        pymsgbox.alert(
            'The price on istyle is lower than last time', 'Warning')
        return

    pymsgbox.alert('Same price as last time', 'Warning')


check_low_price()


# write changes
with open('/home/cristic/Projects/Track_Price_WebScraper/lastprice.txt', 'w') as f1:
    sys.stdout = f1
    print(curr_price_emag)
    print(curr_price_istyle)

# TO DO:
# run on startup
