from Crypto import Random
from Crypto.Cipher import AES
import base64
from hashlib import md5


def pad(content):
    length = 16 - (len(content) % 16)
    return content.encode(encoding='utf-8') + (chr(length) * length).encode(encoding='utf-8')


def unpad(content):
    return content[:-(content[-1] if type(content[-1]) == int else ord(content[-1]))]


def bytes_to_key(data, salt, output=48):
    data = data.encode(encoding='utf-8')
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]


def aes_encrypt(message, passphrase):
    salt = Random.new().read(8)
    key_iv = bytes_to_key(passphrase, salt, 32 + 16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(message)))


def aes_decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32 + 16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))


if __name__ == '__main__':
    key = '4ea5c508a6566e76240543f8feb06fd457777be39549c4016436afda65d2330e'
    data = '{\"copyrightId\":\"6005661DWHS\",\"auditionsFlag\":0,\"type\":1}'
    encrypt_data = aes_encrypt(data, key)
    print(encrypt_data)

    decrypt_data = aes_decrypt(encrypt_data, key)
    print(decrypt_data)
