# Ethereum Vanity Wallet and Contract Address Generator

This repository contains two scripts - one tries to find private keys that produce public addresses with a given prefix. The other script finds private keys that correspond to public addresses for which the first deployed contract starts with the given prefix.

## Installation
In order to ensure you have the correct Python configuration you should install and run pyenv:

     curl https://pyenv.run | bash

Then enable it in your current shell:

     export PATH="/home/$USER/.pyenv/bin:$PATH"
     eval "$(~/.pyenv/bin/pyenv init -)"
     eval "$(~/.pyenv/bin/pyenv virtualenv-init -)"

Finally, make Python 3.8.2 the default for the project folder:

     pyenv install 3.8.2
     pyenv virtualenv 3.8.2 ethereum
     pyenv local ethereum

You can then install the packages required using pip3:

     pip install rlp eth_account eth_utils

## Running the script

Run either script with one command line argument, that is the hex string you want the address to begin with. Ethereum checksum addresses mean that some letters will be capitalized - this is ignored in the scripts. Etherscan shows them all in lower case in the activity pane anyway.

     python vanity-address.py c0ffee
     python vanity-contract.py 001122

Note that longer prefixes take quadratically longer to find.
