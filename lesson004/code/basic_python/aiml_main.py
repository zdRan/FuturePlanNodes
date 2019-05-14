# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 15:29
# @Author  : zdRan
# @FileName: aiml_main.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

"""
安装 aiml
pip install aimi
"""

import aiml

k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml b")

while True:
    print(k.respond(input("input >> ")))


