from brownie import FundMe

def test():
    contract = FundMe[-1]

    print(contract.getConversionRate(1))
    print(contract.getPrice())

def main():
    test()