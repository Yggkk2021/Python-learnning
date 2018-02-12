# 使用了分叉技术的服务器
# 注意Windows不支持分叉
from SocketServer import TCPServer,FokingMixIn,StreamRequestHandler
# pass 什么也不做，是个占位符，一般用来保持程序完整
class Server(ForkingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
    def handle(self): # 重载handle函数
        addr = self.request.getpeername() # 获取地址
        print('Got connection for',addr) # 打印客户端地址
        self.wfile.write('Thank you for connecting') # 发送信息

server = Server(('',1234),Handler)
server.serve_forever() # 开始侦听病处理连接
