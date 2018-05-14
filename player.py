import card


def get_own_player(players):
    for player in players:
        if player['name'] == 'Game On':
            return player


def get_all_in_amount(player):
    return int(player['stack'])


class Player:
    VERSION = "0.02b"

    def betRequest(self, game_state):
        own_player = get_own_player(game_state['players'])
        hole_cards = own_player['hole_cards']

        if card.are_card_ranks_equal(hole_cards):
                if card.is_card_under_ten(hole_cards):
                    return int(own_player['big_blind'])*10
                else:
                    return int(own_player['big_blind'])*2
        elif card.is_card_with_rank(hole_cards, "A"):
            if card.is_card_under_ten(hole_cards):
                return int(own_player['big_blind']) * 10
            else:
                return int(own_player['big_blind']) * 2
        return 0

    def showdown(self, game_state):
        pass
