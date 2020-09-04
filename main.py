import json
import urllib.request
import requests


def telesend(bot_chatID, bot_message):
    url = "https://api.telegram.org/bot1317456522:AAHxR2VLuy8eEVB4xLitXmKNEZ1v_gxATuI/sendMessage?chat_id=" + \
        bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    requests.get(url)


def teleget():
    offset = [0]

    url_covid = 'https://coronavirus-19-api.herokuapp.com/countries/indonesia'
    response_covid = urllib.request.urlopen(url_covid)
    data_covid = json.loads(response_covid.read())

    while True:
        try:
            url = 'https://api.telegram.org/bot1317456522:AAHxR2VLuy8eEVB4xLitXmKNEZ1v_gxATuI/getUpdates?offset=' + \
                str(offset[0])
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            dict = data['result']

            for obj in dict:

                id_telegram = (obj['message']['from']['id'])
                first_name = (obj['message']['from']['first_name'])
                id_update = (obj['update_id'])

            command_chat = (obj['message']['text'])
            intid_update = (str(id_update))
            intid_telegram = (str(id_telegram))

            if (command_chat == '/covid' and (offset[0] != intid_update)):
                opening = "Hallo " + first_name.lower() + \
                    ", berikut adalah data kasus COVID19 di Indonesia"
                cases = "Total Kasus : " + str((data_covid["cases"]))
                deaths = "Meninggal : " + str((data_covid["deaths"]))
                recovered = "Sembuh : " + str((data_covid["recovered"]))
                active = "Kasus Aktif : " + str((data_covid["active"]))
                closing = "Tetap jaga kesehatan dan patuhi protokol ya " + first_name.lower()

                telesend(intid_telegram, opening)
                telesend(intid_telegram, cases)
                telesend(intid_telegram, deaths)
                telesend(intid_telegram, recovered)
                telesend(intid_telegram, active)
                telesend(intid_telegram, closing)
                offset[0] = intid_update

            if ((command_chat != '/covid') and (offset[0] != intid_update)):
                opening = "Hallo " + first_name.lower() + \
                    ", Ketik /covid atau klik untuk mendapatkan Info terkini terkait COVID19 di Indonesia"
                telesend(intid_telegram, opening)
                offset[0] = intid_update

        except Exception:
            pass


teleget()
