
def are_card_ranks_equal(cards):
    if len(cards) == 0:
        return False

    card_rank = cards[0]

    for card in cards:
        if card.rank != card_rank:
            return False

    return True


def is_card_with_rank(cards, rank):
    for card in cards:
        if card.rank == rank:
            return True

    return False;