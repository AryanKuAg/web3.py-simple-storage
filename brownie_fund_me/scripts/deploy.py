from brownie import FundMe
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # print(account)
    fund = FundMe.deploy(
        "0xCD68fB5449c5Cc1c09F430Cb90c2c0A89e8eF1Ad", {"from": account})
    # print(f"deployed to {fund.address}")


def main():
    deploy_fund_me()
