#!/usr/bin/env python

DATA_TIMEOUT = 10

def HasExpired(item):
    import time
    if (time.time() - item[0]) > DATA_TIMEOUT:
        return True

    return False

class State():
    def Keys(self):
        return self.keys.keys()

    def Get(self, key, timeout=True):
        """ Get the data item associated with 'key'.

        If timeout=True, query the RPC server for an updated item. """

        if not (key in self.keys) or (timeout and HasExpired(self.keys[key])):
            self.keys[key] = self.handle.Request(key)

        return self.keys[key]

    def Update(self, timeout=True):
        """ Updates all expired state items via RPC queries.

        If timeout=False, updates all state items. """

        for key in self.keys:
            if not timeout or HasExpired(self.keys[key]):
                self.keys[key] = self.handle.Request(key)

    def __init__(self, handle):
        self.handle = handle
        self.keys = {}
