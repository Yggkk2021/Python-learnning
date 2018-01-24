# 条件和循环语句
x = True + False + 42
print(x)

# ---------------

# 5.4.2 条件执行和if语句
name = input("What is your name:")
if name.endswith('yangshunfan'):
    print('Hello.Mr.yangshunfan')

# ---------------

# 5.4.3 else子句
name = input('What si your name:')
if name.endswith('yangshunfan'):
    print('Hello,Mr.yangshunfan')
else:
    print('Hello,stranger')

# ---------------

# 5.4.4 elif子句
num = int(input("Enter a number:"))
if num > 0:
    print('这个数大于零')
elif num < 0:
    print('这个数小于0')
else:
    print('这个数等于零')

# ---------------

# 5.4.5 嵌套代码块
name = input('What is your name?')
if name.endswith('yangshunfan'):
    if name.startswith('Mr'):
        print('Hello, Mr.yangshunfan')
    elif name.startswith('Mrs'):
        print('Hello,Mrs')
    else:
        print('Hello,yangshunfan')
else:
    print('Hello,stranger')

# ++++++++++++++++++++++++++++++++=

# 运算符
# is 统一运算符
x = 1
y = 2
print(x is y)
y = 1
print(x is y)

# in 成员资格运算符
x = "asdf"
if 's' in x:
    print('has s word')
else:
    print('have no s')

# assert 断言
x = 1
# 如果x>2，则继续执行后面的代码，若不满足条件，则宝报错
assert x > 2
print("x > 2")

# ++++++++++++++++++++++++++++++++=

# 循环
# while
x = 0
while x <= 100:
    print(x)
    x += 1

# for
x = [1,2,3,4,5,6,7]
for i in x:
    print(i)

# range
for i in range(100):
    print(i)

# 遍历字典
dic = {'x':1,"y":2,'z':3}
for key in dic:
    print(key)

# 翻转和排序迭代
x = [12,3,1,2,31,23,34,6]
print(sorted(x))
x = 'hello world'
print(list(reversed(x)))

# break and continue
# break
x =[1,2,3,4,5]
for i in x:
    if i < 3:
        print(i)
    else:
        break

# continue
for i in range(100):
    if i % 2 == 0:
        print(i)
    else:
        continue

# 列表推导式
print([x*x for x in range(10)])