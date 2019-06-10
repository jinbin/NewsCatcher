#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

res = requests.get("http://pi.zju.edu.cn/index.php?c=Index&a=news_list&catid=166")

try:
    soup = BeautifulSoup(res.text, "html.parser")
except:
    print("Parse Fail")

# chrome 使用copy selector
path = "body > div > div.content > div > div > div.list-right > div.list-right-news > div.list-con > ul > li:nth-child(1) > a"
#path = "body > div > div.content > div > div > div.list-right > div.list-right-news > div.list-con > ul"
result = soup.select(path)

for val in result:
    if val.get_text().strip() == "中法创新创业管理双硕士项目2019年招生面试通知":
        print("No new information")
        #os.system("osascript -e 'display notification \"没有关于中法新的通知\" with title \"一切正常\"'")
    else:
        print("New information!")
        print("New information：" + val.get_text())
        os.system("osascript -e 'display notification \"有关于中法新的通知\" with title \"新的通知\"'")









