from bs4 import BeautifulSoup
import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = 'https://www.samsung.com/us/smartphones/galaxy-s21-ultra-5g/models/'
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')


def get_model_start_price(model_name):
    price = "no price found"
    for link in soup.body.find_all('section'):
        if 'm_content-device' in str(link.get('class')):
            for li in link.find_all('li'):
                if li.get('class') and model_name in li.get('class') and 'model-start-price' in li.p['class']:
                    price = li.p.get_text().split(':')[1]

    return price


for model in ('s21-ultra', 's21-plus', 's21'):
    price = get_model_start_price(model)
    print('for ', model, ' start price: ', price)