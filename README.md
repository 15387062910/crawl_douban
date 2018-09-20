# crawl_douban

### 项目目的:    爬取豆瓣的top250系列中的电影、图书、电视剧、音乐的数据

### 项目基本原理
    请求库: requests
    解析库: pyquery

    破解反爬虫: 加user-agent和cookie
        
    项目逻辑结构如下:
    1. crawl: Downloader 下载页面 or 图片  requests  -> 缓存处理(已经下载的不再下载)
    2. parse: HTMLParser 解析页面          pyquery     lxml   (注: pyquery的用法类似前端中的CSS选择器)
    3. model: DataModel 字段 - element     业务逻辑 (自己做一个model)

### 爬取页面地址
* top250电影:     https://movie.douban.com/top250
* top250图书:     https://book.douban.com/top250
* top250电视剧:   https://www.douban.com/doulist/44811565/ 
* top250音乐:     https://music.douban.com/top250

### 项目目录说明
* cached 缓存页面
* data 存储爬取的数据
* img 存储图片
* models 数据模型及存储数据
* parse 解析页面
* spider 下载页面及图片
* run.py 项目入口程序 整个项目由此启动
* README.md 项目说明文件
* settings.py 配置文件

### 其他说明
    关于top250电视剧: 
        top250电视剧不是官方榜单，并且其中只有93部电视剧
    安装包:
        安装pyquery: pip3 install pyquery
        安装requests: pip3 install requests
    运行:
        直接运行项目根目录下的run.py即可