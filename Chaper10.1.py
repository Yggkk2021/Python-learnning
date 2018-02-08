# 模块
# 10.1.2 模块用于定义
# 这里我们导入HelloWorld.py模块
import HelloWorld
# 我们可以用模块来直接调用模块里的方法,这样可以提高代码重用
HelloWorld.sayHelloWorld()
import sys ,pprint
pprint.pprint(sys.path)

# 清单10-3
def hello():
    print('Hello Python')

hello()

# 10-4
def hello():
    print('Hello World')

def test():
    hello()

# 如果被作为主程序执行则hello()方法会执行，而作为模块导入时，它的行为就会和普通模块一样
# if __name__ == '__main__':
#     test()


# 10-6 反序打印命令行参数
import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

# 10-8 简单的数据库应用程序
def store_person(db):
    pid = input('Enter unique ID number:')
    person = {}
    person['name'] = input('Name:')
    person['age'] = input('Age:')
    person['phone'] = input('Phone:')

    db[pid] = person

def lookup_person(db):
    pid = input('Enter ID number:')
    field = input("What would you want to konw?(name,age or phone)")
    # 移除头部和尾部的换行和空格，再进行小写
    field = field.strip().lower()
    # str的capitalize()方法，将字符串的第一个字符变为大写
    print(field.capitalize() + ';',
          db[pid][field])

def print_help():
    print('The available commands are:')
    print('store  : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit   : Save changes and exit')
    print('?      : Prints this message')

def enter_command():
    cmd = input('Enter command (? for help):')
    cmd = cmd.strip().lower()
    return cmd