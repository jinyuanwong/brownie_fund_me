from scripts.util_scripts import*

from brownie import FundMe
def fund():

    contract = FundMe[-1]
    
    account = get_account()
    print(account)

    entranceFee = contract.getEntranceFee()
    
    contract.fund({'from': account, 'value':entranceFee})
def withdraw():
    contract = FundMe[-1]

    account = get_account()

    contract.withdraw({'from': account})
def main():
    fund()
    withdraw()