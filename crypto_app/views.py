# https://min-api.cryptocompare.com/documentation?key=News&cat=latestNewsArticlesEndpoint
from django.shortcuts import render


# Create your views here.
def index(request):
    # requests api
    import requests
    import json

    # grab price data
    price_url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD'
    price_request = requests.get(price_url)
    api_price = json.loads(price_request.content)

    # grabs news
    # api request put into variable
    api_url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
    api_request = requests.get(api_url)
    # convert into json which is easy to work with
    # content from the request we want
    # convert with json.loads and put into new variable
    api = json.loads(api_request.content)
    # pass api into homepage
    return render(request, 'index.html', {'api': api, 'api_price': api_price})
