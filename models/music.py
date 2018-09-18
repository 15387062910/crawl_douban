# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/18
from . import Model


class Music(Model):
    """
    存储音乐信息
    """
    def __init__(self):
        """
        name -> 名字
        score -> 分数
        img_url -> 路径
        ranking -> 排名
        detail -> 其他详情
        """
        self.name = ''
        self.score = 0
        self.img_url = ''
        self.ranking = 0
        self.detail = ''


