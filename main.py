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

    if wetter.get("cod") != "404":
        hauptteil = wetter.get("main", {})
        aktuelle_temperatur = hauptteil.get("temp")
        aktueller_druck = hauptteil.get("pressure")
        aktuelle_feuchtigkeit = hauptteil.get("humidity")
        wetterzustand = wetter.get("weather", [{}])[0]
        wetterbeschreibung = wetterzustand.get("description")

        if aktuelle_temperatur and aktueller_druck and aktuelle_feuchtigkeit:
            print(f"Temperatur (in Celsius): {aktuelle_temperatur}\n"
                  f"Luftdruck (in hPa): {aktueller_druck}\n"
                  f"Feuchtigkeit (in Prozent): {aktuelle_feuchtigkeit}\n"
                  f"Beschreibung: {wetterbeschreibung}")
        else:
            print("Wetterdaten nicht verfügbar.")
    else:
        print("Stadt nicht gefunden.")

if __name__ == "__main__":
    haupt()
