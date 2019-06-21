import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
        
# Perintah untuk menggunakan pin board GPIO Raspberry Pi
GPIO.setmode(GPIO.BOARD)

# Pengaturan GPIO 
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
    
    # Menyalakan channel relay 1
    if command == 'nyala1':
       bot.sendMessage(chat_id, on(37))
       print 'CHANNEL 1 AKTIF'
       
    # Menyalakan channel relay 2
    elif command == 'nyala2':
       bot.sendMessage(chat_id, on(38))
       print 'CHANNEL 2 AKTIF'
       
    # Menyalakan channel relay 3
    elif command == 'nyala3':
       bot.sendMessage(chat_id, on(40))
       print 'CHANNEL 3 AKTIF'
    
    # Memadamkan channel relay 1
    elif command =='padam1':
       bot.sendMessage(chat_id, off(37))
       print 'CHANNEL 1 PADAM'

    # Memadamkan channel relay 2
    elif command =='padam2':
       bot.sendMessage(chat_id, off(38))
       print 'CHANNEL 2 PADAM'
       
    # Memadamkan channel relay 3
    elif command =='padam3':
       bot.sendMessage(chat_id, off(40))
        print 'CHANNEL 3 PADAM'
       
bot = telepot.Bot('Bot Token') # Ganti 'Bot Token' dengan kode token anda, misal bot = telepot.Bot('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
