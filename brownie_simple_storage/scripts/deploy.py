from brownie import accounts, config, SimpleStorage


def main():
    account = accounts[0]  # this will give my account address (random)
    # this will deploy my contract to the local block chain network
    simple_storage = SimpleStorage.deploy({"from": account})
    # This call retrieve view function that is defined in simplestorage contract
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(
        15, {"from": account})  # This will call store function
    transaction.wait(1)  # wait for the 1 block transaction to complete
    updated_stored_value = simple_storage.retrieve()  # again call retrieve function
    print(updated_stored_value)
