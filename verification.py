# -*- coding: utf-8 -*-
import requests
import time

token = ''#Telegram Bot Token
chat = '' #Telegram Chat Number
nanopool = 'https://api.nanopool.org/v1/eth/reportedhashrate/ETHWALLET' #Change ETHWALLET for wallet

while True:
	x = requests.get(nanopool)
	if 'false' in x.text: 
		text='Rig+Desconectado'
		r = requests.post('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat+'&text='+text)
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print('['+current_time+'] '+x.text)
	print('['+current_time+'] '+'Back to sleep')
	time.sleep(600)
