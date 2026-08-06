"""
lxml: 解析html文档
"""

from lxml import html;

with open('./tiobe.html', 'r', encoding="utf-8") as f:
    htmlText = f.read();

    document = html.fromstring(htmlText);

    th_list = document.xpath("//thead/tr/th/text()")

    tr_list = document.xpath("//tbody/tr")

    for tr in tr_list:
        td_list = tr.xpath('./td/text()')
        print(td_list)