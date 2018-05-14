import card
from game import *

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

SAMPLE_CARDS_DETAILS = [CardDetails(card_json) for card_json in SAMPLE_CARDS]


def test_is_card_with_rank():
    assert card.is_card_with_rank(SAMPLE_CARDS_DETAILS, CardDetails.Ranks.RANK_ACE) is True
    assert card.is_card_with_rank(SAMPLE_CARDS_DETAILS, CardDetails.Ranks.RANK_10) is False


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
    equal_cards_details = [CardDetails(card_json) for card_json in equal_cards]

    assert card.are_card_ranks_equal(SAMPLE_CARDS_DETAILS) is False
    assert card.are_card_ranks_equal(equal_cards_details) is True
