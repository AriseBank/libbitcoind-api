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

    import time
    while 1:
        getinfo = state.Get('getinfo')
        print(getinfo)
        time.sleep(1)
