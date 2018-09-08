# douban

### 项目目的:    爬取豆瓣的top250系列 电影、图书、电视剧

### 项目基本原理
    请求库: requests
    解析库: pyquery

    破解反爬虫: 加user-agent和cookie
        
    项目逻辑结构如下:
    1. crawl: Downloader 下载页面 or 图片          requests
    2. parse: HTMLParser 解析页面          pyquery     lxml   (注: pyquery的用法类似前端中的CSS选择器)
    3. model: DataModel 字段 - element     业务逻辑 (自己做一个model)


### 项目目录说明
* cached 缓存页面
* data 存储爬取的数据
* img 存储图片
* models 数据模型
* parse 解析页面
* spider 下载页面 or 下载图片
* main.py 项目入口程序
* README.md 项目说明文件
* settings.py 设置文件

