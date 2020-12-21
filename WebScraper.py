import requests
from bs4 import BeautifulSoup

url = 'https://www.emag.ro/laptop-apple-macbook-air-13-inch-true-tone-procesor-apple-m1-8-nuclee-cpu-si-8-nuclee-gpu-8gb-512gb-gold-int-kb-mgne3ze-a/pd/DM6BL7MBM/?ref=graph_profiled_similar_c_1_2&provider=rec&recid=rec_49_16_u2034550492514704261_91_C_ca82e2f6feb80b89b31eba3cc94e74febcb355cd836da1444147626a4132d11f_1608575391&scenario_ID=49'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
# sure thing buddy


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    get_price = soup.find(class_="product-new-price").get_text()
    price = float(get_price[:-7])

    print(price)


check_price()
