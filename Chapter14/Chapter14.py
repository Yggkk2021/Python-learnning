# 网络编程
# 14-1 一个小型服务器
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
# 捆绑ID或端口号
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection for', addr)
    c.send('Thank you for connecting')
    c.close()


