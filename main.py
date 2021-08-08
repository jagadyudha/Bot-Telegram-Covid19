import json
import urllib.request
import requests
import difflib

def telesend(bot_chatID, bot_message):
    url = "https://api.telegram.org/bot[YOURTOKEN]/sendMessage?chat_id=" + \
        bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    requests.get(url)

def provinsi(name):
    url = 'https://indonesia-covid-19.mathdro.id/api/provinsi/'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    data = (result['data'])
    lower = name.lower()
    db = (difflib.get_close_matches(lower, ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Kalimantan Timur', 'Sulawesi Selatan', 'Banten', 'Bali', 'Riau', 'Daerah Istimewa Yogyakarta', 'Sumatera Barat', 'Kalimantan Selatan', 'Sumatera Utara','Papua', 'Sumatera Selatan', 'Kalimantan Tengah', 'Sulawesi Utara', 'Nusa Tenggara Timur', 'Bangka Belitung', 'Sulawesi Tengah', 'Kalimantan Utara', 'Lampung', 'Aceh', 'Sulawesi Tenggara', 'Nusa Tenggara Barat', 'Kepulauan Riau', 'Maluku', 'Kalimantan Barat', 'Jambi', 'Bengkulu', 'Sulawesi Barat', 'Gorontalo', 'Maluku Utara', 'Papua Barat']))
    datastr = ''.join(db[0])

    for i in data:
        if datastr == i['provinsi']:
            return ("Berikut adalah data terkini terkait covid-19 di " + i['provinsi'] + "\n\n" +  "🔴 Jumlah Positif : " + str(i['kasusPosi'])) + "\n" + "🔴 Jumlah Sembuh : " + str(i['kasusSemb']) + "\n" + "🔴 Jumlah Meninggal : " + str(i['kasusMeni']) + "\n"

def teleget():
    offset = [0]
    while True:
        try:
            url = 'https://api.telegram.org/bot[YOURTOKEN]/getUpdates?offset=' + \
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

            if provinsi(command_chat) and (offset[0] != intid_update):
                data = (provinsi(command_chat))
                telesend(intid_telegram, data)
                offset[0] = intid_update
            
            if command_chat and (offset[0] != intid_update):
                data = "Ketik Provinsi Kalian"
                telesend(intid_telegram, data)
                offset[0] = intid_update


        except Exception:
            pass


teleget()