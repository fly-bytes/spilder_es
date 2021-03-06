import requests

from tools.Ua import ua


def get_ips():
    url = 'https://www.kuaidaili.com/free/inha/1/'
    r = requests.get(url, headers=ua())
    print(r.text)
