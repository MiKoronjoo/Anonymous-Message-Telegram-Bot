import telepot
from telepot.loop import MessageLoop
from config import TOKEN, GROUP_ID
from time import sleep

start_msg = '''
خوش آمدید 🙂
لطفا پیامتان را همینجا بفرستید'''

tnx_msg = '''
ممنون از پیامتون 😊'''


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == u'private':
        if content_type == 'text':
            if msg['text'] == '/start':
                bot.sendMessage(chat_id, start_msg)
            else:
                if 'username' in msg['from']:
                    hashed_id = str(hash('%d%s' % (chat_id, msg['from']['username'])))[::-1]
                else:
                    hashed_id = str(hash(str(chat_id)))[::-1]
                bot.sendMessage(GROUP_ID, '#H%s\n\n%s' % (hashed_id, msg['text']))
                bot.sendMessage(chat_id, tnx_msg)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while True:
    sleep(10)
