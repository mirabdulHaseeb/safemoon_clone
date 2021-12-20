from brownie import accounts, config, SafeMoonClone

def deploy_safemoon():
    owner = accounts.add(config["wallets"]["from_key"])
    safemoon = SafeMoonClone.deploy({"from": owner})
    print(safemoon.balanceOf(owner))


def main():
    deploy_safemoon()