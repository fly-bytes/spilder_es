import csv
import datetime
import json

import requests
import requests as r
from tools.Ua import *
import pandas as pd

headers_1 = {
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
    # s = r.get(code_url, headers=ua())
    s = r.get(code_url, headers=ua())
    s = s.text.replace('var r = ', '').replace(';', '')
    s = json.loads(s)
    s = pd.DataFrame(s, columns=['基金代码', '基金简称', '基金名称', '基金类型', '基金拼音'])
    print(s)
    s.to_csv('jj/所有基金信息-%s.csv' % str(datetime.date.today()), sep=',')
    print(s)


def down_jz(code, name):
    url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=&fundCode=%s&pageIndex=1&pageSize=20000&startDate=&endDate=&_=1615384956811' % code
    s = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        , 'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % code})
    s = s.json()
    d = s['Data']['LSJZList']
    list = []
    for i in d:
        j = {}
        j['基金名称'] = name
        j['净值日期'] = i['FSRQ']
        j['单位净值'] = i['DWJZ']
        j['累计净值'] = i['LJJZ']
        j['日增长率'] = i['JZZZL']
        j['申购状态'] = i['SGZT']
        j['赎回状态'] = i['SHZT']
        j['分红送配'] = i['FHFCBZ']
        list.append(j)

    with open(('jj/%s-%s-基金历史净值信息-%s.csv' % (name, code, str(datetime.date.today()))), 'w', newline='') as f:
        fieldnames = ['基金名称', '净值日期', '单位净值', '累计净值', '日增长率', '申购状态', '赎回状态', '分红送配']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in list:
            writer.writerow(i)
    print('%s 历史净值下载完毕' % name)


# 下载所有基金历史净值
def down_all_code():
    code_url = 'http://fund.eastmoney.com/js/fundcode_search.js'
    s = r.get(code_url, headers=ua())
    s = s.text.replace('var r = ', '').replace(';', '')
    s = json.loads(s)
    for i in s:
        try:
            down_jz(i[0], i[2])
        except Exception:
            print(i[2] , ' 下载失败')
    print('下载完毕！')

if __name__ == '__main__':
    # down_jz('162411', 'asas')
    down_all_code()
