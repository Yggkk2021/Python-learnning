# 创建和使用字典
# 4.2.1 dict函数，需要注意的是dict函数并不是真正的函数。它是类型，就想list、tuple一样,就是key-value形式储存的

auther = dict([('name','yangshufan'),('age',23)])
print(auther)
print(auther['name'])

# ---------------------------

# 4.2.2 基本字典操作
# 键可以使任意不可变类型——这是字典最强大的地方
# x = [] //这里会报错
# x[42] = '42'
# print(x[42])
x = {}
x[42] = '42'
print(x[42])
print(x)

# 电话簿例子
people = {
    'yangshunfan': {
        'phone': '123456',
        'address': 'Baker Street 221B'
    },
    'ergou' : {
        'phone' : '123123',
        'address' : 'Hunan'
    },
    'Jack Ma' : {
        'phone' : '',
        'address' : 'Zhejiang'
    }
}
# 针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
labels = {
    'phone': 'phone number',
    'address': 'address'
}
name = input('Name:')
# 查找电话号码还是地址
request = input('Phone number (p) or address (a) ?')
# 使用正确的键
if request == 'p': key = 'phone'
if request == 'a': key = 'address'
# 如果名字是字典中的有效键才打印信息
if name in people:print(("%s\'s %s is %s.") % \
                  (name, labels[key], people[name][key]))

# ---------------------------

# 4.2.3 字典的格式化字符串
phonebook= {'java':'1234','python':'4321','C++':'1111'}
print(phonebook)

# ---------------------------

# 4.2.4 字典方法
# 4.2.4.1 clear 用于清除字典里所有的项
d = {}
d['name'] = 'yangshunfan'
d['age'] = 42
print(d)
returned_value = d.clear()
print(returned_value)

# *******

# 4.2.4.2 copy 赋值一个字典
x = {'username':'yangshunfan','choice':['run','jump','walk']}
y = x.copy()
y['username'] = 'jack'
y['choice'].remove('walk')
y['choice'].append('bus')
# 若是修改某个值，原值不会变，若是移除或者添加都会影响到原函数
print(y)
print(x)
# 为了避免这个问题，我们需要使用deep copy来对函数进行操作
from copy import deepcopy
d = {}
d['names'] = ['tom','jerry']
c = d.copy()
f = deepcopy(d)
d['names'].append('Han')
print(c)
print(f)

# *******

# 4.2.4.3 fromkeys 使用给定的键建立新的字典，每个键都对应一个默认的值None
str = {}.fromkeys(['name','age'])
print(str)
# 这里有个小小的插曲,若你没有使用[]符号，他会将name拆分成n,a,m,e四个键，每个键的对象都是age,若有三个以上字符则报错

# *******

#4.2.4.4 get 获取访问字典项
# d = {}
# print(d['name']) //这样会报错
d = {}
print(d.get('name'))

# *******

# 字典方法实例
labels = {
    'phone': 'phone number',
    'addr':'address'
}
name = input("Name:")

# 查找电话号码还是地址
request = input('Phone number (p) or address (a) ?')

# 使用正确的键
key = request
if request == 'a':key = 'addr'
if request == 'p':key = 'phone'
# 使用get()提供默认值：
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,"not available")

print("%s\'s %s is %s." % (name,label,result))

# *******

# 4.2.4.5 in 可以检查字典中是否含有特定的键
d = {}
x = 'name' in d
print(x)

# *******

# 4.2.4.6 items和iteritems python3 没有iteritems
d = {
    'title':'Python Web Site','url':'https://www.python.org','spam':0
}

# *******

# 4.2.4.8 pop 获得指定的键，然后删除键
d = {'x':2,'y':4}
d.pop('x')
print(d)

# *******

# 4.2.4.11 update 利用一个字典对另外一个字典进行更新
d = {
    'title':'Python Web Site',
    'url':'https://www.python.org',
    'ip:':'127.0.0.1'
}
x = {
    'title': 'Python Language Website',
    'test': 'test'
}
d.update(x)
print(d)

# *******

# 4.2.4.12 value 以列表的形式返回字典中的值
d = {'1':'1','2':'2','3':'3'}
print(d.values())