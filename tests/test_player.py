import player

def test_get_all_in_amount():
    playerDetails = {
        'name': 'Game On',
        'holt_cards': [],
        'stack': 500
    }

    assert player.get_all_in_amount(playerDetails) == 500