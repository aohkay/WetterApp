import requests

def wetter_abrufen(stadt):
    api_schlussel = "HIER_DEINEN_API_SCHLÜSSEL_EINFÜGEN"
    basis_url = "http://api.openweathermap.org/data/2.5/weather?"
    vollständige_url = basis_url + "appid=" + api_schlussel + "&q=" + stadt + "&lang=de" + "&units=metric"
    antwort = requests.get(vollständige_url)
    return antwort.json()

def haupt():
    stadt = input("Bitte geben Sie den Namen einer Stadt ein: ")
    wetter = wetter_abrufen(stadt)

    if wetter["cod"] != "404":
        hauptteil = wetter["main"]
        aktuelle_temperatur = hauptteil["temp"]
        aktueller_druck = hauptteil["pressure"]
        aktuelle_feuchtigkeit = hauptteil["humidity"]
        wetterzustand = wetter["weather"]
        wetterbeschreibung = wetterzustand[0]["description"]

        print(f"Temperatur (in Celsius): {aktuelle_temperatur}\n"
              f"Luftdruck (in hPa): {aktueller_druck}\n"
              f"Feuchtigkeit (in Prozent): {aktuelle_feuchtigkeit}\n"
              f"Beschreibung: {wetterbeschreibung}")
    else:
        print("Stadt nicht gefunden.")

if __name__ == "__main__":
    haupt()
