import investpy

df = investpy.get_stock_historical_data(stock='blue', country='United States', from_date='01/02/2021', to_date='23/02/2021')


crypto = investpy.get_crypto_historical_data('ethereum', from_date='28/01/2021', to_date='23/02/2021')



test = investpy.get_stock_financial_summary(stock='aapl', country='United States', summary_type='income_statement', period='annual')

print(test.head())