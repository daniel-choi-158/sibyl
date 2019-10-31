# =============================================================================
# Import securities data in OHLCD format using Pandas Datareader
# =============================================================================

# Import necesary libraries
import pandas as pd
import pandas_datareader.data as pdr
import datetime

with open('./dictionary/securities.txt', 'r') as f:
    tickers = f.read().splitlines()


stock_cp = pd.DataFrame() # dataframe to store close price of each ticker
attempt = 0 # initializing passthrough variable
successful = [] # initializing list to store tickers whose close price was successfully extracted
while len(tickers) != 0 and attempt <= 5:
    tickers = [j for j in tickers if j not in successful] # removing stocks whose data has been extracted from the ticker list
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i],datetime.date.today()-datetime.timedelta(365),datetime.date.today(),interval='d')
            temp.dropna(inplace = True)
            stock_cp[tickers[i]] = temp["Adj Close"]
            successful.append(tickers[i])       
        except:
            print(tickers[i]," :failed to fetch data...retrying")
            continue
    attempt += 1
    
print(stock_cp)