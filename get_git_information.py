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
from collections import Iterable
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
    content = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div/div[3]/div/div')
    result=content.text
    print(result)
    sleep(2)
    browser.close()
    with open(commit_save_path, 'w',encoding="utf-8") as f:
        # 将cookies保存为json格式
        f.write(result)
    return result
def info_process():
    with open(commit_save_path,'r',encoding="utf-8") as f:
        commit_info1 = f.read()
    commit_info = commit_info1.split('\n')
    print(isinstance(commit_info1,Iterable))
    commit_info = iter(commit_info)
    information=[]
    record={
        'time': '',
        'project': '',
        'name':'',
        'detail':''
    }
    for list in commit_info:
        if len(list)==2 or len(list)==3:
            record['name'] = list
            record['time'] =
            record['project'] =
            record['detail'] =

info_process()
# if __name__ == "__main__":
#     browser = browser_launch(url)
#     info_process(get_information(browser,url))