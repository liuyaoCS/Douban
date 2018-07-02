import requests

'''代理IP地址（高匿）'''
proxy = {
    'http': 'http://187.12.44.34:8080',
    'https': 'https://187.12.44.34:8080'
}
'''head 信息'''
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}
'''http://icanhazip.com会返回当前的IP地址'''

p = requests.get('https://book.douban.com/top250?start=0', headers=head, proxies=proxy)
print(p.text)