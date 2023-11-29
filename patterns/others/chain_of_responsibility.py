class Handler:
    """Abstract handler"""

    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)  # if handled, stop here

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation")


class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print(f"Request {request} is handled in handler 1")
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        """if there is no handler available"""
        print(f"End of chain, no handler for {request}")
        return True


class Client:
    def __init__(self):
        # create handlers
        self.handler = ConcreteHandler1(successor=DefaultHandler(None))

    def delegate(self, requests):
        for req in requests:
            self.handler.handle(req)


client = Client()
client.delegate([2, 5, 30])