# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# 主程序入口文件
from spider.crawl import download_image
from parse.movie import movies_from_url
from parse.drama import dramas_from_url
from parse.book import books_from_url


# 爬电影的主逻辑
def crawl_movie():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_from_url(url)
        print('top250 movies: ', movies)
        [download_image(m.img_url, "movie_img", m.name.split("/")[0]) for m in movies]


# 爬电视剧的主逻辑
def crawl_drama():
    for i in range(0, 100, 25):
        url = 'https://www.douban.com/doulist/44811565/?start={}'.format(i)
        dramas = dramas_from_url(url)
        print('top250 drams: ', dramas)
        [download_image(d.img_url, "drama_img", d.name) for d in dramas]


# 爬图书的主逻辑
def crawl_book():
    ranking_begin = 1
    for i in range(0, 250, 25):
        # todo 实现中 - 爬图书
        url = 'https://book.douban.com/top250?start={}'.format(i)
        books = books_from_url(url, ranking_begin)
        ranking_begin = ranking_begin + 25
        print('top250 books: ', books)
        [download_image(m.img_url, "book_img", m.name) for m in books]


# 爬音乐的主逻辑
def crawl_music():
    for i in range(0, 250, 25):
        # todo 待完成 - 爬音乐
        pass


def main():
    # crawl_movie()
    # crawl_drama()
    crawl_book()
    # crawl_music()


if __name__ == '__main__':
    main()



