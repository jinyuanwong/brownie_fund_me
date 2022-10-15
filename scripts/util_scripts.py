

from hashlib import new
from brownie import accounts,config,network,MockV3Aggregator

from web3 import Web3

DECIMAL= 8
STARTING_PRICE= 2 * 10**DECIMAL
LOCAL_BLOCKCHAIN_NETWORKS = ['development','ganache-local']
FORK_BLOCKCHAIN_NETWORKS = ['mainnet-fork-dev']
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_NETWORKS or network.show_active() in FORK_BLOCKCHAIN_NETWORKS:
        return accounts[0]
    else:
        return accounts.add(config['wallet']['from_key'])


def deploy_mocks():
    print(f'The active network is {network.show_active()}')
    print('Start deploying mocks...')
    if len(MockV3Aggregator)<20:
        MockV3Aggregator.deploy(
            DECIMAL,
            Web3.toWei(STARTING_PRICE,'ether'),
            {'from':get_account()},
        )
    print('Successfuly deployed mocks!')