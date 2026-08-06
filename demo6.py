"""
文件操作
"""

f = open('./demo6.txt', 'r', encoding="utf-8")
content = f.read()
print(content)
f.close()
f = open('./demo6.txt', 'w', encoding="utf-8")
f.write('zcc')
f.close()
with open('./demo6.txt', 'r', encoding="utf-8") as f:
    pass