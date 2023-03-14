import requests
import json
import time





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


#primeira consulta para saber o valor do withdraw e poder monitorar a mudança
r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
json_data = r.json()
initial_bsc_withdraw = json_data[1]['is_withdraw_disabled']

while True:
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    json_data = r.json()

    bsc_withdraw_atual = json_data[1]['is_withdraw_disabled']

    if bsc_withdraw_atual != initial_bsc_withdraw:
        hora_atual = time.localtime()
        hora_formatada = time.strftime("%H:%M:%S", hora_atual)

        if bsc_withdraw_atual == 1:
            print("BSC DESABILITADO - " + hora_formatada)
            message = "SAQUE BLOQUEADO NA REDE BSC - " + hora_formatada + " @ReachNextSupport"
            post_message_telegram(message,"-1001753388157")


        else:
            print("BSC HABILITADO - " + hora_formatada)
            titulo = 'SAQUE SDAO BSC NA GATE'
            mensagem = 'LIBERADO!'
            message = "SAQUE LIBERADO NA REDE BSC - " + hora_formatada + " @ReachNextSupport"
            post_message_telegram(message,"-1001753388157")

        initial_bsc_withdraw = bsc_withdraw_atual
    print("Nothing have changed")
    time.sleep(5)





