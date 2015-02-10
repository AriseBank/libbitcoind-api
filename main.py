#/usr/bin/env python

#==============================================================================
# libbitcoind-api by azeteki
# https://github.com/azeteki/libbitcoind-api
#==============================================================================

def ParseArguments():
    """ Parse the command-line arguments passed from the shell. """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config",
                        help="path to config file [bitcoin.conf]",
                        default="bitcoin.conf")

    return parser.parse_args()

if __name__ == '__main__':
    args = ParseArguments()

    import config
    cfg = config.Config(args.config)
    url = cfg.GetRPCURL()

    import rpc
    handle = rpc.BitcoinRPCHandle(url)

    import state
    state = state.State(handle)

    print("=== libbitcoind-api test ===\n")

    watchlist = ['getblockchaininfo', 'getmempoolinfo', 'getmininginfo',
                    'getnetworkinfo', 'getnettotals', 'getconnectioncount',
                    'getwalletinfo']
    state.BatchGet(watchlist)

    import time
    while 1:
        state.Update(False)
        for key in state.Keys():
            print(key, state.Get(key))
        print()
        time.sleep(1)
