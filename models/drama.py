# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
from . import Model


class Drama(Model):
    """
    存储电视剧信息
    """
    def __init__(self):
        """
        name -> 名字
        score -> 分数
        img_url -> 路径
        ranking -> 排名
        details -> 详细信息
        """
        self.name = ''
        self.score = 0
        self.img_url = ''
        self.ranking = 0
        self.details = ''