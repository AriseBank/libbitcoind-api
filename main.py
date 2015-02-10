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

def InitializeState():
    args = ParseArguments()

    import config
    cfg = config.Config(args.config)
    url = cfg.GetRPCURL()

    import rpc
    handle = rpc.BitcoinRPCHandle(url)

    import state
    return state.State(handle)

if __name__ == '__main__':
    state = InitializeState()

    import debug
    debug.Debug(state)
