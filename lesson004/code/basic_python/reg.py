# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 14:51
# @Author  : zdRan
# @FileName: reg.py
# @Software: PyCharm
# @Blog    ：https://github.com/zdRan/FuturePlanNodes

import re

s = "代码地址是http://www.github.com"

reg = "http://[w]{3}\.[a-z0-9]*\.com"
result = re.findall(reg, s)
print(result)

s = "hello python hello"
reg = "hello"
print(re.findall(reg,s))
print(re.findall(reg,s)[1])

# 元字符
'''
. 代表换行符以外的任意字符
\w 匹配字母、数字、汉字、下划线
\s 匹配任意空白符
\d 匹配任意数字
^  匹配字符串开头
$  匹配字符串结束

'''

s = "dasdasdasd汉字汉字汉    字  12312312！@#￥%"
print(re.findall('\w',s))
print(re.findall('\d',s))
print(re.findall('\s',s))
print(re.findall('^d',s))

# 反义代码
'''
\W 匹配与 \w 相反的内容
\S 匹配与 \s 相反的内容
\D 匹配与 \d 相反的内容
'''

# 限定符
'''
* 重复 0 次或多次
+ 重复 1 次或多次
? 重复 0 次或 1 次
{n} 重复 n 次
{n,} 最小重复 n 次
{n,m} 重复 n 到 m 次

'''

s = "aaaa111nnn!!!n333444555汉字"
print(re.findall('\d{3}',s))

# 分组匹配
s = "qq号是12345678，邮编地址是11111，我的手机号是222222"
reg = "(\d{8}).*(\d{5})"
print(re.findall(reg,s))
print(re.search(reg,s))
print(re.search(reg,s).group())
# 整个正则表达式匹配到的内容
print(re.search(reg,s).group(0))

print(re.search(reg,s).group(1))
print(re.search(reg,s).group(2))