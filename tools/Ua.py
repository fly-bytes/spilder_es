from fake_useragent import UserAgent

# 随机ua
def ua():
    return {'user-agent': UserAgent().random}
