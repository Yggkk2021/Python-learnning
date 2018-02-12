# 14-5 一个使用了线程处理的服务器
from SocketServer import TCPSserver,ThreadingMixIn,StreamRequestHandler
class Server(ThreadingMixIn,TCPSserver):pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from',addr)
        self.wfile.write('Thank you for connecting')
server = Server(('',1234),Handler)
server.server_forever()