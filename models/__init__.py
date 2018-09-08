# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# Model类
import json


# 底层的save:
def save(data, path):
    """
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        # log('save: ', path, s, data)
        f.write(s)


# 底层的load:
def load(path):
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
        path = 'data/{}.txt'.format(classname)
        return path

