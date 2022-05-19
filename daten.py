#Quelle: Fabian Odoni (demo_snippes)

import json

#jsondatei öffnen (Liste)
def opendatei():
    try:
        with open("daten2.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt =[]

    return datei_inhalt


#Daten aus Formularfeld speichern

def storedatei(datei_inhalt):
    with open("daten2.json", "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=2) #datei_inhalt und open_file ist von oben (def opendatei)









