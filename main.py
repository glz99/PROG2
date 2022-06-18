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
@app.route("/", methods=["get", "post"])
def index():
    # diese Funktionen der anderen Datei erhalten hier Namen (alarm, alarm1 usw.)
    alarm = rechnen()
    alarm1 = rechnen1()
    alarm2 = rechnen2()
    alarm3 = rechnen3()
    # zurücksetzen der json für den ResetButton
    if request.method == 'POST':
        if request.form.get("reset") == "reset":
            meine_sammlung = []
            with open('daten2.json', 'w') as open_file:
                json.dump(meine_sammlung, open_file, indent=3, separators=(',', ':'))
            summe = []
            with open('summe.json', 'w') as open_file:
                json.dump(summe, open_file, indent=3, separators=(',', ':'))

#es soll die drei Funktionen returnen, bei welchen die Rechnungen zur Entsorgung gemacht wurden
    return render_template("index.html", alarm=alarm, alarm1=alarm1, alarm2=alarm2, alarm3=alarm3)


"""Formularfeld"""
@app.route("/form", methods=["get", "post"])
def form():
    # method get, post (Formularfelder) Daten werden abgeholt und dann weiter verarbeitet
    if request.method.lower() == "get":

        return render_template("formular.html")
    if request.method.lower() == "post":
        # Verknüpfung zu json (Datum, was, Masseinheit, Anzahl)
        a = request.form.get("Datum")
        b = request.form.get("Was")
        c = request.form.get("Masseinheit")
        d = request.form.get("Anzahl")
        #meine_sammlung ist frei wählbar
        meine_sammlung = {"Datum": a, 'Was': b, "Masseinheit": c,  "Anzahl": d}
        #request holt Daten aus Formular und tut Sie in den Dictionary "meine_sammlung". Dann speichert es diese Daten
        #in die json daten

        #daten2.json
        # Datei öffnen von der Daten.py
        data = opendatei()
        # Daten zur json Datei hinzufügen
        data.append(meine_sammlung)
        # Eingaben in daten2.json speichern
        storedatei(data)
        # meine Sammlung ist daten2.json
        return render_template("formular.html", name="meine_sammlung")



"""Auswertungsseite"""

@app.route("/auswertung", methods=["POST", "GET"])
def auswerten():
    # get post (Formular) für den Filter button auf der HTML seite
    if request.method.lower() == "get":
        return render_template("auswertung.html")
    if request.method.lower() == "post":
# refrenziert mit der unteren if Funktion um eine Sortierung nach der Sorte zu machen (in einer neuen Liste)
        was = request.form.get("Was")
    auswertungs_liste = []   #list erstellen leer für die HTML seite
    data = opendatei()  #Json Datei öffnen
    for element in data:
        # Element "Was" ist Pet, Glas oder Karton aus json liste ansprechen
        if element["Was"] == was:
            auswertungs_liste.append([element["Datum"], element["Was"], element["Masseinheit"], element["Anzahl"]])
            # für jedes Element in der jason Datei soll es nun jeweils
            # die Elemente zu der auswertungs_liste dazutun
            # ausgabe des Htmls und der auswertungs_liste (jeweils mit dem ausgewählten Filter)
    return render_template("auswertung.html", liste=auswertungs_liste)


"""Seite mit co2"""
@app.route("/co2")
def c02():
    # die Funktion der anderen Datei(c02.py) erhält hier einen Namen (co2 usw. und wird returned)
    co2 = co2_sparen()
    return render_template("co2.html", co2=co2)


"""Seite mit statistik"""


@app.route("/statistik", methods=["get", "post"])
def stat():
    # diese Funktionen der anderen Datei erhalten hier Namen (alarm, alarm1 usw.) (Summen, die es braucht
    #um weiter zu rechnen für die Statistik
    alarm = rechnen()
    alarm1 = rechnen1()
    alarm2 = rechnen2()
    alarm3 = rechnen3()

    # method get, post (Formularfelder) Daten werden abgeholt und dann weiter verarbeitet

    if request.method.lower() == "get":

        return render_template("statistik.html", alarm=alarm, alarm1=alarm1, alarm2=alarm2, alarm3=alarm3)
    #Bei Klick auf Button wird Funktion ausgeführt, um die Daten in die neue json Datei zu speichern
    #-> diese braucht es, um die Diagramme zu erstellen
    if request.form.get("anzeigen") == "anzeigen":

        # Datei öffnen von daten1.py um nachher dort Daten hinein zu speichern
        data1 = opendatei1()
        # daten clearen bevor Daten dazugefügt werden, um immer die aktuellste Anzahl zu haben
        data1.clear()
        # kommt von alarm.py (Funktion welche summen ausgibt)
        summe = form1()
        # Daten zur json Datei (summe.json) hinzufügen
        data1.append(summe)
        # Eingaben von summe.json speichern
        storedatei1(data1)


    #die Funkion viz() erhält einen Namen und wird unten durch das render_template returned
    alarm5 = form1()
    div = viz()
    try:
        with open("summe.json") as open_file:
            data1 = json.load(open_file)
    except FileNotFoundError:
        data1 = {}

    return render_template("statistik.html", viz_div=div, alarm5=alarm5)


def get_data():
    # Glas Pet und Karton als Sorte sind vordefiniert, die bleiben
    sorte = ["Glas", "Pet", "Karton"]
    # für die Anzahl wird eine neue Liste geöffnet und die Anzahle dort rein gespeichert
    anzahl = []
    try:
        with open("summe.json") as open_file:
            data1 = json.load(open_file)
    except FileNotFoundError:
        data1 = {}
    # Liste in Liste darum zwei mal [][]
    # zu der Anzahlliste wird jeweils der 1. eintrag aus dem ersten eintrag hinzugefügt
    anzahl.append(data1[0][0])
    # dann der zweite Eintrag aus dem ersten Eintrag
    anzahl.append(data1[0][1])
    # dann der dritte Eintrag aus dem ersten Eintrag

    anzahl.append(data1[0][2])
    # mit dem Return sorte und Anzahl wird dann unten weitergerechnet
    return sorte, anzahl



#funktion fürs Plotly (visualisierung)
def viz():
    sorte, anzahl = get_data()
    # hier wird definiert, welche Achse von welchen Daten gebraucht wird
    fig = px.bar(x=sorte, y=anzahl)
    fig.update_layout(
        # Achsentitel
        xaxis_title="Sorte",
        yaxis_title="Anzahl Glas oder Pet/Gramm Karton",
    )

    div = plot(fig, output_type="div")

    # der Funktion viz() wird oben ein Name gegeben (div) diese wird dann returnt
    # diese Funktion wird dann als jinja auf der Seite ausgegeben
    return div

"""Wenn der Name der Datei mit Main übereinstimmt, führt es die App auf dem Port 5000 aus"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)

#bei der Ausführung von FLASK wird der port 5000 verwendet. FLASK ist mit __name__ definiert
