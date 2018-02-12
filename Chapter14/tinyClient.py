# 一个小型的客户级
import socket
c = socket.socket() # 生成一个socket对象
host = socket.gethostname()
port = 1234

c.connect((host,port)) # 连接服务器
print(c.recv(1024)) # 读取数据
c.close() # 关闭连接