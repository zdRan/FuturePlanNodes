# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 22:17
# @Author  : zdRan
# @FileName: js_location.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
import json
import time
import os
from selenium import webdriver

driver = webdriver.Chrome(r"D:\SDK\python_env\chromedriver.exe")


def search_12306():
    driver.get("https://www.12306.cn/index/")
    from_element = driver.find_element_by_id("fromStationText")
    time.sleep(5)
    from_element.click()
    time.sleep(2)
    from_element.send_keys("北京")
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='北京北']").click()

    to_element = driver.find_element_by_id("toStationText")
    time.sleep(2)
    to_element.click()
    to_element.send_keys("上海")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='citem_0']").click()
    time.sleep(2)
    # 时间控件 train_date
    js = "$('input[id=train_date]').removeAttr('readonly')"
    driver.execute_script(js)
    data_element = driver.find_element_by_id("train_date")
    time.sleep(2)
    data_element.click()
    data_element.clear()
    data_element.send_keys("2019-06-02")
    driver.find_element_by_class_name("form-label").click()
    driver.find_element_by_id("search_one").click()
    time.sleep(5)

if __name__ == "__main__":
    search_12306()
