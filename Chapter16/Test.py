# 第一个测试程序
from area import rect_area
height = 3
width = 4
correct_answer = 12
# 这里假设调用了rect_area函数来进行测试
answer = rect_area(height,width)

if answer == correct_answer:
    print("Test passed")
else:
    print('Test failed!')

def rect_area(h,w):
    return h*w