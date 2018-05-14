
def are_card_ranks_equal(cards):
    if len(cards) == 0:
        return False

    card_rank = cards[0]['rank']

    for card in cards:
        if card['rank'] != card_rank:
            return False

    return True


def is_card_with_rank(cards, rank):
    for card in cards:
        if card['rank'] == rank:
            return True

    return False


def

def are_card_suit_equal(cards):
    if len(cards) == 0:
        return False

    card_suit = cards[0]['suit']

    for card in cards:
        if card['suit'] != card_suit:
            return False

    return True

def is_card_under_ten(cards):
    for card in cards:
        if card['rank'] < 10:
            return True

    return False
