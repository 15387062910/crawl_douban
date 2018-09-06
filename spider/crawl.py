# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# Downloader 下载页面 or 图片
import requests
import os


def download_image(url, floder_name, img_name):
    """
    下载图片
    :param url: 图片路径    floder_name: 图片存在img下的文件夹的名字
    :return:
    """
    folder = "img"
    folder_path = os.path.join(folder, floder_name)
    img_name = img_name + ".jpg"
    img_path = os.path.join(folder, floder_name, img_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if os.path.exists(img_path):
        return

    headers = {
        'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
    }
    # 如果url不为None发送网络请求, 把结果写入到文件夹中
    if url:
        r = requests.get(url, headers)
        with open(img_path, 'wb') as f:
            f.write(r.content)


def cached_url(url, name):
    """
    缓存, 避免重复下载网页浪费时间
    :param url: 页面链接 eg: https://movie.douban.com/top250?start=0
    :param name: cached下的每一个子文件夹的名字 eg: movie、drama
    :return:
    """
    cached_path = "cached"
    # 存具体缓存页面的文件夹名、文件名、存储路径
    folder_name = name + '_cached'
    filename = url.split('=', 1)[-1] + '.html'
    path = os.path.join(cached_path, folder_name, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        # 建立 cached 文件夹
        folder_path = os.path.join(cached_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
        }
        # 发送网络请求, 把结果写入到文件夹中
        r = requests.get(url, headers)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content
