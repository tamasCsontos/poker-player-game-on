import player


def test_get_own_player():
    own_player = {
        'name': 'Game On',
        'holt_cards': [],
        'stack': 500
    }

    players = [
        own_player,
        {
            'name': 'Other On',
            'holt_cards': [],
            'stack': 860
        }
    ]

    assert player.get_own_player(players) == own_player

def test_get_all_in_amount():
    playerDetails = {
        'name': 'Game On',
        'holt_cards': [],
        'stack': 500
    }

    assert player.get_all_in_amount(playerDetails) == 500