import sys
import os
from eth_account import Account

if len(sys.argv) < 3:
    print("Vanity suffix and prefix not provided")
    sys.exit()

vanityPrefix = sys.argv[1]

vanitySuffix = sys.argv[2]

try:
    int(vanityPrefix, 16)
except:
    print("Vanity prefix must be a hex string")
    sys.exit()
    
try:
    int(vanitySuffix, 16)
except:
    print("Vanity suffix must be a hex string")
    sys.exit()

print("Searching for address starting with 0x" + vanityPrefix + " and ending with " + vanitySuffix)
print("This is length " + str(len(vanitySuffix) + len(vanityPrefix)))
print("Expected number of tries: " + str(16**len(vanitySuffix + vanityPrefix)))
count = 0

while True:
    count = count + 1
    if not count % 100000:
        print(count)
    privkey = os.urandom(32)
    acct = Account.privateKeyToAccount(privkey)
    acct_addr = acct.address
    if acct_addr[2:len(vanityPrefix)+2].lower() == vanityPrefix and acct_addr[-1*len(vanitySuffix):].lower() == vanitySuffix:
        print("Private key: " + str(privkey.hex()))
        print("Account address: " + acct_addr)
