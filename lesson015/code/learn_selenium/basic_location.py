# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 22:21
# @Author  : zdRan
# @FileName: basic_location.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"D:\SDK\python_env\chromedriver.exe")

driver.get("https://www.jd.com")

# search_element = driver.find_element_by_id("key")
#
# search_element.send_keys("电脑")
# search_element.send_keys(Keys.ENTER)

#driver.find_element_by_class_name("cate_menu_lk").click()
# driver.find_element_by_link_text("手机").click()
driver.find_element_by_xpath("//*[@id=\"J_cate\"]/ul/li[7]").click()


