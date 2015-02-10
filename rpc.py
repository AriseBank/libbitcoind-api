#!/usr/bin/env python

from bitcoinrpc.authproxy import AuthServiceProxy
import threading
import queue

class BitcoinRPCHandle:
    def __init__(self, rpcurl):
        """ Initialize the RPC handle using the URL
            pointing to the bitcoind instance. """
        self._request_queue = queue.Queue()
        self._response_queue = queue.Queue()
        threading.Thread(target=self._RPCThread, args=(rpcurl,), daemon=True).start()

#    def SyncRequest(self, request):
#        """ TODO: Implement blocking synchronous request that returns. """

    def AsyncRequest(self, request):
        """ Send an RPC request asynchronously. """
        self._request_queue.put(request)

    def GetResponse(self):
        """ Pop a response from the queue and return it. """
        try:
            response = self._response_queue.get(False)
            return response
        except queue.Empty:
            pass
        return False

    #==========================================================================
    # Code below here operates in the RPC thread.
    #==========================================================================

    def _RPCThread(self, rpcurl):
        try:
            self._handle = AuthServiceProxy(rpcurl)
            self._handle.help()
        except Exception:
            raise ConnectionError("Failed to connect to bitcoind")

        while True: # Daemon thread dies with the main thread.
            request = self._request_queue.get(True)
            response = self._Request(request)
            self._response_queue.put(response)

    def _Request(self, request, *args):
        """ Send an RPC request and return its' output. """
        import time
        try:
            response = getattr(self._handle, request)(*args)
            return (request, (int(time.time()), response))
        except Exception:
            raise ConnectionError("Failed to perform API request \'%s\'"
                                    % request)
