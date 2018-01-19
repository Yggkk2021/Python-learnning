# 2.3.1
str = list('hello');
print(str)

# 2.3.2.1 改变列表：元素复制
# 这里注意，不能为一个不存在的位置复制
x = [1,2,1]
x[2] = 4
print(x)

# 2.3.2.2 删除元素
names = ['Alice','Beth','Cecil','Tom','Jerry']
# 删除Beth
del names[1:]
print(names)

# 2.3.2.3 分片赋值
names = list('Perl')
print(names)
# 分片赋值
names[1:] = list('ython')
print(names)

numbers = [1,2,3,4,5]
# 这里相当于在第二个数和第三个数中间增加元素,2没有被包括在内，而3被替换了
numbers[2:3] = [6,7,8,9]
print(numbers)
# 这里可以看到若分片赋值后的位置不够，列表会进行增加numbers=[1,2,3,4,5]变成numbers=[1,2,6,7,8,9,4,5],列表长度增加了

# ----------------------------------------------------------

# 2.3.3
# 2.3.3.1 append 用于在列表末尾追加新的对象
lst = [1,2,3]
lst.append(4)
print(lst)

# 2.3.3.2 count 计算某个元素在列表中出现的次数
counts = ['to','but','haha','hehe','hehe','to']
temp = counts.count('hehe')
print(temp)

# 2.3.3.3 extend 继承
a = [1,2,3]
b = [4,5,6]
a.extend(b)
# 这里a继承b，a = [1,2,3,4,5,6],b不变
print(a)
print(b)

# 2.3.3.4 index 找出第一个与目标值匹配的下表
best = ['We','art','the','best']
n = best.index('best')
# n = 3
print(n)

# 2.3.3.5 insert 插入
numbers = [1,2,3,4,5]
numbers.insert(3,999)
print(numbers)

# 2.3.3.6 pop 移除列表的最后一个元素，若没有指定，则移除最后一个
x = [1,2,3]
x.pop()
print(x)
x.append(3)
# x = [1,2,3]
x.pop(0)
print(x)

# 2.3.3.7 remove 移除一个指定的值
a = ['Just','do','it','ok']
a.remove('ok')
print(a)

# 2.3.3.8 reverse 方法见将列表中的元素方向存着
x = [1,2,3]
x.reverse();
print(x)

# 2.3.3.9 sort 排序
x = [4,3,2,12,3,42,2]
x.sort()
print(x)
# 获取排序后副本，原列表不变
x = [4,3,2,12,3,42,2]
y = sorted(x)
print(x)
print(y)