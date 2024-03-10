import os
import sys
from eth_account import Account
from eth_utils import keccak, to_checksum_address, to_bytes
import rlp


def mk_contract_address(sender: str, nonce: int) -> str:
    """Create a contract address using eth-utils.
    # https://ethereum.stackexchange.com/a/761/620
    """
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    h = keccak(raw)
    address_bytes = h[12:]
    return to_checksum_address(address_bytes)


if len(sys.argv) < 2:
    print("Vanity prefix not provided")
    sys.exit()

vanity = sys.argv[1]

try:
    int(vanity, 16)
except:
    print("Vanity prefix must be a hex string")
    sys.exit()

print("Searching for first contract starting with 0x" + vanity)
print("This is length " + str(len(vanity)))
print("Expected number of tries: " + str(16**len(vanity)))
count = 0

while True:
    count = count + 1
    if not count % 100000:  # show every 100k tries so we can see progress
        print(count)
    privkey = os.urandom(32)
    acct = Account.from_key(privkey)
    contract = mk_contract_address(acct.address, 0)
    if contract[2:len(vanity)+2].lower() == vanity:
        print("Private key: " + str(privkey.hex()))
        print("Deployment address: " + acct.address)
        print("First contract address: " + contract)
