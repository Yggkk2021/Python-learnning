# 八皇后问题
# 已知的皇后的位置被传递诶conflict函数，然后又函数判断下一个皇后的位置会不会又冲突
def conflict(state, nextX):
    # nextX表示水平位置（X坐标）nextY表示垂直位置（Y坐标）
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后和正在考虑的前一个皇后的水平距离为0或等于垂直距离，就返回False
        if abs(state[i] - nextX) in (0, nextY - 1):
            return False
    return True


# 最后一个皇后时
def queens(num=8, state=()):
    for pos in range(num):
        if conflict(state, pos):
            if len(state) == num - 1:
                # yield类似返回return，但是下一次直接从yield下一行代码开始执行
                # yield返回执行结果并不中断程序执行，return在返回执行结果的同时中断程序执行。
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


# 最后处理
def prettyprint(solution):
    # 函数内部的函数为助手函数
    def line(pos, length=len(solution)):
        return '. ' * pos + '* ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


# print(len(list(queens(8))))
import random
prettyprint(random.choice(list(queens(8))))
