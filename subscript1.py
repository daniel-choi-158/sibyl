def get_price_data(name, start, end, web, pd):
    data = web.get_data_yahoo(name, start, end, interval='d')
    del data['Adj Close'] # we don't need Adj Close
    data['Return'] = (data['Close'] - data['Open']) / data['Open']
    data.index = data.index + pd.DateOffset(1)
    print(data)
    return data