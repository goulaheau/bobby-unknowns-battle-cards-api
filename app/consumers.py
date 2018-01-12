from channels import Group

from app.models import Game, User


def ws_connect(message, game_id, user_id):
    message.reply_channel.send({'accept': True})
    Group(game_id).add(message.reply_channel)


def ws_receive(message, game_id, user_id):
    print(message.content['text'])
    Group(game_id).send({
        'text': message.content['text']
    })


def ws_disconnect(message, game_id, user_id):
    Group(game_id).discard(message.reply_channel)
