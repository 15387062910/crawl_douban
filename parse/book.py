# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/16
from models.book import Book
from pyquery import PyQuery as pq
from spider.crawl import (
    cached_url,
)


'''
爬虫
    1. 裸请求 百度 google
    2. 反爬虫策略
    3. js 频繁上新的页面
'''


def book_from_div(div, rank):
    """
    从一个 div 里面获取到一个图书信息
    :param div: 每个图书的div
    :param rank: 图书的排名
    :return:
    """
    e = pq(div)

    # 小作用域变量用单字符
    m = Book()
    m.name = e('a')[1].text.strip()
    m.score = e('.rating_nums').text()
    m.quote = e('.inq').text()
    m.img_url = e('img').attr('src')
    m.ranking = rank
    m.detail = e('p')[0].text.strip()
    m.save()
    return m


def books_from_url(url, ranking):
    """
    从 url 中下载网页并解析出页面内所有的电影 -> 只会下载一次(通过cached_url实现)
    然后:
        1. 解析 dom
        2. 找到父亲节点
        3. 每个子节点拿一个movie
    """
    page = cached_url(url, "book")
    e = pq(page)
    items = e('.item')
    books = []
    for i in items:
        book = book_from_div(i, ranking)
        ranking = ranking + 1
        books.append(book)
    return books


