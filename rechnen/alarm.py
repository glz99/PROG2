import json

#mit dieser Funktion kann in jeder anderen Datei in der die neusten Daten aufgerufen werden (mit from main import get_data)
def get_data():
    with open('daten2.json', 'r') as file:
        obj = json.load(file)
    return obj

def rechnen():
    obj = get_data() #Daten von der get_data Funktion werden gebraucht
    global summeglas
    summeglas = 0
    global summepet
    summepet = 0
    global summekarton
    summekarton = 0

    for element in obj:
        #hier kommt die Berechnung wie viel von Pet, Glas oder Karton bereits in der Liste sind

        if element["Was"] == "Glas":
            summeglas = summeglas + float(element["Anzahl"])


        if element["Was"] == "Pet":
           summepet= summepet +float(element["Anzahl"])


        if element["Was"] == "Karton":
            summekarton = summekarton + float(element["Anzahl"])

    return "Aktuelle Anzahl Glas:" + str(summeglas) + " Stück Aktuelle Anzahl Pet: " + str(summepet) + " Stück Aktuelle Anzahl Karton: " + str(summekarton) + " Gramm"

#mit der Anzahl von oben werden weitere Funktionen erstellt, wann es die Meldung machen soll, dass
#entsotgt werden muss
def rechnen1():

    if summeglas > 20:
        return "Glas muss entsorgt werden!"

    else:
        return "Es hat noch Platz im Glasbehälter!"

def rechnen2():
    if summepet > 20:
        return "Pet muss entsorgt werden!"

    else:
        return "Es hat noch Platz im Petbehälter!"

def rechnen3():
    if summekarton > 500:
        return "Karton muss entsorgt werden!"

    else:
        return "Es hat noch Platz im Kartonbehälter!"





