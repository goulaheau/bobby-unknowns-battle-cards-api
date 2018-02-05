import random
import  math

from app.models import Card, CardValue
from app.serializers import CardSerializer


def action_switcher(game, user, action, payload):
    switcher = {
        'init': action_init,
        'play_card': action_play_card,
        'attack': action_attack,
        'end_turn': action_end_turn,
    }

    func = switcher.get(action)

    return func(game, user, payload)


def action_init(game, user, payload):
    game.turn = 1
    game.owner_health = 30
    game.opponent_health = 30

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
        'payload': {
            'success': True
        }
    }


def action_play_card(game, user, payload):
    success = True
    card_to_play = None

    if user.id != game.player_turn.id:
        success = False
    else:
        if user.id == game.owner.id:
            try:
                card_to_play = game.owner_hand_cards.get(
                    id=payload['card_to_play']
                )
            except Card.DoesNotExist:
                success = False

            if success:
                if card_to_play.cost > game.owner_mana:
                    success = False
                else:
                    game.owner_mana -= card_to_play.cost
                    game.owner_hand_cards.remove(card_to_play)

                    card_value = CardValue(
                        user=user,
                        card=card_to_play,
                        strength=card_to_play.strength,
                        health=card_to_play.health,
                        can_attack=False,
                    )
                    card_value.save()

                    game.owner_board_card_values.add(card_value)
                    game.save()
        else:
            try:
                card_to_play = game.opponent_hand_cards.get(
                    id=payload['card_to_play']
                )
            except Card.DoesNotExist:
                success = False

            if success:
                if card_to_play.cost > game.opponent_mana:
                    success = False
                else:
                    game.opponent_mana -= card_to_play.cost
                    game.opponent_hand_cards.remove(card_to_play)

                    card_value = CardValue(
                        user=user,
                        card=card_to_play,
                        strength=card_to_play.strength,
                        health=card_to_play.health,
                        can_attack=False
                    )
                    card_value.save()

                    game.opponent_board_card_values.add(card_value)
                    game.save()

    return {
        'action': 'play_card',
        'payload': {
            'emitter': user.id,
            'success': success,
            'card_to_play': '' if success is False else card_to_play.id,
        }
    }


def action_attack(game, user, payload):
    success = True
    attacker = None
    victim = None

    if user.id != game.player_turn.id:
        success = False
    else:
        # Attack User
        if payload['victim'] == 'user':
            if user.id == game.owner.id:
                try:
                    attacker = game.owner_board_card_values.get(
                        card=payload['attacker'],
                        user=game.owner.id
                    )
                except CardValue.DoesNotExist:
                    success = False
                if success:
                    if attacker.can_attack is False:
                        success = False
                    else:
                        attacker.can_attack = False
                        attacker.save()

                        game.opponent_health -= attacker.strength
                        game.save()
            else:
                try:
                    attacker = game.opponent_board_card_values.get(
                        card=payload['attacker'],
                        user=game.opponent.id
                    )
                except CardValue.DoesNotExist:
                    success = False
                if success:
                    if attacker.can_attack is False:
                        success = False
                    else:
                        attacker.can_attack = False
                        attacker.save()

                        game.owner_health -= attacker.strength
                        game.save()
        # Attack Card
        else:
            if user.id == game.owner.id:
                try:
                    attacker = game.owner_board_card_values.get(
                        card=payload['attacker'],
                        user=game.owner.id
                    )
                    victim = game.opponent_board_card_values.get(
                        card=payload['victim'],
                        user=game.opponent.id
                    )
                except CardValue.DoesNotExist:
                    success = False

                if success:
                    if attacker.can_attack is False:
                        success = False
                    else:
                        victim.health -= attacker.strength
                        attacker.health -= victim.strength

                        if attacker.health <= 0:
                            game.owner_board_card_values.remove(attacker)
                            game.owner_graveyard_cards.add(attacker.card)
                            game.save()
                            attacker.delete()
                        else:
                            attacker.can_attack = False
                            attacker.save()
                        if victim.health <= 0:
                            game.opponent_board_card_values.remove(victim)
                            game.opponent_graveyard_cards.add(victim.card)
                            game.save()
                            victim.delete()
                        else:
                            victim.save()
            else:
                try:
                    attacker = game.opponent_board_card_values.get(
                        card=payload['attacker'],
                        user=game.opponent.id,
                    )
                    victim = game.owner_board_card_values.get(
                        card=payload['victim'],
                        user=game.owner.id,
                    )
                except CardValue.DoesNotExist:
                    success = False

                if success:
                    if attacker.can_attack is False:
                        success = False
                    else:
                        victim.health -= attacker.strength
                        attacker.health -= victim.strength

                        if attacker.health <= 0:
                            game.opponent_board_card_values.remove(attacker)
                            game.opponent_graveyard_cards.add(attacker.card)
                            game.save()
                            attacker.delete()
                        else:
                            attacker.can_attack = False
                            attacker.save()
                        if victim.health <= 0:
                            game.owner_board_card_values.remove(victim)
                            game.owner_graveyard_cards.add(victim.card)
                            game.save()
                            victim.delete()
                        else:
                            victim.save()

    return {
        'action': 'attack',
        'payload': {
            'emitter': user.id,
            'success': success,
            'attacker': payload['attacker'],
            'victim': payload['victim'],
        }
    }


def action_end_turn(game, user, payload):
    success = True
    card_draw = None

    if user.id != game.player_turn.id:
        success = False
    else:
        game.turn += 1
        if user.id == game.owner.id:
            game.player_turn = game.opponent
            game.opponent_mana = math.ceil(game.turn / 2)

            card_values = game.opponent_board_card_values.all()
            for card_value in card_values:
                card_value.can_attack = True
                card_value.save()

            card_draw = draw_card(
                game.opponent_deck_cards,
                game.opponent_hand_cards
            )
        else:
            game.player_turn = game.owner
            game.owner_mana = math.ceil(game.turn / 2)

            card_values = game.owner_board_card_values.all()
            for card_value in card_values:
                card_value.can_attack = True
                card_value.save()

            card_draw = draw_card(
                game.owner_deck_cards,
                game.owner_hand_cards
            )
        game.save()

    return {
        'action': 'end_turn',
        'payload': {
            'emitter': user.id,
            'success': success,
            'card_draw': '' if success is False else CardSerializer(card_draw).data,
        }
    }


def draw_card(deck_cards, hand_cards):
    card_to_draw = random.randint(0, len(deck_cards.all()) - 1)
    card_to_draw = deck_cards.all()[card_to_draw]

    hand_cards.add(card_to_draw)
    deck_cards.remove(card_to_draw)

    return card_to_draw
