# 字符串方法
# 3.4.1 find 查找字符出现的最左端的位置下标，找不到返回-1
str1 = 'With a moo-moo here. and a moo-moo there'
index1 = str1.find('moo')
print(index1)

str2 = '$$$ Get rich now $$$'
# 这里提供了起点为1，所以第一个$$$就没有找到
index2 = str2.find('$$$',1)
print(index2)
# 还可以设置终点,找不到返回-1
index3 = str2.find('$$$',1,5)
print(index3)

# -------------------------

# 3.4.2 join 方法 连接序列中的元素 必须是字符串 数组变为字符串
str3 = ['1','2','3','4','5']
sep = '+'
temp = sep.join(str3)
print(temp)

# -------------------------

# 3.4.3 lower 将字符串都变成小写
str4 = 'I LOVE YOU FOREVER!!!'
temp = str4.lower()
print(temp)

# -------------------------

# 3.4.4 replace 将所有匹配的字符串替换
str5 = 'I hate hate hate you!!!'
temp = str5.replace('hate','love')
print(temp)

# -------------------------

# 3.4.5 split join的逆方法，根据字符分隔字符串,变为字符串数组
str6 = '1,2,3,4,5'
temp = str6.split(',')
print(temp)

# -------------------------

# 3.4.6 strip 出去两侧空格的字符串
str7 = '      I love you       '
print(str7)
temp = str7.strip()
print(temp)

