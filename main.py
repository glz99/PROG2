
from flask import Flask
from flask import render_template
from flask import request
from daten import opendatei, storedatei
import plotly
import json
from rechnen.co2 import co2_sparen





app = Flask("Daten")


app = Flask("__name__")

#Hauptseite
@app.route("/")
def index():
    return render_template("index.html")


#Formularfeld
@app.route("/form", methods=["get", "post"])
def form():

    if request.method.lower() == "get":
        return render_template("formular.html")
    if request.method.lower() == "post":
        a=request.form.get("Datum")  # Verknüpfung zu json
        b=request.form.get("Was")   #Verknüpfung zu json
        c=request.form.get("Masseinheit") #Verknüpfung zu json
        d=request.form.get("Anzahl") #Verknüpfung zu json
        meine_sammlung = {"Datum": a, 'Was': b, "Masseinheit": c,  "Anzahl": d}

        data=opendatei()
        data.append(meine_sammlung)
        storedatei(data)

        return render_template("formular.html", name="meine_sammlung")




#Auswertungseite
@app.route ("/auswertung")
def auswerten():
    auswertungs_liste = [] #list erstellen leer für die HTML seite
    data = opendatei()  #Json Datei öffnen
    for element in data: # für jedes Element in der jason Datei soll es nun jeweils die Elemente zu der (neuen) auswertungs_liste dazutun
        auswertungs_liste.append([element["Datum"],element["Was"], element["Masseinheit"], element["Anzahl"]])
    return render_template("auswertung.html", liste=auswertungs_liste) #ausgabe des Htmls und der auswertungs_liste

#Alarm
@app.route ("/entsorgungsalarm")
def entsorgungsalarm():
    return render_template("entsorgungsalarm.html")

#Seite mit co2
@app.route ("/co2")
def c02():
    co2 = co2_sparen()
    return render_template("co2.html", co2=co2)







"""Wenn der Name der Datei mit Main übereinstimmt, führt es die App auf dem Port 5000 aus"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)
