import card


def get_own_player(players):
    for player in players:
        if player['name'] == 'Game On':
            return player


def get_all_in_amount(player):
    return int(player['stack'])


class Player:
    VERSION = "0.01"

    def betRequest(self, game_state):
        own_player = get_own_player(game_state['players'])
        hole_cards = own_player['hole_cards']
        print "asdsadasd: " + own_player

        if card.are_card_ranks_equal(hole_cards) or card.is_card_with_rank(hole_cards, "A"):
            if card.are_card_ranks_equal(hole_cards):
                return get_all_in_amount(own_player)
            else:
                return get_all_in_amount(own_player)/2

        return 0

    def showdown(self, game_state):
        pass
