from card import *
import sys
from game import *

def get_all_in_amount(player):
    return int(player['stack'])


class Player:
    VERSION = "0.1b1223"

    def betRequest(self, game_state):
        try:
            game_state = GameState(game_state)
            cards_in_hand = game_state.own_player.hole_cards

            if int(game_state.round) == 1:
                if are_card_ranks_equal(cards_in_hand):
                        if is_there_card_under_ten(cards_in_hand):
                            return game_state.big_blind * 10
                        else:
                            return game_state.big_blind * 2

                elif is_card_with_rank(cards_in_hand, CardDetails.Ranks.RANK_ACE):
                    if is_there_card_under_ten(cards_in_hand):
                        return game_state.big_blind * 10
                    else:
                        return game_state.big_blind * 2
            else:
                if is_there_card_under_ten(cards_in_hand):
                    if is_there_card_under_ten(cards_in_hand):
                        return game_state.current_buy_in * 2
                    else:
                        return game_state.current_buy_in

                elif is_card_with_rank(cards_in_hand, CardDetails.Ranks.RANK_ACE):
                    if is_there_card_under_ten(cards_in_hand):
                        return game_state.current_buy_in * 2
                    else:
                        return game_state.current_buy_in

        except:
            print "Unexpected error: ", sys.exc_info()[0]

        return 0

    def showdown(self, game_state):
        pass
