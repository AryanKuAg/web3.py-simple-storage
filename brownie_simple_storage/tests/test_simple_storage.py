from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected_value = 0
    # assert
    assert starting_value == expected_value


def test_updating_function():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 101
    simple_storage.store(expected, {"from": account})
    # assert
    assert expected == simple_storage.retrieve() 
