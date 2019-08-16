# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 21:41
# @Author  : zdRan
# @FileName: my_screenshot.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r"D:\SDK\python_env\chromedriver.exe")

driver.get("https://www.jd.com")
driver.find_element_by_link_text("手机").click()
handlers = driver.window_handles
current_handler = driver.current_window_handle

for handler in handlers:
    if handler != current_handler:
        driver.switch_to.window(handler)
        driver.save_screenshot("home.png")

#关闭当前标签页面
driver.close()
#关闭整个浏览器
driver.quit()
