"""
python数据类型
    int
    float
    str
    bool
    NoneType
    list
    tuple
    dict
    set
"""

"""
列表list:
    append: 向最后一位追加
    insert(index, item): 向指定索引之前追加元素
    remove: 删除匹配到的第一个元素
    pop: 删除指定索引的的元素, 不写就删除最后一个
    sort: 排序
    reverse: 反转数组 

    item in list: 判断元素在列表中
    item not in list: 判断元素不在列表中
    

    *list: 解包, 将list元素一个个取出来
    list + list: 组包, 可以直接讲两个列表合并 

    range(num): 生成指定长度的列表

    [i**2 for i in range(1, 21) if i % 2 == 0]: 推导式（按照规则快速生成列表）

    min()
    max()
    sum()
    len()
"""

"""
字符串str:
    find(item): 查找自定字符串第一次出现的索引
    count(item): 统计指定字符串出现的次数
    upper: 转大写
    lower: 转小写
    split: 按照指定分隔符切成list
    strip('*): 去除两端的空白字符或指定字符
    replace('', ''): 将指定字符串替换成其他内容
    startswith: 以什么字符开头

    in: 判断指定的字符是否存在字符串中 
"""

"""
元组tuple: 一旦定义就不可修改
    count: 某个元素在元组中的个数 
    index: 查找某个元素第一次出现的索引

    组包: t1 = (1, 2, 3, 4)
    基础解包: a b c d = t1, 数量要保持一致
    扩展解包: x *y z = t1, y为剩余元素的list
"""

"""
集合set: 自动去重, 不可以存储重复数据, 是无序的, 不可以通过下标来获取数据
    定义: s1 = {1,2,3,4,5} 
          s2=set() 定义空集合

    add
    remove
    pop: 随机删除一个并返回
    clear

    in
    not in

    difference(-): 两个集合的差集
        s1.difference(s2): 包含在第一个, 不包含在第二个
    union(|): 两个集合的并集
    intersection(&): 两个集合的交集

    也支持集合式推导{ 需要添加的元素 for s in s1 if 条件语句 }
"""

"""
字典dict:
    pop: 删除指定key并返回value
    del

    keys()
    values()
    items()
"""

t1 = 1, 2, 3, 4;

x, *y, z = t1;

print(y, type(y))
