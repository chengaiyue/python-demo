"""
类:
    class 类名:
        def __init__(self, 参数列表)

        // 定义方法
        def method(self): 
            pass

    __dict__ 实例对象的特殊属性, 用来记录实例对象上的属性

    魔法方法: 以下划线开始和下划线结束的方法, 类似__init__, 用于定义类的特殊行为, 不需要手动调用, python会在合适时机自动调用
        __init__
        __str__
        __eq__
        __lt__
        __le__
        __gt__
        __ge__
"""

class Person:
    pass

zhang = Person()

zhang.name = 'zcc'
zhang.age = 32

print(zhang.__dict__)