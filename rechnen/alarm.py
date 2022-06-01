import json

#mit dieser Funktion kann in jeder anderen Datei in der die neusten Daten aufgerufen werden (mit from main import get_data)
def get_data():
    with open('daten2.json', 'r') as file:
        obj = json.load(file)
    return obj

def rechnen():
    obj = get_data() #Daten von der get_data Funktion werden gebraucht
    summeglas = 0
    summepet = 0
    summekarton = 0

    for element in obj:

        if element["Was"] == "Glas":
            summeglas = summeglas + float(element["Anzahl"])


        if element["Was"] == "Pet":
           summepet= summepet +float(element["Anzahl"])


        if element["Was"] == "Karton":
            summekarton = summekarton + float(element["Anzahl"])

    return (summeglas, summepet, summekarton)

if summeglas > 20:
    print ("Glas muss entsorgt werden")

else:
    print ("Es hat noch Platz")

if summepet > 20:
    print ("Pet muss entsorgt werden")

else:
    print ("Es hat noch Platz")

if summekarton > 20:
    print ("Pet muss entsorgt werden")

else:
    print ("Es hat noch Platz")


