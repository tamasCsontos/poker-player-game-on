import player


def test_get_own_player():
    own_player = {
        'name': 'Game On',
        'holt_cards': [],
        'stack': 500
    }

    players = [
        {
            'name': 'Game On',
            'holt_cards': [],
            'stack': 500
        },
        {
            'name': 'Other On',
            'holt_cards': [],
            'stack': 860
        }
    ]

    assert player.get_own_player(players) == own_player
