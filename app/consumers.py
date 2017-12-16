from channels import Group


def ws_connect(message, game_id):
    print(game_id)
    message.reply_channel.send({'accept': True})
    Group('users').add(message.reply_channel)


def ws_receive(message, game_id):
    print(message.content['text'])
    print(game_id)
    Group('users').send({
        'text': message.content['text']
    })


def ws_disconnect(message, game_id):
    print(game_id)
    Group('users').discard(message.reply_channel)
