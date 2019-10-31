def get_live_data(name, start, end, web, pd):
    idx = pd.IndexSlice
    data = web.get_data_yahoo(name, start, end, interval='d')
    del data['Adj Close']  # we don't need Adj Close
    # df_temp = data.loc[:, idx['Volume']].rename(columns={'Volume':'adjustedVolume'}) * 3
    # print(df_temp)
    # print(pd.concat([data, df_temp], axis=1))
    # data_final = pd.concat([data,df_temp], axis=1)
    
    data['Return'] = (data['Close'] - data['Open']) / data['Open']
    data.index = data.index + pd.DateOffset(1)
    print(data)
    return data
    # return data_final