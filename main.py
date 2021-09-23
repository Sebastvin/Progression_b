import requests


#A8NNGHYPH9FAV2HO
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey' \
      '=A8NNGHYPH9FAV2HO'
r = requests.get(url)
data = r.json()

print(data)