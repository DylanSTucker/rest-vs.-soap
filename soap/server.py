#Dylan Tucker, dst833, 11235055
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import sys


sys.set_int_max_str_digits(0)



class HelloWorldService(ServiceBase):
    @rpc(Integer, _returns=Integer)
    def fib(ctx, n):
        num1 = 0
        num2 = 1
        nextNum = 1
        count = 1
        while count <= n:
            count += 1
            num1 = num2
            num2 = nextNum
            nextNum = num1 + num2
        return nextNum


application = Application([HelloWorldService], 'spyne.examples.hello.soap',in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()