# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/6
# Model类


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