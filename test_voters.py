from voter import Voter

def test_can_create_voter():
    new_voter = Voter('John Doe', '123 sycamore rd')
    assert new_voter.name == 'John Doe', 'Unexpected name'
    assert new_voter.address == '123 sycamore rd', 'Unexpected address'
    assert new_voter.id == 'johndoe208be15dd00b6108a1b05ad1b0046349', 'Incorrect ID generated'


