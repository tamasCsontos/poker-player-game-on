import card

def get_own_player(players):
    for player in players:
        if player.name == "Game On":
            return player

def get_all_in_amount(player):
    return player.stack

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        own_player = get_own_player(game_state.players)
        hole_cards = own_player.hole_cards

        if card.are_card_ranks_equal(hole_cards) or card.is_card_with_rank(hole_cards, "A"):
            return get_all_in_amount(own_player)

        return 0

    def showdown(self, game_state):
        pass
