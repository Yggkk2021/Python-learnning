# 模块
# 10.1.2 模块用于定义
# 这里我们导入HelloWorld.py模块
import HelloWorld
# 我们可以用模块来直接调用模块里的方法,这样可以提高代码重用
HelloWorld.sayHelloWorld()
import sys ,pprint
pprint.pprint(sys.path)