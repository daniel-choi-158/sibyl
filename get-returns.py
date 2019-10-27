"""
def get_symbol_returns_from_yahoo(symbol, start=None, end=None):
    
    Wrapper for pandas.io.data.get_data_yahoo().
    Retrieves prices for symbol from yahoo and computes returns
    based on adjusted closing prices.
    Parameters
    ----------
    symbol : str
        Symbol name to load, e.g. 'SPY'
    start : pandas.Timestamp compatible, optional
        Start date of time period to retrieve
    end : pandas.Timestamp compatible, optional
        End date of time period to retrieve
    Returns
    -------
    pandas.DataFrame
        Returns of symbol in requested period.
    """

# Import necesary libraries
import pandas as pd
import pandas_datareader.data as web
import datetime

symbol = ["MQG.AX","PLS.AX"]
start = datetime.date.today()-datetime.timedelta(365)
end = datetime.date.today()

try:
    px = web.get_data_yahoo(symbol, start=start, end=end)
    rets = px[['Adj Close']].pct_change().dropna()
except Exception as e:
    print(
        'Yahoo Finance read failed: {}, falling back to Google'.format(e),
        UserWarning)
    px = web.get_data_google(symbol, start=start, end=end)
    rets = px[['Close']].pct_change().dropna()

rets.index = rets.index.tz_localize("UTC")
rets.columns = [symbol]

print(px)
#print(rets)
#return rets
print("process complete.")