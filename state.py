#!/usr/bin/env python

DATA_TIMEOUT = 5

class State():
    def Get(self, key):
        """ Get the data item associated with 'key'.

            If this item has not been previously requested, or it has
            expired, query the RPC server for it synchronously. """

        import time

        cur_time = time.time()

        if (not (key in self.keys) or
                (time.time() - self.keys[key][0]) > DATA_TIMEOUT):
            self.keys[key] = (time.time(), self.handle.Request(key))

        return self.keys[key]

    def __init__(self, handle):
        self.handle = handle
        self.keys = {}
