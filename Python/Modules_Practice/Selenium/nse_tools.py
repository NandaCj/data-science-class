from nsetools import Nse
import pickle

class nse_tools_helpers:
    dump_file = 'stocks_list'

    def dump_nse_stocks_list(self):
        """
        Dump the list of nse stocks to a pickle file
        :return:
        """
        nse = Nse()
        dump_file = open(__class__.dump_file, 'ab')
        stocks = nse.get_stock_codes()
        del stocks['SYMBOL'] # removing unwanted key
        pickle.dump(stocks, dump_file)
        dump_file.close()

    def load_nse_stocks_list(self):
        """
        load the nse stocks dict from pickle file
        :return:
        """
        dump_file = open(__class__.dump_file, 'rb')
        stocks = pickle.load(dump_file)
        dump_file.close()
        return stocks

if __name__ == "__main__":
    obj = nse_tools_helpers()
    # obj.dump_nse_stocks_list()
    # print(obj.load_nse_stocks_list())




