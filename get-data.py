import pandas_datareader.data as pdr
import datetime as dt
import logging

ticker = "AMZN"
start_date = dt.date.today() - dt.timedelta(365);
end_date = dt.date.today();

data = pdr.get_data_yahoo(ticker, start_date, end_date, interval="d");

print(data);
print('run complete.');