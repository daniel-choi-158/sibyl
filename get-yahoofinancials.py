# =============================================================================
# use to access a wide variety of data from Yahoo Finance
# return the data in JSON format.
# =============================================================================

from yahoofinancials import YahooFinancials
import datetime


with open('./dictionary/securities.txt', 'r') as f:
    tickers = f.read().splitlines()

print(tickers)

yahoo_financials = YahooFinancials(tickers)
from_date = (datetime.date.today()-datetime.timedelta(365)).strftime('%Y-%m-%d')
to_date = datetime.date.today().strftime('%Y-%m-%d')

#balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
#income_statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
#all_statement_data_qt =  yahoo_financials.get_financial_stmts('quarterly', ['income', 'cash', 'balance'])
#earnings_data = yahoo_financials.get_stock_earnings_data()
net_income = yahoo_financials.get_net_income()
#historical_stock_prices = yahoo_financials.get_historical_price_data(from_date, to_date, 'daily')
print("process complete.")