# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 20:52
# @Author  : zdRan
# @FileName: import_package.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

# 导包

#from 包名 import 模块名
from package.module import my_print ,ImportClass

my_print()
ic = ImportClass
ic.import_class_my_print()

from package import module
module.my_print()

#from ... import ... as 别名
from package import module as m
m.my_print()



