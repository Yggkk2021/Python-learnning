# 创建自己的类
# 1.确定使用的新式类
__metaclass__ = type
class Person:
    # self参数事实上是方法和函数的区别
    def __set_name__(self, name):
        self.name = name

    def __get_name__(self):
        return self.name

    def greet(self):
        print("Hello,world! I \'m %s" % self.name)
foo = Person()
foo.__set_name__('yangshunfang')
foo.greet()

# -------

# 7.2.3 特性、函数和方法
class Demo:
    def method(self):
        print('I have a self')

def function():
    print('I don\'t have self')

demo = Demo()
demo.method()
demo.method = function
demo.method()

# 方法私有(外部无法访问)
class Func:
    # 在方法前加双下划线就好
    def __youCannotSee(self):
        print('you can\'t see')
    def youCanSee(self):
        print('you can see')
        self.__youCannotSee()
f = Func()
# 若在这里f.__sayHello会报错
f.youCanSee()

# ----------

# 类的命名空间
# 下面两个语句几乎等价
def foo(x):
    return x*x
foo = lambda x: x*x

# 在看下面的例子
class MemberCounter:
    members = 0
    def init(self):
        self.members += 1

m1 = MemberCounter()
m2 = MemberCounter()
m1.init()
m2.init()
print(MemberCounter.members)
print(m1.members)
print(m2.members)

# ----------

# 指定超类
class Fileter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Fileter):
    def init(self):
        self.blocked = ['SPAM']

f = Fileter()
f.init()
print(f.filter([1,2,3]))
s = SPAMFilter()
s.init()
print(s.filter([1,2,3,'SPAM']))

# 检查继承 issubclass(A,B)函数 检查B是否是A的超类
i = issubclass(SPAMFilter,Fileter)
print(i)

# ----------

# 多个超类
class Calculator:
    def calucalate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print('Hi! my value is',self.value)