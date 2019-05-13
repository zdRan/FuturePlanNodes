# 列表推导式
# x for x in a
# 遍历 in 之后的集合，执行 for 之前的表达式，将结果加入到结果集
y = [x + 1 for x in [1, 2, 3, 4]]
print(y)
print(list(x + 4 for x in [1, 2, 3, 4] if x > 2))


def qsort(my_list):
    if len(my_list) <= 1: return my_list
    return qsort([left_list for left_list in my_list[1:] if left_list < my_list[0]]) + \
           my_list[0:1] + \
           qsort([right_list for right_list in my_list[1:] if right_list >= my_list[0]])


def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        first = my_list[0]
        left_list = quick_sort([l for l in my_list[1:] if l < first])
        right_list = quick_sort([l for l in my_list[1:] if l >= first])

    return left_list + [first] + right_list


my_l = [1, 5, 3, 6, 7, 9, 2, 0]
print(qsort(my_l))

# 集合推导式
y = {x + 1 for x in [1, 2, 3, 4]}

# 字典推导式
d = {x: y for x, y in {"a": 1, "b": 2}.items() if y > 1}
d = {x for x, y in {"a": 1, "b": 2}.items()}
print(d)
