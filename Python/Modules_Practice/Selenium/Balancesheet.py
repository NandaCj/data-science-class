import requests
import re
from et_urls import home_page
# url = "https://economictimes.indiatimes.com/hdfc-bank-ltd/balancesheet/companyid-{}.cms"
url = home_page
file = open('stock_et_codes.txt', 'r')
sec_file = open('stock_et_sector.txt', 'w+')
fund_details = open('fund_details.txt', 'w+')
regex_map = {
    'mkt_cap' : 'nse_tab mkt_cap tar',
    'p_e' : 'nse_tab p_e tar',
    'p_b':'nse_tab p_b tar',
    'div' : 'nse_tab div_yield tar',
    'f_v' :'face_value tar',
    'eps' : 'eps_ttm tar',
    'bv_sh' : 'bv_sh tar',


}

values_map = {
    'mkt_cap' : '{}',
    'p_e' : '{}',
    'p_b' :{},
    'div' : '{}',
    'f_v' :'{}',
    'eps' : '{}',
    'bv_sh' : '{}',
}
for line in file.readlines():
    stock = line.split()[0]
    code = line.split()[1]
    n_url = url.format(code)
    print(n_url)
    res = requests.get(n_url).text
    # print(res)
    for key, regex in regex_map.items():
        try:
            reg = r'{}">(.*?)</span>'.format(regex)
            # print(reg)
            value = re.findall(reg , res)[0]
            # print(value)
            if value != '':
                values_map[key] = value
            else:
                values_map[key] = 'NAN'
        except:
            values_map[key] = 'NAN'
    print(str(stock) + "::" + str(code) + "::" + values_map['mkt_cap'] + "::" +
          values_map['p_e'] + "::"+
          values_map['p_b'] + "::" +
          values_map['div'] + "::"+
        values_map['f_v'] + "::"+
          values_map['eps'] + "::" +
    values_map['bv_sh'] )
    fund_details.write(str(stock) + "::" + str(code) + "::" + values_map['mkt_cap'] + "::" +
          values_map['p_e'] + "::"+
           values_map['p_b'] + "::" +
          values_map['div'] + "::"+
        values_map['f_v'] + "::"+
          values_map['eps'] + "::" +
    values_map['bv_sh'] + '/n')




def get_ind_sec(res):
    txt = re.findall(r'IND:</b>(.*)ISIN', res)[0]
    IND = re.findall(r'^(.*)&nbsp.?\; \| \&' ,str(txt))[0]
    SEC = re.findall(r'<b>SECT:</b>(.*?)</span>', res)[0]
    print(str(stock) + "::" + str(code) + "::" +str(IND) + "::" +str(SEC))
    sec_file.write(str(stock) + "::" + str(code) + "::" +str(IND)+ "::" +str(SEC) + "\n")