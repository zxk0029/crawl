import requests


def aa():
    proxy = {'https': "https://95121.13.218.231:117"}
    # 用百度检测ip代理是否成功
    url = 'https://www.baidu.com/s?'
    # 请求网页传的参数
    params = {
        'wd': 'ip地址'
    }
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    # 发送get请求
    response = requests.get(url=url, headers=headers, params=params, proxies=proxy,  verify=False)
    # 获取返回页面保存到本地，便于查看
    with open('ip.html', 'w', encoding='utf-8') as f:
        f.write(response.text)


def qq():
    proxy = {'https': 'https://221.229.173.129:2867'}

    url = 'https://httpbin.org/get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    # 发送get请求
    response = requests.get(url=url, headers=headers, proxies=proxy, verify=False)
    print(response.text)


qq()

