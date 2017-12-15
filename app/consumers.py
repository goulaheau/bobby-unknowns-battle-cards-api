from channels import Group


def ws_connect(message):
    message.reply_channel.send({'accept': True})
    Group('users').add(message.reply_channel)


def ws_receive(message):
    print(message.content['text'])
    Group('users').send({
        'text': message.content['text']
    })


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)
