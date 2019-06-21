import time, datetime

import RPi.GPIO as GPIO

import telepot

from telepot.loop import MessageLoop

relay = 37
now = datetime.datetime.now()

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

 #LED

GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, 0) #Off initially

def action(msg):

    chat_id = msg['chat']['id']

    command = msg['text']

 

    print 'Received: %s' % command

 

    if 'on' in command:

        message = "Turned on "

        if 'relay' in command:

            message = message + "led"

            GPIO.output(led, 1)

            telegram_bot.sendMessage (chat_id, message)

 

    if 'off' in command:

        message = "Turned off "

        if 'relay' in command:

            message = message + "led "

            GPIO.output(relay, 0)

            

          

        telegram_bot.sendMessage (chat_id, message)

 

 telegram_bot = telepot.Bot('895169805:AAEXRwriDjwSY4MkBzSP3F-Cyfgkq6QherI')

print (telegram_bot.getMe())

 

MessageLoop(telegram_bot, action).run_as_thread()

print 'Up and Running....'

 

while 1:

    time.sleep(10)
