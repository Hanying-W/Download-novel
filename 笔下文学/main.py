# -*- coding: utf-8 -*
import random
import requests
import time
import sys


# 获得小说目录
def get_url(book):
    # 获取小说目录
    url = 'https://www.bxwxorg.com/read/' + str(book) + '/'
    # 获得网页代码
    html = requests.get(url)
    # 转换格式
    contents = html.text
    # 获取章节位置
    a = contents.find('<dl>')
    b = contents.find('</dl>')
    contents = contents[a:b]
    # 跳过最前面的更新列表
    for i in range(0, 4):
        a = contents.find('dt')
        contents = contents[a + 3:]
    # 读取章节链接
    while True:
        # 获取该章节名和链接
        a = contents.find('<dd>') + 4
        # 如果没找到就会返回-1，再加上往后移的位数
        if a == 3:
            break
        # 获取链接的结束坐标
        b = contents.find('</dd>')
        # 存放章节名和链接
        s = contents[a:b]
        c = s.find('">')
        # 提取链接
        url = 'https://www.bxwxorg.com' + s[9:c]
        print(url)
        # 提取小说正文
        get_Fiction(url, book)
        # 输出提示性信息
        print(s[c + 2:-4] + ' 下载成功')
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
    # 处理小说格式
    s = s.replace('<p>', '')
    s = s.replace('</p>', '')
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
        'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, '
                  '* / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
        'accept - encoding': 'gzip, deflate, br',
        'accept - language': 'zh - CN, zh;q = 0.9, en;q = 0.8, zh - TW;q = 0.7, en - US;q = 0.6, zh - HK;q = 0.5',
        'cache - control': 'no - cache',
        'cookie': '__cfduid = d703d24f256e484721c270ef033417d3b1584693348;Hm_lvt_46329db612a10d9ae3a668a40c152e0e = '
                  '1584693357, 1584693376;Hm_lpvt_46329db612a10d9ae3a668a40c152e0e = 1584693376',
        'dnt': 1,
        'pragma': 'no - cache',
        'referer': 'https://www.bxwxorg.com/',
        'sec - fetch - dest': 'document',
        'sec - fetch - mode': 'navigate',
        'sec - fetch - site': 'same - origin',
        'sec - fetch - user': '?1',
        'upgrade - insecure - requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.' + o + '.' + t + 'Safari/537.36 chrome-extension '
    }
    html = requests.get(url, params=req_header)
    file = open('log.txt', 'w+')
    file.write(url)
    file.write(' ')
    file.write(str(html))
    file.write('\n')
    file.close()
    return html.text


book_number = input("请输入小说的编号：")
get_url(book_number)
