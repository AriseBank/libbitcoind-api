#!/usr/bin/env python

from bitcoinrpc.authproxy import AuthServiceProxy

class BitcoinRPCHandle:
    def __init__(self, rpcurl):
        """ Initialize the RPC handle using the URL
            pointing to the bitcoind instance. """
        try:
            self.handle = AuthServiceProxy(rpcurl)
            self.handle.help()
        except Exception:
            raise ConnectionError("Failed to connect to bitcoind")

    def Request(self, request, *args):
        """ Send an RPC request and return its' output. """
        import time
        try:
            response = getattr(self.handle, request)(*args)
            return (int(time.time()), response)
        except Exception:
            raise ConnectionError("Failed to perform API request \'%s\'"
                                    % request)
