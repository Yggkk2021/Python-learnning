# 使用了select的简单服务器
import socket,select
s = socket.socket() # 生成一个socket类

host = socket.gethostname()
part = 1234
s.bind(host,part)

s.listen(5)
inputs = [s]
while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print("Got connection from:",addr)
            inputs.append(c)
        else:
            try:
                # data获取接受的函数
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print(r.getpeername(),'disconnected')
                inputs.remove(r)
            else:
                print(data)
