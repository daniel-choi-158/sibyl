"""
def get_data(name, start, end):
    data = web.get_data_yahoo(name, start, end)
    del data['Adj Close'] # we don't need Adj Close
    data['Return'] = (data['Close'] - data['Open']) / data['Open']

    return data 
"""

# Import necesary libraries
import pandas as pd
import pandas_datareader.data as web
import datetime

with open('./dictionary/securities.txt', 'r') as f:
    tickers = f.read().splitlines()
start = datetime.date.today()-datetime.timedelta(365)
end = datetime.date.today()

print(tickers)

data = web.get_data_yahoo(tickers, start, end, interval='d')
del data['Adj Close']  # we don't need Adj Close
#data['Return'] = (data['Close'] - data['Open']) / data['Open']  # add 'Return' column
#data['Return'] = (data.Close - data.Open) / data.Open
print(data)