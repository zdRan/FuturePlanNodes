# dict字典
可变容器，存储键值对，见不可重复，	格式

```
d = {k:v,k:v,k:v}
```

## 声明
```
d = {1:"zhangsna", 2 :"lisi"}
print(d)

```
## 字典遍历

```
keys = d.keys()
print(keys)

for i in keys:
    print(i)
    print(d[i])

```

## 字典操作
```
# 添加
d[3] = "aaaa"
d.setdefault(4,"44444")
print(d)

# 更新
d[4] = "bbb"
print(d)

# 删除
# 删除并返回指定元素
r = d.pop(4)
print(r)
print(d)

del d[3]
print(d)
```