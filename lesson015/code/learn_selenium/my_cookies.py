# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 21:36
# @Author  : zdRan
# @FileName: my_cookies.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
import json
import time
import os
from selenium import webdriver

driver = webdriver.Chrome(r"D:\SDK\python_env\chromedriver.exe")


def login():
    driver.get("https://www.jd.com")
    driver.maximize_window()
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_partial_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("461163677@qq.com")
    driver.find_element_by_id("nloginpwd").send_keys("zdR930116")
    driver.find_element_by_id("loginsubmit").click()

    save_cookies()


def save_cookies():
    project_path = os.path.dirname(os.getcwd())
    save_cookies_path = project_path + "/cookeis/"
    if not os.path.exists(save_cookies_path):
        os.mkdir(save_cookies_path)

    cookies = driver.get_cookie()
    with open(save_cookies_path + "jd.cookies", "w")as cookies_file:
        json.dump(cookies, cookies_file)

    print(cookies)


def get_order_list():
    project_path = os.path.dirname(os.getcwd())
    save_cookies_path = project_path + "/cookeis/"
    cookies_file = save_cookies_path + "jd.cookies"

    jd_cookies = open(cookies_file, "r")

    cookies_str = jd_cookies.readline()
    cookies_dict = json.load(cookies_str)

    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    for cookie in cookies_dict:
        driver.add_cookie(cookie)

    driver.get("https://order.jd.com/center/list.action")

if __name__ == "__main__":
    login()
