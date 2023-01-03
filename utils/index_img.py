import re


def index_img():
    import requests
    from lxml import etree
    from pyquery import PyQuery as py

    url = 'https://cn.bing.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    res_text = response.text
    href_list1 = re.findall('href="/(.*?)&amp;', res_text)[0] + '123'
    href_list2 = re.findall('href="/(.*?)123', href_list1)[0]
    return ('https://cn.bing.com/' + href_list2)


