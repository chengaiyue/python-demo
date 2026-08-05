"""
函数
    global:
        可以允许在函数内部修改全局变量的值

    关键字参数: 可以不用在乎顺序，指定传入的参数是什么
        fun(name: 1, age: 2)

    参数默认值: 必须放在没有默认参数的后面
        fun(age='3')

    不定长参数: 参数会被封装成元组，不会封装关键字参数
        fun(*args)
        关键字传递: 会封装成一个字典类型 
            fun(*args, **kwargs)
    
    匿名函数:
        fun = lambda 参数名: 函数体(不能换行)

    函数注解
        def fun(data: list[str]) -> bool:
            return True;
"""

list1: list[str] = ['1', 2];

print(list1)

add = lambda x,y: x+y

num = 1

def changeNum():
    global num
    num = 2;

changeNum()

print(num)

