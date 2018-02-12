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

# 练习
def story(**kwds):
    return '在很久很久以前有个%(job)s叫%(name)s.' % kwds

def power(x,y,*others):
    if others:
        print('接受多余参数:' + others)
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step > 0'
    # 如果没有为stop提供值
    if stop is None:
        # 指定参数
        start,stop = 0,start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result
# 测试
print(story(job="国王",name="杨顺帆"))
# 用这种方式输入中文字符，每个中文字符后面都会有个空字符
params = {'job':'老师','name':'哈哈'}
print(*story(**params))

print(power(2,3))

print(interval(10))