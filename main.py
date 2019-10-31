# Import necesary libraries
import pandas as pd
import pandas_datareader.data as web
import datetime
import pytz    # $ pip install pytz
import tzlocal  # $ pip install tzlocal

# import functions from subfiles
from live_prices import *
from historical_prices import *

with open('./dictionary/securities.txt', 'r') as f:
    tickers = f.read().splitlines()
tickers = ["MQG.AX"]
local_timezone = tzlocal.get_localzone()
start = datetime.date.today()-datetime.timedelta(365)
end = datetime.date.today()

# test live data
#for x in tickers:
#    get_live_data(x, start, end, web, pd)

# test historical data
for x in tickers:
    get_historical_data(x, start, end, web, pd)

