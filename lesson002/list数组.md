# list数组
## list 是一个数组类型，格式是：

```
list = [1,2,3]

```
数组的元素可以是任意的类型，而且同一个 list 可以存储不同的元素类型

```
list1 = [1,2,3,4]
print(list1)
print(type(list1))

list2 = [1,2,3.1,'a','b',list1]

print(list2)
```

## list 的元素访问

+ 使用下标访问

```
list1 = [1,2,3,4]
print(list1[1]) # 2
```

+ 使用区间访问

```
list1 = [1,2,3,4]
print(list1[1:3]) # 2 3
print(list1[1:]) # 2 3 4
```
## list 添加元素
+ 使用 append 方法
+ 使用 ```+``` 运算符

```
list1.append('a')
list1 = list1 + ['c','d']
print(list1)
```

## list 元素的更新与删除

```
# 更新
list1[0] = 0
print(list1)

# 删除

del list1[-1]
print(list1)
```

## 嵌套列表

```
list1 = [1,2,3,4]

list2 = [1,2,list1]

print(list2[2][2]) # 3
```
