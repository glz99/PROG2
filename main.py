import json

from plotly.offline import plot
import plotly.express as px
from daten1 import opendatei1, storedatei1
from flask import Flask
from flask import render_template
from flask import request

from daten import opendatei, storedatei
from rechnen.alarm import form1
from rechnen.alarm import rechnen
from rechnen.alarm import rechnen1
from rechnen.alarm import rechnen2
from rechnen.alarm import rechnen3
from rechnen.co2 import co2_sparen

app = Flask("Daten")


app = Flask("__name__")

"""Hauptseite"""
@app.route("/")
def index():
    alarm = rechnen() #diese Funktionen der anderen Datei erhalten hier Namen (alarm, alarm1 usw.)
    alarm1 = rechnen1()
    alarm2 = rechnen2()
    alarm3 = rechnen3()
    #es soll die drei Funktionen returnen, bei welchen die Rechungen zur Entsorgung gemacht wurden
    return render_template("index.html", alarm=alarm, alarm1=alarm1, alarm2=alarm2, alarm3=alarm3)


"""Formularfeld"""
@app.route("/form", methods=["get", "post"])
def form():

    if request.method.lower() == "get": #method get, post (Formularfelder) Daten werden abgeholt und dann weiter
        #verarbeitet
        return render_template("formular.html")
    if request.method.lower() == "post":



        a=request.form.get("Datum")  # Verknüpfung zu json
        b=request.form.get("Was")   #Verknüpfung zu json
        c=request.form.get("Masseinheit") #Verknüpfung zu json
        d=request.form.get("Anzahl") #Verknüpfung zu json
        meine_sammlung = {"Datum": a, 'Was': b, "Masseinheit": c,  "Anzahl": d}
        #request holt Daten aus Formular und tut Sie in den Dictionary "meine_sammlung. Dann speichert es diese Daten
        #in die json datei

        #summe.json
        data=opendatei1()  # Datei öffnen von der daten1.py
        data.clear() #daten clearen bevor Daten dazugefügt werden, um immer die aktuellste Anzahl zu haben
        summe = form1()  # kommt von alarm.py (Funktion welche summen ausgibt)
        data.append(summe)  # Daten zur json Datei (summe.json) hinzufügen
        storedatei1(data)  # Eingaben von summe.json speichern



        #summe.json
        data=opendatei() #Datei öffnen von der Daten.py
        data.append(meine_sammlung) #Daten zur json Datei hinzufügen
        storedatei(data)  #Eingaben von daten2.json speichern





        return render_template("formular.html", name="meine_sammlung") #meine Sammlung ist daten2.json




"""Auswertungseite"""

@app.route ("/auswertung", methods=["POST", "GET"])
def auswerten():
    if request.method.lower() == "get": #get post (Formular) für den Filter button auf der HTML seite
        return render_template("auswertung.html")
    if request.method.lower() == "post":
        Was = request.form.get("Was") #refrenziert mit der unteren if Funktion
    auswertungs_liste = [] #list erstellen leer für die HTML seite
    data = opendatei()  #Json Datei öffnen
    for element in data:
        if element["Was"] == Was: #Element Was ist Pet, Glas oder Karton aus json liste ansprechen
            auswertungs_liste.append([element["Datum"],element["Was"], element["Masseinheit"], element["Anzahl"]])
            # für jedes Element in der jason Datei soll es nun jeweils
            # die Elemente zu der  auswertungs_liste dazutun
    return render_template("auswertung.html", liste=auswertungs_liste) #ausgabe des Htmls und der auswertungs_liste



"""Alarm"""
@app.route ("/entsorgungsalarm")
def entsorgungsalarm():
    alarm = rechnen()  #diese Funktionen der anderen Datei erhalten hier Namen (alarn, alarm1 usw.)
    alarm1 = rechnen1()
    alarm2 = rechnen2()
    alarm3 = rechnen3()
    # es soll die drei Funktionen returnen, bei welchen die Rechnungen zur Entsorgung gemacht wurden
    return render_template("entsorgungsalarm.html", alarm=alarm, alarm1=alarm1, alarm2=alarm2, alarm3 = alarm3)

"""Seite mit co2"""
@app.route ("/co2")
def c02():
    co2 = co2_sparen() #die Funktion der anderen Datei erhält hier einen Namen (co2 usw. und wird returned)
    return render_template("co2.html", co2=co2)

"""Seite mit statistik"""
@app.route ("/statistik")

def hello_auswertung():
    div = viz()

    try:
        with open("summe.json") as open_file:
            data = json.load(open_file)
    except FileNotFoundError:
        data = {}

    return render_template('statistik.html', viz_div=div)


def get_data():

    sorte = ["Glas", "Pet", "Karton"]
    anzahl = []
    try:
        with open("summe.json") as open_file:
            data = json.load(open_file)
    except FileNotFoundError:
        data = {}

    anzahl.append(data[0][0])
    anzahl.append(data[0][1])
    anzahl.append(data[0][2])



    return sorte, anzahl


def viz():
    sorte, anzahl = get_data()
    fig = px.bar(x=sorte, y=anzahl)
    fig.update_layout(
        xaxis_title="Sorte",
        yaxis_title="Anzahl",
    )

    div = plot(fig, output_type="div")

    return div


"""Wenn der Name der Datei mit Main übereinstimmt, führt es die App auf dem Port 5000 aus"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)

#bei der Ausführung von FLASK wird der port 5000 verwendet. FLASK ist mit __name__ definiert
