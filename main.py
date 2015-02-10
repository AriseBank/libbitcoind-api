#/usr/bin/env python

#==============================================================================
# libbitcoind-api by azeteki
# https://github.com/azeteki/libbitcoind-api
#==============================================================================

import config

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
    api = rpc.BitcoinRPCHandle(url)

    print("===")
    print("libbitcoind-api test")
    print("===")

    getinfo = api.Request('getinfo')
    print(getinfo)
