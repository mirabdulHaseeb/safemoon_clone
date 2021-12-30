from brownie import accounts, config, SafeMoonClone

def test_transaction():
    owner = accounts.add(config["wallets"]["from_key"])
    receiver = "0x5297f21E36e727c1Fd2f875054E7DE654A8a296E"
    sfc = SafeMoonClone.deploy({'from': owner})
    print(f"Owner balance before at deployment: {sfc.balanceOf(owner)}")
    
    sfc.transfer(receiver, 100, {"from": owner})
    print(f"Receiver balance: {sfc.balanceOf(receiver)}")
    print(f"Owner balance: {sfc.balanceOf(owner)}")

def main():
    test_transaction()