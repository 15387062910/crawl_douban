# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# 主程序入口文件
from spider.crawl import download_image
from parse.movie import movies_from_url
from parse.drama import drama_from_url


def crawl_movie():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_from_url(url)
        print('top250 movies: ', movies)
        [download_image(m.cover_url, "movie_img", m.name.split("/")[0]) for m in movies]


def crawl_drama():
    for i in range(0, 100, 25):
        url = 'https://www.douban.com/doulist/44811565/?start={}'.format(i)
        dramas = drama_from_url(url)
        print('top250 drams: ', dramas)
        [download_image(d.cover_url, "drama_img", d.name) for d in dramas]


def main():
    # crawl_movie()
    crawl_drama()


if __name__ == '__main__':
    main()



