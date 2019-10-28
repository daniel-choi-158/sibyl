# Import necesary libraries
import pandas as pd
import pandas_datareader.data as web
import datetime
import pytz    # $ pip install pytz
import tzlocal  # $ pip install tzlocal

# import functions from subfiles
from subscript1 import *

with open('./dictionary/securities.txt', 'r') as f:
    tickers = f.read().splitlines()
tickers = ["MQG.AX"]
local_timezone = tzlocal.get_localzone()
start = datetime.date.today()-datetime.timedelta(365)
end = datetime.date.today()

get_price_data(tickers, start, end, web, pd)