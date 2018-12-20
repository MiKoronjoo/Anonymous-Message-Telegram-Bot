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
                bot.sendMessage(GROUP_ID, '#hashed%d\n\n%s' % (chat_id, msg['text']))  # TODO: hashing chat_id
                bot.sendMessage(chat_id, tnx_msg)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while True:
    sleep(10)
