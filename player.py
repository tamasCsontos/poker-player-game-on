from card import *
import sys
from game import *

def am_i_big_blind_or_small_blind(game_state):
    #Please test if this gives back if we are the bigblind
    if game_state.dealer == 4 or game_state.dealer == 5:
        return True
    return False


def get_count_of_active_players(game_state):
    count = 0
    for player in game_state.players:
        if player.status == PlayerDetails.Statuses.STATUS_ACTIVE or player.status == PlayerDetails.Statuses.STATUS_FOLDED:
            count += 1

    return count


def is_there_card_in_community_cards(game_state):
    b1 = is_card_with_rank(game_state.community_cards, game_state.own_player.hole_cards[0].rank)
    b2 = is_card_with_rank(game_state.community_cards, game_state.own_player.hole_cards[1].rank)
    return b1 or b2


class Player:
    VERSION = "2.01002b beta"

    def betRequest(self, game_state):
        try:
            game_state = GameState(game_state)
            cards_in_hand = game_state.own_player.hole_cards

            if len(game_state.community_cards) and game_state.community_cards is not None:
                if is_there_card_in_community_cards(game_state):
                    return game_state.current_buy_in * 3

            if get_count_of_active_players(game_state) > 2:
                if game_state.pot <= game_state.big_blind * 4:
                    if are_card_ranks_equal(cards_in_hand):
                        if is_there_card_under_ten(cards_in_hand):
                            return game_state.big_blind * 10
                        else:
                            return game_state.big_blind * 2

                    elif is_card_with_rank(cards_in_hand, CardDetails.Ranks.RANK_ACE):
                        return game_state.big_blind

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
                        return game_state.current_buy_in
                    elif am_i_big_blind_or_small_blind(game_state):
                        if game_state.current_buy_in < game_state.big_blind * 3:
                            return game_state.current_buy_in
            else:
                if is_card_with_rank(cards_in_hand, CardDetails.Ranks.RANK_ACE) or are_card_ranks_equal(cards_in_hand):
                    return game_state.own_player.stack

        except:
            print "Unexpected error: "

        return 0

    def showdown(self, game_state):
        pass
