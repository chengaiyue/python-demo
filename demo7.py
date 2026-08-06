"""
json数据
    dump: 序列化，可以写入文件
    load: 反序列化，从文件中读取json 
"""

import json

with open('./demo6.txt', 'w', encoding="utf-8") as f:
    json.dump({"name": "zcc"}, f, ensure_ascii=False, indent=2)


with open('./demo6.txt', 'r', encoding="utf-8") as f:
    content = json.load(f)
    print(content)
    print(type(content))