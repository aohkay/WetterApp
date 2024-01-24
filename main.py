import requests

def hava_durumu_getir(sehir):
    api_key = "BURAYA_API_ANAHTARINIZI_YAZIN"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    tam_url = base_url + "appid=" + api_key + "&q=" + sehir + "&lang=de" + "&units=metric"
    yanit = requests.get(tam_url)
    return yanit.json()

def main():
    sehir = input("Bitte geben Sie den Namen einer Stadt ein: ")
    hava_durumu = hava_durumu_getir(sehir)

    if hava_durumu["cod"] != "404":
        y = hava_durumu["main"]
        mevcut_sicaklik = y["temp"]
        mevcut_basinc = y["pressure"]
        mevcut_nem = y["humidity"]
        z = hava_durumu["weather"]
        hava_durumu_aciklama = z[0]["description"]

        print(f"Temperatur (in Celsius): {mevcut_sicaklik}\n"
              f"Luftdruck (in hPa): {mevcut_basinc}\n"
              f"Feuchtigkeit (in Prozent): {mevcut_nem}\n"
              f"Beschreibung: {hava_durumu_aciklama}")
    else:
        print("Stadt nicht gefunden.")

if __name__ == "__main__":
    main()
