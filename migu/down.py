from urllib import parse

import requests
from tools.AESTools import aes_encrypt
from tools.RSATools import ras_encrypt

# 咪咕加密RSA公钥
pub_key = '''MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8asrfSaoOb4je+DSmKdriQJKWVJ2oDZrs3wi5W67m3LwTB9QVR+cE3XWU21Nx+YBxS0yun8wDcjgQvYt625ZCcgin2ro/eOkNyUOTBIbuj9CvMnhUYiR61lC1f1IGbrSYYimqBVSjpifVufxtx/I3exReZosTByYp4Xwpb1+WAQIDAQAB'''
# 咪咕加密AES公钥
aes_key = '4ea5c508a6566e76240543f8feb06fd457777be39549c4016436afda65d2330e'

data = {
    "dataType": "2",
    # 歌曲信息AES加密
    "data": '{"copyrightId":"60054701897","type":1,"auditionsFlag":0}',
    # RAS加密AES公钥
    "secKey": '4ea5c508a6566e76240543f8feb06fd457777be39549c4016436afda65d2330e'
}

header = {
    "authority": "music.migu.cn",
    "method": "GET",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://music.migu.cn/v3/music/player/audio",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}

info = 'https://music.migu.cn/v3/api/music/audioPlayer/getPlayInfo?dataType=2' \
       '&data=%s' \
       '&secKey=%s'

if __name__ == '__main__':
    info = info % (
        parse.quote(
            aes_encrypt(data.get('data'), data.get('secKey'))),
        parse.quote(
            ras_encrypt(pub_key, data.get('secKey'))
        )
    )
    r = requests.session()
    s = r.get(info, headers=header)
    print(s.status_code)
    print(s.json())
