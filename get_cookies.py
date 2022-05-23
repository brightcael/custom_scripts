#########
# 将cookie写入文件
#########
from selenium import webdriver
import time
import json

url='https://gitee.com/'
cookie_save_path='gitee_cookies.txt'

# 填写webdriver的保存目录
driver = webdriver.Chrome()
# 记得写完整的url 包括http和https
driver.get(url)

# 程序打开网页后20秒内 “手动登陆账户”
time.sleep(60)

with open(cookie_save_path,'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))
driver.close()