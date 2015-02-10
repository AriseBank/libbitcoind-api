#!/usr/bin/python

def Debug(state):
    """ Debugging function for development purposes. """
    print("=== libbitcoind-api test ===\n")

    watchlist = ['getblockchaininfo', 'getmempoolinfo', 'getmininginfo',
                    'getnetworkinfo', 'getnettotals', 'getconnectioncount',
                    'getwalletinfo']
    state.UpdateBatch(watchlist)

    import time
    while 1:
        state.Sync()
        state.UpdateAll()
        for key in state.Keys():
            print(key, state.Get(key))
        print()
        time.sleep(1)
