"""
requests: 请求库 
"""

import requests;

target_url = "https://www.tiobe.com/tiobe-index/"

response = requests.get(target_url);

with open('./tiobe.html', 'w', encoding="utf-8") as f:
    f.write(response.text)

print(response.text)