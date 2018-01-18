import random


def init(game, payload):
    player_turn = random.randint(0, 1)
    game.player_turn = [game.owner, game.opponent][player_turn]

    if player_turn == 0:
        game.owner_mana = 1
        game.opponent_mana = 0
    else:
        game.owner_mana = 0
        game.opponent_mana = 1

    game.owner_deck_cards.set(game.owner_deck.cards.all())
    game.opponent_deck_cards.set(game.opponent_deck.cards.all())

    game.owner_hand_cards.set([])
    game.opponent_hand_cards.set([])
    for x in range(0, 5):
        draw_card(
            game.owner_deck_cards,
            game.owner_hand_cards
        )

        draw_card(
            game.opponent_deck_cards,
            game.opponent_hand_cards
        )

    game.save()

    return {
        'action': 'init',
        'payload': payload
    }


def draw_card(deck_cards, hand_cards):
    card_to_draw = random.randint(0, len(deck_cards.all()) - 1)

    hand_cards.add(deck_cards.all()[card_to_draw])
    deck_cards.remove(deck_cards.all()[card_to_draw])


def action_switcher(game, action, payload):
    switcher = {
        'init': init,
    }

    func = switcher.get(action)

    return func(game, payload)
