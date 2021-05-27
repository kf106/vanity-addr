import sys
import os
from eth_account import Account

if len(sys.argv) < 2:
    print("Vanity prefix not provided")
    sys.exit()

vanity = sys.argv[1]

try:
    int(vanity, 16)
except:
    print("Vanity prefix must be a hex string")
    sys.exit()

print("Searching for address starting with 0x" + vanity)
print("This is length " + str(len(vanity)))
print("Expected number of tries: " + str(16**len(vanity)))
count = 0

while True:
    count = count + 1
    if not count % 100000:
        print(count)
    privkey = os.urandom(32)
    acct = Account.privateKeyToAccount(privkey)
    acct_addr = acct.address
    if acct_addr[2:len(vanity)+2].lower() == vanity:
        print("Private key: " + str(privkey.hex()))
        print("Deployment address: " + acct_addr)
