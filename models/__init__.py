# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# Model类
import os
import json
from settings import data_path


# 底层的save:
def save(data, path):
    """
    :param data: 是 dict 或者 list
    :param path: 保存文件的路径
    :return:
    """
    s = json.dumps(data, indent=2, ensure_ascii=False) + ",\n"
    with open(path, 'a+', encoding='utf-8') as f:
        # log('save: ', path, s, data)
        f.write(s)


# 底层的load:
def load(path):
    """
    :param path: 读取文件的路径
    :return:
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        # log('load: ', s)
        return json.loads(s)


class Model(object):
    """
    基类, 用来显示类的信息
    """
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        # print(properties)     # properties是个生成器对象
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s

    @classmethod
    def db_path(cls):
        """
        cls 是类名, 谁调用的类名就是谁的
        classmethod 有一个参数是 class(这里我们用 cls 这个名字)
        所以我们可以得到 class 的名字
        """
        classname = cls.__name__
        path = '{}.txt'.format(classname)
        path = os.path.join(data_path, path).replace('\\', '/')
        return path

    def item_obj(self):
        properties = [{k: v} for k, v in self.__dict__.items()]

        return properties

    def save(self):
        """
        用 all 方法读取文件中的所有 model 并生成一个 list
        把 self 添加进去并且保存进文件
        """
        path = self.db_path()
        save(self.item_obj(), path)

