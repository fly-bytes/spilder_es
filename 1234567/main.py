import datetime
import json

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


if __name__ == '__main__':
    pass
