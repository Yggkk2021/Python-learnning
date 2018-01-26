# 创建函数
def sayHello(name):
    return('Hello,' + name + '!')
print(sayHello('yangshunfan'))

# ---------

# 6.3.1 文化档函数
# 这里给一个函数增加解释性文档，相当于注释
def square(x):
    '计算x的平方'
    return x*x
# 查看方法文档(这里要去掉后面的括号)：方法名._doc_
print(square.__doc__)
y = square(2)
print(y)
