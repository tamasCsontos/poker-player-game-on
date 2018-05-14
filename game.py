def get_json_value(json_data, key):
    if key in json_data.keys():
        return json_data[key]
    return None


class CardDetails:

    class Ranks:
        RANK_1 = '1'
        RANK_2 = '2'
        RANK_3 = '3'
        RANK_4 = '4'
        RANK_5 = '5'
        RANK_6 = '6'
        RANK_7 = '7'
        RANK_8 = '8'
        RANK_9 = '9'
        RANK_10 = '10'
        RANK_ACE = 'A'
        RANK_KING = 'K'
        RANK_QUEEN = 'Q'
        RANK_JACK = 'J'

    class Suits:
        SUIT_CLUBS = 'clubs'
        SUIT_DIAMONDS = 'diamonds'
        SUIT_SPADES = 'spades'
        SUIT_HEARTS = 'hearts'

    def __init__(self, json_data):
        self.rank = get_json_value(json_data, 'rank')
        self.suit = get_json_value(json_data, 'suit')


class PlayerDetails:

    class Statuses:
        STATUS_OUT = 'out'
        STATUS_FOLDED = 'folded'
        STATUS_ACTIVE = 'active'

    def __init__(self, json_data):
        self.id = get_json_value(json_data, 'id')
        self.name = get_json_value(json_data, 'name')
        self.status = get_json_value(json_data, 'status')
        self.version = get_json_value(json_data, 'version')
        self.stack = get_json_value(json_data, 'stack')
        self.bet = get_json_value(json_data, 'bet')
        self.hole_cards = get_json_value(json_data, 'hole_cards')

        if self.hole_cards is not None:
            self.hole_cards = [
                CardDetails(card_json_data) for card_json_data in get_json_value(json_data, 'hole_cards')
            ]
        else:
            self.hole_cards = []



class GameState:
    OWN_PLAYER_NAME = 'Game On'

    def _get_own_player(self):
        for player in self.players:
            if player.name == GameState.OWN_PLAYER_NAME:
                return player

    def __init__(self, json_data):
        self.tournament_id = get_json_value(json_data, 'tournament_id')
        self.game_id = get_json_value(json_data, 'game_id')
        self.round = get_json_value(json_data, 'round')
        self.bet_index = get_json_value(json_data, 'bet_index')
        self.minimum_raise = get_json_value(json_data, 'minimum_raise')
        self.dealer = get_json_value(json_data, 'dealer')
        self.small_blind = get_json_value(json_data, 'small_blind')
        self.big_blind = get_json_value(json_data, 'big_blind')

        if self.big_blind is None:
            self.big_blind = self.small_blind * 2

        self.current_buy_in = get_json_value(json_data, 'current_buy_in')
        self.pot = get_json_value(json_data, 'pot')
        self.orbits = get_json_value(json_data, 'orbits')
        self.in_action = get_json_value(json_data, 'in_action')
        self.community_cards = [
            CardDetails(card_json_data) for card_json_data in get_json_value(json_data, 'community_cards')
        ]
        self.players = [
            PlayerDetails(player_json_data) for player_json_data in get_json_value(json_data, 'players')
        ]
        self.own_player = self._get_own_player()