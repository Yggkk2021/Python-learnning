# 赋值魔法
# 5.2.1 序列解包
x,y,z = 1,2,3
print(x,y,z)
x,y = y,x
print(x,y,z)

# --------------

# 5.2.2 链是赋值 实际上就是从右往左开始赋值
x = y = 5
print(x)
print(y)

# --------------

# 5.2.3 增量赋值x
x = 1
# 相当于x = x + 1
x += 1
print(x)
x *= 2
print(x)