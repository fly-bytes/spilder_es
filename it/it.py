import random
import time

import requests

it_url = [
    'http://wechatcn.itezhop.com/index/check-in?brand_id=8',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=3',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=1',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=4',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=5',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=6',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=7',
    'http://wechatcn.itezhop.com/index/check-in?brand_id=8'
]

header = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer":'http://wechatcn.itezhop.com/index/check-in?brand_id=8&code=12&state=1212',
    "accept-language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
    "cookie": "it-wechat=uaag8p5kj58l05mhtmnigqj2r6"
}

if __name__ == '__main__':
    r = requests.session()
    # ua = UserAgent()
    for u in it_url:
        print(u)
        s = r.post(u, headers=header)
        print(s.status_code)
        print(s.content, s.status_code, s.json())
        t = random.randint(0, 5)
        print('暂停', t, '秒')
        time.sleep(t)
