#!/usr/bin/env python

class Config:
    def _ParseConfig(self):
        """ Parse the configuration file.
            Credit: wumpus/laanwj """
        with open(self.filename) as f:
            self.keys = {}
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    try:
                        (key, value) = line.split('=', 1)
                        self.keys[key] = value
                    except ValueError:
                        # Line has no '='; ignore it
                        pass

    def GetRPCURL(self):
        """ Return the URL pointing to bitcoind for use by
            rpc.BitcoinRPCHandle() """
        user = self.keys.get('rpcuser')
        password = self.keys.get('rpcpassword')
        ip = self.keys.get('rpcip', '127.0.0.1')

        if self.keys.get('rpcport'):
            port = keys.get('rpcport')
        elif self.keys.get('testnet') == "1":
            port = '18332'
        else:
            port = '8332'

        if self.keys.get('rpcssl') == "1":
            proto = "https"
        else:
            proto = "http"

        return proto + "://" + user + ":" + password + "@" + ip + ":" + port

    def __init__(self, filename):
        """ Try to open and parse the configuration file. """
        try:
            self.filename = filename
            self._ParseConfig()
        except IOError:
            raise FileNotFoundError("Failed to load config file \'%s\'"
                                    % filename)
