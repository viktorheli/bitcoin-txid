# bitcoin-txid
Get all txid from block or range of blocks

Simple Python script for get all transactions id from Bitcoin blockchain.
Dependencies:

1. [python-bitcoinrpc](https://github.com/jgarzik/python-bitcoinrpc)

  pip install python-bitcoinrpc

2. Installed and full synced [Bitcoin Core](https://bitcoin.org/en/wallets/desktop/linux/bitcoincore/) wallet

How to use:

pyhton gettxid.py <start block> <end block>

Start without any parameters will display all tx-id from last block.
