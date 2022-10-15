from threading import active_count
from scripts.util_scripts import*
from brownie import FundMe,config,network,MockV3Aggregator
from web3 import Web3

def deploy_fund_me():
    account = get_account()
    current_network = str(network.show_active())
    if current_network in LOCAL_BLOCKCHAIN_NETWORKS:
        deploy_mocks()
        price_fee_address = MockV3Aggregator[-1].address
    else:
        price_fee_address = config['networks'][current_network].get('price_fee_address')
        print(f'this is price_fee_address:{price_fee_address}' )
    verify = config['networks'][current_network].get('verify')
    print(f'Active Account: {account}')
    fund_me = FundMe.deploy(
        price_fee_address,
        {'from': account},
        publish_source = verify,
        )
    print(f'Successfully deployed Fund-Me contract: {fund_me.address}')

    return fund_me
def main():
    deploy_fund_me()

