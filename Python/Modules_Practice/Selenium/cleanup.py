import pickle
stock_et_file = "stock_et_codes.txt"
et_codes = 'et_codes'

class CleanUp():

    def __init__(self):
        pass

    def dump_et_codes(self):
        """
        dump {stock_nse_code : stock_et_code} into pickle
        :return:
        """
        Dict = dict()
        Ofile = open(stock_et_file, 'r+').readlines()
        et_codes = open(et_codes, 'ab')
        for line in Ofile:
            nse_code , et_id = line.split()[:2]
            Dict[nse_code] = et_id
        pickle.dump(Dict, et_codes)

    def test_dump_et_codes(self):
        et_codes = open('et_codes', 'rb')
        Dict = pickle.load(et_codes)
        print(Dict)

if __name__ == "__main__":
    obj = CleanUp()
    obj.test_dump_et_codes()


