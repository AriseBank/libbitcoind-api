#!/usr/bin/env python

import time

DATA_TIMEOUT = 5

class State():
    def Keys(self):
        return self._RawKeys()

    def Get(self, key):
        """ Return the data item associated with 'key'.

        If the item has expired, query the RPC server asynchronously
        and return the old item (if available). """

        self.Update(key)
        return self._RawGet(key)

    def Expired(self, key, timeout=DATA_TIMEOUT):
        """ Return true if item older than timeout, or item does not exist. """
        item = self._RawGet(key)
        if item and (time.time() - item[0]) < timeout:
            return False
        return True

    def Sync(self):
        """ Incorporate responses from the queue into the current state. """
        while True:
            response = self.handle.GetResponse()
            if not response:
                break
            (key, payload) = response
            self._RawPut(key, payload)

    def Update(self, key):
        """ Update the data item associated with 'key'. """
        if self.Expired(key):
            self.handle.AsyncRequest(key)

    def UpdateBatch(self, keys):
        """ Batch update of multiple keys. """
        for key in keys:
            self.Update(key)

    def UpdateAll(self):
        """ Updates all expired state items via RPC queries. """
        self.UpdateBatch(self.Keys())

    def __init__(self, handle):
        self.handle = handle        # Handle to BitcoinRPCHandle object
        self.keys = {}

    #==========================================================================
    # Raw dictionary operations in case the DB format changes later.
    #==========================================================================

    def _RawGet(self, key):
        if key in self.keys:
            return self.keys[key]
        return False

    def _RawPut(self, key, payload):
        self.keys[key] = payload

    def _RawKeys(self):
        return self.keys.keys()
