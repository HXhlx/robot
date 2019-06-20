from pprint import pprint
from cqhttp import CQHttp
import random

bot = CQHttp(api_root="http://127.0.0.1:5700")


@bot.on_message('private')
def handle_msg(ctx):
    pprint(ctx)
    msg = ctx['message']
    echo_cmd = 'echo'
    if msg.startswith(echo_cmd + ' '):
        bot.send(ctx, msg[len(echo_cmd):].lstrip())
    elif msg == '喵一个':
        bot.send(ctx, '喵')
    elif msg == '随机数':
        bot.send(ctx, str(random.randint(0, 100)))


bot.run('127.0.0.1', 8080)
