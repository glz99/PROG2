import json

#jsondatei öffnen (Liste)
def opendatei1():
    try:
        with open("summe.json") as open_file:
            datensumme = json.load(open_file)
    except FileNotFoundError:
        datensumme = []

    return datensumme


#Daten aus Formularfeld speichern

def storedatei1(datensumme):
    with open("summe.json", "w") as open_file:
        # datei_inhalt und open_file ist von oben (def opendatei), indent=2 -> untereinander nicht nebeneinander
        json.dump(datensumme, open_file, indent=2)
