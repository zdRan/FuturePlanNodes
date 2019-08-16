# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 21:30
# @Author  : zdRan
# @FileName: mouse_and_keyboard.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r"D:\SDK\python_env\chromedriver.exe")

driver.get("https://www.jd.com")

element = driver.find_element_by_link_text("手机")

ActionChains(driver).move_to_element(element).perform()
time.sleep(3)
old_phone = driver.find_element_by_link_text("老人机")
old_phone.click()

