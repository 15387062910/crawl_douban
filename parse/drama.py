# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# HTMLParser 解析页面
from models.drama import Drama
from pyquery import PyQuery as pq
from spider.crawl import (
    cached_url,
    download_image,
)


'''
爬虫
    1. 裸请求 百度 google
    2. 反爬虫策略
    3. js 频繁上新的页面
'''


def drama_from_div(div):
    """
    从一个 div 里面获取到一个电影信息
    """
    e = pq(div)

    # 小作用域变量用单字符
    m = Drama()
    m.name = e('.title').text()
    m.score = e('.rating').find('.rating_nums').text()
    m.img_url = e('img').attr('src')
    m.ranking = e('.hd').find('.pos').text()
    m.details = e('.abstract').text()
    m.save()
    return m


def drama_from_url(url):
    """
    从 url 中下载网页并解析出页面内所有的电视剧 -> 只会下载一次(通过cached_url实现)
    然后:
        1. 解析 dom
        2. 找到父亲节点
        3. 每个子节点拿一个drama
    """
    page = cached_url(url, "drama")
    e = pq(page)
    items = e('.doulist-item')
    movies = [drama_from_div(i) for i in items]
    return movies
