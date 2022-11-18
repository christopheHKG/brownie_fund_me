from brownie import FundMe, MockV3Aggregator
from brownie import network, config

from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    print(f"using account {account} \n")
    
    #pass the priceFeed address to the AggregatorV3Interface contract to the constructor in FundMe
    #if we are on a persistent network like Goerli, use the associated address
    #else, deploy mock
    
    print(f"active network: {network.show_active()}\n")
        
    if (network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed_address"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address #use the most recently deployed Mock
     
    print("Deploying contract FundMe.sol\n")
    fund_me = FundMe.deploy(price_feed_address, {"from":account}, publish_source=config["networks"][network.show_active()]["verify"]) 
    #verify contract if on Etherscan ; can use: .get("verify") instead of ["verify"]
    print(f"Contract deployed @ {fund_me.address}\n")
    return fund_me
    
def main():
    deploy_fund_me()
