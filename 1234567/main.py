import datetime
import json

import requests
import requests as r
from tools.Ua import *
import pandas as pd

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "api.fund.eastmoney.com",
    "Referer": "http://fundf10.eastmoney.com/"
}


# 所有基金信息
def down_jj_code():
    code_url = 'http://fund.eastmoney.com/js/fundcode_search.js'
    s = r.get(code_url, headers=ua())
    s = s.text.replace('var r = ', '').replace(';', '')
    s = json.loads(s)
    s = pd.DataFrame(s, columns=['基金代码', '基金简称', '基金名称', '基金类型', '基金拼音'])
    print(s)
    s.to_csv('jj/所有基金信息-%s.csv' % str(datetime.date.today()), sep=',')
    print(s)


def down_jz(code):
    url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=&fundCode=%s&pageIndex=1&pageSize=20000&startDate=&endDate=&_=1615384956811' % code
    s = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        , 'Referer': 'http://fundf10.eastmoney.com/'})

    s = s.json()
    s = pd.DataFrame.from_dict(s['Data']['LSJZList'])
    s.to_csv('jj/%s-基金净值信息-%s.csv' % (code, str(datetime.date.today())), sep=',')
    print('down load success')


if __name__ == '__main__':
    down_jz('000001')
