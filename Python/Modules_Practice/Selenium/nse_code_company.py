from nsetools import Nse
import pickle
nse = Nse()
stocks = nse.get_stock_codes()
print(type(stocks))
dump_file = open('stock_list', 'ab')
pickle.dump(stocks, dump_file)
for code, name in stocks.items():
    print(code , name)
stocks_list_file = open('stock_list', 'rb')
stocks = pickle.load(stocks_list_file)
print(stocks)

