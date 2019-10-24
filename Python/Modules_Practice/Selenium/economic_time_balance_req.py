import requests
import os
from lxml import html
import pickle


balance_sheet_url = 'https://economictimes.indiatimes.com/hdfc-bank-ltd/balancesheet/companyid-{}.cms'
balance_sheet_output_file = os.path.join(os.path.dirname(__file__), 'balance_sheet_data.txt')


bank_nifty = {  #'yes_bank' :'16552',
                # 'icici_bank' :'9194',
                'federal_bank' :'9211',
                'pnb_bank' :'11585',
                'rbl_bank' :'7750',
                'idfc_bank' :'62245',
                'bob_bank' : '12040',
                'kotak_bank' : '12161',
                'hdfc_bank' : '9195',
                'axis_bank' : '9175',
                'sbin' : '11984',
                'indusind' : '9196'}
et_codes = open('et_codes', 'rb')
codes = pickle.load(et_codes)
# print(codes)
output_file = open(balance_sheet_output_file, 'a')

for bank, code in codes.items():
    url = balance_sheet_url.format(code)
    response = requests.get(url)
    tree = html.fromstring(response.text)
    try :
        Data = tree.xpath('//td/text()')
        NetWorth = Data.index('Net Worth');  # print (NetWorth)
        SecuredLoan = Data.index('Secured Loan');
        TotalYears = SecuredLoan - NetWorth
        TotalLiabilities = Data.index('TOTAL LIABILITIES');  # print (TotalLiabilities)
        TotalCurrentAssests = Data.index('Total Current Assets');  # print (TotalCurrentAssests)
        TotalCurrentLiabilities = Data.index('Total Current Liabilities');  # print (TotalCurrentLiabilities)
        NETCURRENTASSETS = Data.index('NET CURRENT ASSETS');  # print (NETCURRENTASSETS)
        TOTALASSETS = Data.index('TOTAL ASSETS(A+B+C+D+E)');  # print (TOTALASSETS)
    except Exception as err:
        print(err)
        continue
    years = ['2019-04-01', '2018-04-01', '2017-04-01', '2016-04-01', '2015-04-01', ]

    detail_list = []
    try :
        for j in range(1, len(years) + 1):
            detail = {
                'year': years[j - 1],
                'stock_name': bank,
                # 'code':self.company_ids[self.i],
                'net_worth': Data[NetWorth + j],
                'total_liabilities': Data[TotalLiabilities + j],
                'total_current_assests': Data[TotalCurrentAssests + j],
                'net_current_assets': Data[NETCURRENTASSETS + j],
                'total_assets': Data[TOTALASSETS + j]
            }
            detail_list.append(detail)
    except Exception as err:
        print("------------->",bank, err)
    output_file.write(str(detail_list))
    output_file.write('\n')

    print(detail_list)
