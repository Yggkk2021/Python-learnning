# 懒惰即美德
# 写一段程序表示斐波那契函数
fibs = [0,1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)