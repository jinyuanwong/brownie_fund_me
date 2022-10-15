from scripts.deploy_fund_me import deploy_fund_me
from scripts.util_scripts import get_account,LOCAL_BLOCKCHAIN_NETWORKS
from brownie import network,accounts,exceptions
import pytest

def test_fund_me():
    account = get_account()
    fund_me = deploy_fund_me()
    entranceFee = fund_me.getEntranceFee()+100 # this must be larger than fund_me.getEntranceFee(), or it might fail.
    tx1 = fund_me.fund({'from': account, 'value': entranceFee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entranceFee
    tx2 = fund_me.withdraw({'from': account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
# def test_only_owner_withdraw():
#     if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS:
#         pytest.skip('Only test in the local network.')
    
#     fund_me = deploy_fund_me()

#     bad_actor = accounts.add()

#     with pytest.raises(exceptions.VirtualMachineError):
#         fund_me.withdraw({'from': bad_actor})
#         # print("Hello World")