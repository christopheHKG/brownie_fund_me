from brownie import accounts, config, network
from brownie import MockV3Aggregator
#from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev" ]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000_000_000_000_000_000_000

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])

def deploy_mocks():
    print("Deploying Mocks...\n")
        #only deploy if there is no Mock already deployed:
    if len(MockV3Aggregator)<=0 :   
        #excerpt:  constructor(uint8 _decimals, int256 _initialAnswer)
        # use Web.toWei to add 18 decelimal zeroes
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print(f"Mocks deployed @ {mock_aggregator.address}\n")
    else:
        print("using existing Mocks")
        