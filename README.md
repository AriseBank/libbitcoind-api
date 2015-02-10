# libbitcoind-api

Python library for interacting with the Bitcoin Core API.
azeteki - https://azeteki.github.io

## NOTE - libbitcoind-api is currently under development and is uploaded here for informational purposes only.

## Dependencies

* Current development takes place on Python 3.4.1, Bitcoin Core v0.10.0rc4
* jgarzik's bitcoinrpc library (https://github.com/jgarzik/python-bitcoinrpc)

## Setup

```
git clone https://github.com/azeteki/libbitcoind-api.git
```

Ensure that the RPC server is up and running. You may test it using the
following command:

```
bitcoin-cli help
```

Copy your bitcoin.conf to libbitcoind-api's folder, or alternatively run with
the --config=/path/to/config/file switch.

## Launch

Note that libbitcoind-api requires Python 3 in order to run.
```
$ python main.py
$ python3 main.py
```

## Frog food

Do you find libbitcoind-api useful?
Please donate to support your friendly neighbourhood amphibian.

![ScreenShot](/img/donation-qr.png)

**1FrogqMmKWtp1AQSyHNbPUm53NnoGBHaBo**
