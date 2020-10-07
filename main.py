import json
import urllib.request
import requests


def telesend(bot_chatID, bot_message):
    url = "https://api.telegram.org/bot1317456522:AAHxR2VLuy8eEVB4xLitXmKNEZ1v_gxATuI/sendMessage?chat_id=" + \
        bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    requests.get(url)


def provinsi(idprov):
    url_covid_provinsi = 'https://indonesia-covid-19.mathdro.id/api/provinsi/'
    response_covid_provinsi = urllib.request.urlopen(url_covid_provinsi)
    covid_provinsi = json.loads(response_covid_provinsi.read())

    lol = (covid_provinsi['data'])
    for i in lol:
        if (i['kodeProvi'] == idprov):
            cases = "🔴 Total Kasus : " + str((i["kasusPosi"]))
            deaths = "🔴 Meninggal : " + str((i["kasusMeni"]))
            recovered = "🔴 Sembuh : " + str((i["kasusSemb"]))
            x = (cases + "\n" + deaths + "\n" +
                 recovered + "\n\n")
            return (x)


def teleget():
    offset = [0]

    while True:
        try:
            url_covid = 'https://coronavirus-19-api.herokuapp.com/countries/indonesia'
            response_covid = urllib.request.urlopen(url_covid)
            data_covid = json.loads(response_covid.read())

            url_berita_covid = 'https://dekontaminasi.com/api/id/covid19/news/'
            response_berita_covid = urllib.request.urlopen(url_berita_covid)
            berita_covid = json.loads(response_berita_covid.read())

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

            if (command_chat == 'start' and (offset[0] != intid_update)):
                opening = "Hallo " + first_name.lower() + \
                    ", berikut adalah command yang bisa kalian pakai terkait kasus corona di Indonesia 🚑" + "\n\n\n" + \
                    "/covid  👉🏽 Menampilkan Total kasus covid-19 di Indonesia." + "\n\n" + \
                    "/berita 👉🏽 Menampilkan berita terkait covid-19 di Indonesia." + "\n\n" + \
                    "/berita 👉🏽 Menampilkan berita terkait covid-19 di Indonesia."
                telesend(intid_telegram, opening)
                offset[0] = intid_update

            if (command_chat == '/covid' and (offset[0] != intid_update)):
                opening = "[+] Hallo " + first_name.lower() + \
                    ", berikut adalah perkembangan kasus covid-19 di Indonesia [+]"
                cases = "🔴 Total Kasus : " + str((data_covid["cases"]))
                deaths = "🔴 Meninggal : " + str((data_covid["deaths"]))
                recovered = "🔴 Sembuh : " + str((data_covid["recovered"]))
                active = "🔴 Kasus Aktif : " + str((data_covid["active"]))
                closing = "Tetap waspada dengan jaga jarak, gunakan masker, dan cuci tangan dengan sabun untuk memutus rantai penularan covid-19 ya " + first_name.lower() + \
                    "[+]"
                x = (opening + "\n" + "\n" + cases + "\n" + deaths +
                     "\n" + recovered + "\n" + active + "\n" + "\n" + closing)
                telesend(intid_telegram, x)

                offset[0] = intid_update

            if ((command_chat == '/berita') and (offset[0] != intid_update)):
                title_berita = (berita_covid[0]['title'])
                link_berita = (berita_covid[0]['url'])
                x = (title_berita + "\n" + link_berita)
                telesend(intid_telegram, x)
                offset[0] = intid_update

            if ((command_chat == '/provinsi') and (offset[0] != intid_update)):
                data_prov = "Jakarta\n" + \
                    provinsi(31) + "Jawa Timur\n" + provinsi(35) + "Jawa Tengah\n" + provinsi(33) + "Jawa Barat\n" + provinsi(32) + "Sulawesi Selatan\n" + provinsi(73) + "Kalimantan Selatan\n" + provinsi(32) + "Sumatera Utara\n" + provinsi(12) + "Bali\n" + provinsi(51) + "Kalimantan Timur\n" + provinsi(64) + "Sumatera Selatan\n" + provinsi(16) + "Papua\n" + provinsi(94) + "Banten\n" + provinsi(36) + "Nusa Tenggara Barat\n" + provinsi(52) + "Kalimantan Tengah\n" + provinsi(62) + "Sumatera Barat\n" + provinsi(13) + "Riau\n" + provinsi(14) + "Gorontalo\n" + provinsi(75) + \
                    "Maluku\n" + provinsi(81) + "Aceh\n" + provinsi(11) + "Maluku Utara\n" + provinsi(82) + "Sulawesi Tenggara\n" + provinsi(74) + "Daerah Istimewa Yogyakarta\n" + provinsi(34) + "Kepulauan Riau\n" + provinsi(21) + "Papua Barat\n" + provinsi(91) + "Kalimantan Barat\n" + provinsi(
                        61) + "Lampung\n" + provinsi(18) + "Kalimantan Utara\n" + provinsi(65) + "Sulawesi Barat\n" + provinsi(74) + "Bengkulu\n" + provinsi(17) + "Jambi\n" + provinsi(15) + "Sulawesi Tengah\n" + provinsi(72) + "Nusa Tenggara Timur\n" + provinsi(53) + "Kepulauan Bangka Belitung\n" + provinsi(19)

                telesend(intid_telegram, data_prov)
                offset[0] = intid_update

        except Exception:
            print("asu")


teleget()
