import sys
from bitcoinrpc.authproxy import AuthServiceProxy

RPC_ADDRESS="<you ip address>:8332"
RPC_USER="you rpc username"
RPC_PASSWORD="you rpc password"

def connect(address, user, password):
        return AuthServiceProxy("http://%s:%s@%s"%(user, password, address))

rpc = connect(RPC_ADDRESS, RPC_USER, RPC_PASSWORD)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        startbl = int(sys.argv[1])
    else:
        startbl = rpc.getblockcount()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        stopbl = int(sys.argv[2])
    else:
        stopbl = rpc.getblockcount()

for blnum in xrange(startbl, stopbl+1):
        block = rpc.getblock(rpc.getblockhash(blnum))
        for tx in block[u'tx']:
                print(str(tx))
