import card

SAMPLE_CARDS = [
    {
        'rank': 'A',
        'suit': 'clubs'
    },
    {
        'rank': '1',
        'suit': 'diamonds'
    },
    {
        'rank': 'K',
        'suit': 'diamonds'
    },
    {
        'rank': '9',
        'suit': 'spades'
    }
]


def test_is_card_with_rank():
    assert card.is_card_with_rank(SAMPLE_CARDS, 'A') is True
    assert card.is_card_with_rank(SAMPLE_CARDS, '10') is False


def test_are_card_ranks_equal():
    equal_cards = [
        {
            'rank': 'K',
            'suit': 'diamonds'
        },
        {
            'rank': 'K',
            'suit': 'spades'
        }
    ]

    assert card.are_card_ranks_equal(SAMPLE_CARDS) is False
    assert card.are_card_ranks_equal(equal_cards) is True
