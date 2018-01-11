from channels import Group

from app.models import Game, User


def ws_connect(message, game_id, user_id):
    user_id = int(user_id)
    game = Game.objects.get(id=game_id)
    already_in_game = False
    user_number = 0
    for user in game.users.all():
        user_number += 1
        if user_id == user.id:
            already_in_game = True
            break
    if not already_in_game and user_number < 2:
        game.users.add(User.objects.get(id=user_id))
        game.save()
    message.reply_channel.send({'accept': True})
    Group(game_id).add(message.reply_channel)


def ws_receive(message, game_id, user_id):
    print(message.content['text'])
    Group(game_id).send({
        'text': message.content['text']
    })


def ws_disconnect(message, game_id, user_id):
    user_id = int(user_id)
    game = Game.objects.get(id=game_id)
    for user in game.users.all():
        if user_id == user.id:
            game.users.remove(User.objects.get(id=user_id))
            game.save()
            break
    Group(game_id).discard(message.reply_channel)
