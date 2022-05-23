#########
# 实现将cookie添加到网址中
#########
from selenium import webdriver
import json
url='https://gitee.com/'
cookie_save_path='gitee_cookies.txt'

# 填写webdriver的保存目录
#driver = webdriver.Chrome()

# 记得写完整的url 包括http和https
#driver.get(url)

# 首先清除由于浏览器打开已有的cookies
def get_cookies(driver,url):
    driver.get(url)
    driver.delete_all_cookies()

    with open(cookie_save_path,'r') as f:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookies_list = json.load(f)
        # 方法1 将expiry类型变为int
        for cookie in cookies_list:
            # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
    driver.get(url)
    return driver
    # 方法2删除该字段
    # for cookie in cookieslist:
    #     # 该字段有问题所以删除就可以
    #     if 'expiry' in cookie:
    #         del cookie['expiry']
    #     driver.add_cookie(cookie)
