import card


def get_own_player(players):
    print "ASASSAS" + players[0]
    for player in players:
        if player['name'] == 'Game On':
            print "sadasdas" + player
            return player


def get_all_in_amount(player):
    return int(player.stack)


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        own_player = get_own_player(game_state['players'])
        hole_cards = own_player['hole_cards']
        print own_player

        ## if card.are_card_ranks_equal(hole_cards) or card.is_card_with_rank(hole_cards, "A"):
        #   return get_all_in_amount(own_player)

        return 1000

    def showdown(self, game_state):
        pass
