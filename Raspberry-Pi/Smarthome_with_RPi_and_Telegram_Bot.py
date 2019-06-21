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
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.output(37, 0)
GPIO.output(38, 0)
GPIO.output(40, 0)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
    
    # Menyalakan channel relay 1
    if command == 'nyala1':
       bot.sendMessage(chat_id, on(37))
       
    # Menyalakan channel relay 2
    elif command == 'nyala2':
       bot.sendMessage(chat_id, on(38))
       
    # Menyalakan channel relay 3
    elif command == 'nyala3':
       bot.sendMessage(chat_id, on(40))
    
    # Memadamkan channel relay 1
    elif command =='padam1':
       bot.sendMessage(chat_id, off(37))

    # Memadamkan channel relay 2
    elif command =='padam2':
       bot.sendMessage(chat_id, off(38))
       
    # Memadamkan channel relay 3
    elif command =='padam3':
       bot.sendMessage(chat_id, off(40))
       
bot = telepot.Bot('Bot Token') # Ganti 'Bot Token' dengan kode token anda, misal bot = telepot.Bot('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9')
bot.message_loop(handle)
print '=================================================='
print 'Selamat datang di demo Smarthome Telegram DigiWare'
print '=================================================='
print ' '
print '     + kirim pesan nyala1 untuk mengaktifkan relay channel 1"
print '     + kirim pesan nyala2 untuk mengaktifkan relay channel 2"
print '     + kirim pesan nyala3 untuk mengaktifkan relay channel 3"
print '     + kirim pesan padam1 untuk menonaktifkan relay channel 1"
print '     + kirim pesan padam2 untuk menonaktifkan relay channel 2"
print '     + kirim pesan padam3 untuk menonaktifkan relay channel 3"
print ' '
print 'Siap menerima pesan Anda...'

while 1:
     time.sleep(10)
