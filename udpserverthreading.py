from SocketServer import UDPServer, BaseRequestHandler

class Handler(BaseRequestHandler):
    def handle(self):
        print "message:", self.request[0]
        print "from:", self.client_address
        socket = self.request[1]
        socket.sendto("hello", self.client_address)


addr = ("", 5555)
print "listening on %s:%s" % addr
server = UDPServer(addr, Handler)
server.serve_forever()


