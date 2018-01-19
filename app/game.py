import random

from app.models import Card, CardValues


def action_init(game, user, payload):
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


def action_play_card(game, user, payload):
    success = True
    card_to_play = Card.objects.get(id=payload['card_to_play'])

    if user.id == game.owner.id:
        try:
            game.owner_hand_cards.get(id=card_to_play.id)
        except Card.DoesNotExist:
            success = False

        if success:
            game.owner_hand_cards.remove(card_to_play)

            card_values = CardValues(
                user=user,
                card=card_to_play,
                strengh=card_to_play.strengh,
                health=card_to_play.health,
            )
            card_values.save()

            game.owner_board_cards.add(card_values)

            game.save()
    else:
        try:
            game.opponent_hand_cards.get(id=card_to_play.id)
        except Card.DoesNotExist:
            success = False

        if success:
            game.opponent_hand_cards.remove(card_to_play)

            card_values = CardValues(
                user=user,
                card=card_to_play,
                strengh=card_to_play.strengh,
                health=card_to_play.health,
            )
            card_values.save()

            game.opponent_board_cards.add(card_values)

            game.save()

    return {
        'action': 'play_card',
        'payload': {
            'emitter': user.id,
            'success': success,
            'card_to_play': card_to_play.id
        }
    }


def draw_card(deck_cards, hand_cards):
    card_to_draw = random.randint(0, len(deck_cards.all()) - 1)

    hand_cards.add(deck_cards.all()[card_to_draw])
    deck_cards.remove(deck_cards.all()[card_to_draw])


def action_switcher(game, user, action, payload):
    switcher = {
        'init': action_init,
        'play_card': action_play_card
    }

    func = switcher.get(action)

    return func(game, user, payload)
