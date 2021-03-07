import datetime
import os
import time
from turtle import pd

import tushare as ts
from sqlalchemy import create_engine
from tushare import util

ts.set_token('336c13b4bea04e188b0f9d1ae3f68dfd38d9d1ee7f0c489f94a4b7c8')


# 下载A股股票代码
def download_stock_basic_info():
    data = stock_code()
    data.to_sql('stock_code1', con=create_engine('mysql+pymysql://root:123456@localhost:3306/abc?charset=utf8'),
                schema='abc', index=False, if_exists='append', chunksize=5000)


def stock_code():
    pro = ts.pro_api()
    # 查询当前所有正常上市交易的股票列表
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date,is_hs')
    print('加载A股所有股票代码...')
    print(data)
    return data

def down():
    # 股票代码
    codes = stock_code()
    i = 0
    sum = 0
    while i < len(codes.ts_code):
        code = codes.ts_code[i]
        date = codes.list_date[i]
        print('加载', code, date, '以来后复权数据')
        # 后复权
        df = ts.pro_bar(ts_code=code, adj='hfq', start_date=str(date), end_date='20210305')
        print(df)
        sum = sum + len(df)
        time.sleep(0.3)
        df.to_sql('stock_date', con=create_engine('mysql+pymysql://root:123456@localhost:3306/abc?charset=utf8'),
                  schema='abc', index=False, if_exists='append', chunksize=5000)
        i = i + 1
    print('下载完毕,共下载', sum, '条数据')


# 爬取A股股票代码的后复权数据到MySql
if __name__ == '__main__':
    download_stock_basic_info()
    pass
