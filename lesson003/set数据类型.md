# set 数据类型
保存无序且不重复的数据序列，格式

```
# 声明
set_param = set()
print(set_param)
print(type(set_param))

set_param = {1,2,3}
print(set_param)
print(type(set_param))
```

## in 运算

判断一个 元素是否在集合内

```
print(1 in set_param)
```

## 集合运算

```
a = set("abcd") # 会把 字符串拆分开
b = set("cdef")

# 并集
print(a | b)
# 交集
print(a & b)

```

## 集合操作
```
# 集合操作
my_set = set(("abc","cde","def"))

my_set.add("fgh")
print(my_set)

my_set.remove("abc")
print(my_set)
my_set.clear()
print(my_set)
```