# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 16:33
# @Author  : zdRan
# @FileName: reg.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes
"""
正则表达式高级应用
贪婪与非贪婪
非贪婪符号'?',可以在 *、+、? 后面使用
"""

import re

s = "githubaaaaaaaaaaa"
reg = "githuba*?"
reg2 = "githuba+?"

print(re.findall(reg2,s)) # github

# 分支条件匹配 (|)

s = "我的电话号码：010-89345738 0940-48594835 0049-4839576"
reg = "0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7}"
print(re.findall(reg,s))
reg = "0\d{2,3}-\d{7,8}"
print(re.findall(reg,s))

# 零宽断言
"""
?=reg 匹配 reg 前面的位置
?<=reg 匹配 reg 后面的位置
?!=reg 匹配后面跟的不是 reg 的位置
?<!reg 匹配前面跟的不是 reg 的位置

"""

s = "hellogithubworld"
# 符合 'l{2}o' 且在 'github' 之前
reg = "l{2}o(?=github)"
print(re.findall(reg,s))
# 在 'github'之后，且符合 '[a-z]*'
reg = "(?<=github)[a-z]*"
print(re.findall(reg,s))