"""
def co2_berechnen(anzahl1, anzahl2, anzahl3): #Glasflasche 3.3 dl = 200gramm
    #Jede Tonne recyceltes Glas spart 670 kg CO2 ein.somit spart jedes Kilogramm Glas670 Gramm  c02
    # -> jede Flasche somit 134 Gramm c02
    ersparnisglas = anzahl1 * 134
    ersparnispet = anzahl2 * 236
    ersparniskaron = anzahl3 * 2
    gesamt = ersparniskaron + ersparnisglas + ersparnispet
    return (gesamt)
"""
import json

#mit dieser Funktion kann in jeder anderen Datei in der die neusten Daten aufgerufen werden (mit from main import get_data)
def get_data():
    with open('daten2.json', 'r') as file:
        obj = json.load(file)
    return obj

def co2_sparen():
    obj=get_data()

    summe_gesamt=0

    for element in obj:
        if element["Was"] == "Glas":
            summe1= float(element["Anzahl"])* 134
        else:
            summe1=0

        if element["Was"] == "Pet":
            summe2=float(element["Anzahl"]) * 236
        else:
            summe2=0

        if element["Was"] == "Karton":
            summe3 = float(element["Anzahl"]) * 2
        else:
            summe3=0

        summe_gesamt = summe_gesamt + summe1 + summe2 + summe3

    return (summe_gesamt)




"""
def co2_berechnen1(anzahl1): #Pet 5 dl = 100gramm
    #Jedes Kilogramm recyceltes Plastik spart 2.38kg kg CO2 ein.somit spart jede 100 Gramm Pet 238 Gramm  c02
    ersparnis1 = anzahl1 * 236
    return (ersparnis1)


def co2_berechnen2(anzahl3): #Karton 100 Gramm
    #Jede Tonne  recyceltes Karton spart 2 Tonnen CO2 ein.somit spart jede 1 Gramm Karton 2 Gramm  c02
    ersparnis2 = anzahl3 * 200
    return (ersparnis2)


def gesamt_co2():
    gesamt=co2_berechnen() + co2_berechnen1() + co2_berechnen2()
    return (gesamt)
"""