import card

def am_i_big_blind(game_state):
    #Please test if this gives back if we are the bigblind
    if game_state['dealer'] == 4:
        return True
    return False


def am_i_small_blind(game_state):
    if game_state['dealer'] == 5:
        return True
    return False


def get_own_player(players):
    for player in players:
        if player['name'] == 'Game On':
            return player


def get_all_in_amount(player):
    return int(player['stack'])


class Player:
    VERSION = "0.1b1223"

    def betRequest(self, game_state):
        own_player = get_own_player(game_state['players'])
        hole_cards = own_player['hole_cards']
        if int(game_state['round']) == 1:
            if card.are_card_ranks_equal(hole_cards):
                    if card.is_card_under_ten(hole_cards):
                        return int(game_state['big_blind'])*10
                    else:
                        return int(game_state['big_blind'])*2
            elif card.is_card_with_rank(hole_cards, "A"):
                if card.is_card_under_ten(hole_cards):
                    return int(game_state['big_blind'])*10
                else:
                    return int(game_state['big_blind'])*2
        elif int(game_state['round']) != 1:
            if card.are_card_ranks_equal(hole_cards):
                    if card.is_card_under_ten(hole_cards):
                        return int(game_state['current_buy_in']) * 2
                    else:
                        return int(game_state['current_buy_in'])
            elif card.is_card_with_rank(hole_cards, "A"):
                if card.is_card_under_ten(hole_cards):
                    return int(game_state['current_buy_in']) * 2
                else:
                    return int(game_state['current_buy_in'])
        elif am_i_small_blind(game_state):
            if int(game_state['current_buy_in']) < int(game_state['big_blind'])*2:
                return int(game_state['current_buy_in'])
        elif am_i_big_blind(game_state):
            if int(game_state['current_buy_in']) < int(game_state['big_blind'])*3:
                return int(game_state['current_buy_in'])
        return 0

    def showdown(self, game_state):
        pass
