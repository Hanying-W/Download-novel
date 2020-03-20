# -*- coding: utf-8 -*
import random
import requests
import time
import sys


# 获得小说目录
def get_url(book):
    # 获取小说目录
    url = 'https://www.biquge.com.cn/book/' + str(book) + '/'
    # 获得网页代码
    html = requests.get(url)
    # 转换格式
    contents = html.text
    # 获取小说名字
    a = contents.find('<dt>') + 4
    b = contents.find('</dt>')
    name = book
    contents = contents[b:]
    # 读取章节链接
    while True:
        # 获取链接的开始坐标
        a = contents.find('<dd>') + 13
        # 如果没找到就会返回-1，再加上往后移的位数
        if a == 12:
            break
        # 获取链接的结束坐标
        b = contents.find('</a')
        s = contents[a:b]
        # 提取链接
        url = 'https://www.biquge.com.cn' + s[:s.find('html') + 4]
        # 提取小说正文
        get_Fiction(url, name)
        # 输出提示性信息
        print(s[s.find('html') + 8:] + ' 下载成功')
        contents = contents[b + 4:]


# 获取小说正文
def get_Fiction(url: str, name: str):
    # 打开存放小说的文件
    file_fiction = open(name + '.txt', 'a+', encoding='utf-8')
    # 获取含有小说的网页
    t = get_Request(url)
    # 提取小说的章节名
    s = t[t.find('<h1>') + 4:t.find('</h1>')]
    file_fiction.writelines(s)
    file_fiction.writelines('\n')
    # 提取小说正文
    a = t.find('<div id="content">') + 18
    t = t[a:]
    b = t.find('</div>')
    s = t[:b]
    s = s.replace('<br>', '\n')
    s = s.replace('&nbsp;', '')
    s = s.replace('<br />', '\n')
    # 存放读入小说
    file_fiction.write(s)
    file_fiction.write('\n')
    file_fiction.close()


# 获取正文网页
def get_Request(url):
    o = str(random.randint(3000, 4000))
    t = str(random.randint(100, 200))
    o = '3987'
    t = '132'
    req_header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6,zh-HK;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=1707cf4b66f95f-0154c401d9bdfb-b383f66-1fa400-1707cf4b670a6f; ' \
                  'bcolor=; ' \
                  'font=; ' \
                  'size=; ' \
                  'fontcolor=; ' \
                  'width=; ' \
                  'CNZZDATA1264388021=1970049713-1582642024-https%253A%252F%252Fwww.google.com%252F%7C1584250571; ' \
                  'Hm_lvt_79146f7516f35fe12fd594789a89d25d=1582644399,1584251346; ' \
                  'hitme=1; hitbookid=32221; Hm_lpvt_79146f7516f35fe12fd594789a89d25d=1584251399',
        'DNT': 1,
        'Host': 'www.biquge.com.cn',
        'Referer': 'https://www.biquge.com.cn/book/32101/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.' + o + '.' + t + 'Safari/537.36 chrome-extension '
    }
    html = requests.get(url, params=req_header)
    file = open('log.txt', 'a+')
    file.write(url)
    file.write(' ')
    file.write(str(html))
    file.write('\n')
    file.close()
    return html.text


book_number = input("请输入小说的编号：")
get_url(book_number)
