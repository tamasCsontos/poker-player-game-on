from card import *
import sys
from game import *

def am_i_big_blind_or_small_blind(game_state):
    #Please test if this gives back if we are the bigblind
    if game_state.dealer == 4 or game_state.dealer == 5:
        return True
    return False


def get_all_in_amount(player):
    return player['stack']


class Player:
    VERSION = "1.01b"

    def betRequest(self, game_state):
        try:
            game_state = GameState(game_state)
            cards_in_hand = game_state.own_player.hole_cards

            if game_state.pot <= game_state.big_blind * 4:
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

                elif am_i_big_blind_or_small_blind(game_state):
                    if game_state.current_buy_in < game_state.big_blind * 3:
                        return game_state.current_buy_in

            elif game_state.pot > game_state.big_blind * 4:
                if are_card_ranks_equal(cards_in_hand):
                    if is_there_card_under_ten(cards_in_hand):
                        return game_state.big_blind * 10
                    else:
                        return game_state.current_buy_in * 2
                elif is_card_with_rank(cards_in_hand, CardDetails.Ranks.RANK_ACE):
                    if is_there_card_under_ten(cards_in_hand):
                        return game_state.current_buy_in * 2
                    else:
                        return game_state.current_buy_in
                elif am_i_big_blind_or_small_blind(game_state):
                    if game_state.current_buy_in < game_state.big_blind * 3:
                        return game_state.current_buy_in

        except:
            print "Unexpected error: "

        return 0

    def showdown(self, game_state):
        pass
