import requests
from .datamodels.quote import Quote
import json

base_url = 'https://api.iextrading.com/1.0'

def get_stocks(symbol):
    '''
    Gets Quote for given stock ticker

    TAKES:
    symbols: string of stock ticker eg. (AAPL, FB)

    RETURNS:
    Quote: quote object of json response. If error exists, quote object will contain error message
    '''

    api_url = '/stock/{}/quote'.format(symbol)
    url = base_url + api_url

    response = requests.get(url)
    if response.text == "Unknown symbol":
        quote = Quote()
        quote.error = "Unknown symbol"
        return quote
    
    try:
        quote_dic = response.json()
    except json.decoder.JSONDecodeError:
        quote = Quote()
        quote.error = "invalid json"
        return quote
        

    quote = Quote(quote_dic)
    return quote
    