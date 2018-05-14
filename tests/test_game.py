import game

GAME_STATE_JSON = {
  'tournament_id':'550d1d68cd7bd10003000003',

  'game_id':'550da1cb2d909006e90004b1',

  'round': 0,

  'bet_index': 0,

  'small_blind': 10,


  'current_buy_in': 320,

  'pot': 400,

  'minimum_raise': 240,

  'dealer': 1,

  'orbits': 7,

  'in_action': 1,

  'players': [
      {

          'id': 0,

          'name': 'Albert',

          'status': 'active',

          'version': 'Default random player',

          'stack': 1010,


          'bet': 320
      },
      {
          'id': 1,
          'name': 'Game On',
          'status': 'active',
          'version': 'Default random player',
          'stack': 1590,
          'bet': 80,
          'hole_cards': [

              {
                  'rank': '6',
                  'suit': 'hearts'
              },
              {
                  'rank': 'K',
                  'suit': 'spades'
              }
          ]
      },
      {
          'id': 2,
          'name': 'Chuck',
          'status': 'out',
          'version': 'Default random player',
          'stack': 0,
          'bet': 0
      }
  ],
  'community_cards': [
      {
          'rank': '4',
          'suit': 'spades'
      },
      {
          'rank': 'A',
          'suit': 'hearts'
      },
      {
          'rank': '6',
          'suit': 'clubs'
      }
  ]
}


def test_game_state_details():
    game_state = game.GameState(GAME_STATE_JSON)
    assert game_state.tournament_id == GAME_STATE_JSON['tournament_id']
    assert game_state.game_id == GAME_STATE_JSON['game_id']
    assert game_state.round == GAME_STATE_JSON['round']
    assert game_state.pot == GAME_STATE_JSON['pot']
    assert game_state.orbits == GAME_STATE_JSON['orbits']
    assert game_state.dealer == GAME_STATE_JSON['dealer']
    assert game_state.small_blind == GAME_STATE_JSON['small_blind']
    assert game_state.big_blind == GAME_STATE_JSON['small_blind'] * 2
    assert game_state.minimum_raise == GAME_STATE_JSON['minimum_raise']
    assert game_state.in_action == GAME_STATE_JSON['in_action']
    assert game_state.own_player.id == 1
    assert game_state.own_player.name == "Game On"
