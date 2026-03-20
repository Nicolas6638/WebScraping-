import requests
from bs4 import BeautifulSoup
import time

def fetch_page():
    url = 'https://www.mercadolivre.com.br/apple-iphone-16-256-gb-preto-distribuidor-autorizado/p/MLB1040287796#polycard_client=search-desktop&search_layout=grid&position=2&type=product&tracking_id=962e90aa-c7f9-48ad-9a0a-4cfab0e325a5&wid=MLB3931272075&sid=search'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_page(html): 
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_= "ui-pdp-title").get_text()
    prices: list = soup.find_all('span', class_="andes-money-amount__fraction")
    old_price: int = int(prices[0].get_text().replace('.', ''))
    new_price: int = int(prices[1].get_text().replace('.', ''))
    installment_prices: int = int(prices[2].get_text().replace('.', ''))

    return{
        'product_name': product_name,
        'old_price' : old_price,
        'new_price': new_price,
        'installment_prices': installment_prices
    }

if __name__ == "__main__":
    while True:
        page_content = fetch_page()
        produto_info = parse_page(page_content)
        print(produto_info)
        time.sleep(10)