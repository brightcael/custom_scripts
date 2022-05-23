##########
# 从gitee中获取代码提交信息
##########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
import add_cookies
##########
url='https://e.gitee.com/emnets/projects/218248/overview'
commit_save_path = 'commit_info.txt'
##########
def browser_launch(Url):
    ###启动参数
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    ###启动
    browser = webdriver.Chrome(chrome_options=options)
    return browser
def get_information(browser,Url):
    ####
    browser = add_cookies.get_cookies(browser,Url)
    ####
    sleep(2)
    ####
    button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[6]')
    button.click()
    sleep(3)
    content = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div/div[3]/table/tbody')

    result=content.text
    print(result)
    result = result.split('\n')
    i=0
    for list in result:
        if list[0]>'A' and list[0]<'z':
            print(list)
        i=i+1

    sleep(10)
    browser.close()

if __name__ == "__main__":
    browser = browser_launch(url)
    get_information(browser,url)