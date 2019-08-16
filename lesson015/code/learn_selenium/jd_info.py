# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 22:37
# @Author  : zdRan
# @FileName: jd_info.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
import json
import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"D:\SDK\python_env\chromedriver.exe")


def to_goods_page(driver):
    driver.get("https://www.jd.com")
    computer_element = driver.find_element_by_link_text("电脑")
    # 鼠标悬停
    ActionChains(driver).move_to_element(computer_element).perform()
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    handles = driver.window_handles

    index_hendle = driver.current_window_handle
    for h in handles:
        if index_hendle != h:
            driver.switch_to_window(h)

    driver.find_element_by_xpath('//*[@id="brand-11518"]/a/img').click()
    driver.find_element_by_xpath('//*[@id="plist"]/ul/li[1]/div/div[1]/a/img').click()
    # 切换句柄
    handles = driver.window_handles

    notebook_handle = driver.current_window_handle
    for h in handles:
        if index_hendle != h & notebook_handle != h:
            driver.switch_to_window(h)


if __name__ == "__main__":
    to_goods_page(driver)
