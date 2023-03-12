import requests
import json
import time
#from plyer import notification




host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url = '/wallet/currency_chains'
query_param = 'currency=SDAO'

telegram_bot_id = "5204223531:AAEPh5JVlWNKKQ8f7mchDGig_hI41wzOREo"

def post_message_telegram(message,chat_id):
    URL = 'https://api.telegram.org/bot5204223531:AAEPh5JVlWNKKQ8f7mchDGig_hI41wzOREo/sendMessage?'
    PARAMS = {
        'text': message,
        'chat_id' : chat_id
    }
    r = requests.get(URL, PARAMS)
    return



while True:

	r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
	json_data = r.json()

	bsc_withdraw = json_data[1]['is_withdraw_disabled']

	# Obtém a hora atual do sistema
	hora_atual = time.localtime()

	# Formata a hora atual como uma string no formato hh:mm:ss
	hora_formatada = time.strftime("%H:%M:%S", hora_atual)

	if bsc_withdraw == 1:
		print(f"BSC DESABILITADO - " + hora_formatada, end="\r")
		#message = "SAQUE BLOQUEADO NA REDE BSC  - " + hora_formatada +  " @ReachNextSupport"
		#post_message_telegram(message,"-819860381")


	else:
		print("BSC HABILITADO - " + hora_formatada)
		titulo = 'SAQUE SDAO BSC NA GATE'
		mensagem = 'LIBERADO!'
		#notification.notify(title=titulo, message=mensagem)
		message = "SAQUE LIBERADO NA REDE BSC  - " + hora_formatada +  " @ReachNextSupport"
		post_message_telegram(message,"-819860381")
	time.sleep(15)





