
from flask import Flask
from flask import render_template
from flask import request
from daten import opendatei, storedatei


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
        a=request.form.get("was")
        b=request.form.get("Masseinheit")
        c=request.form.get("anzahl")
        meine_sammlung = {'was': a, "Masseinheit": b,  "anzahl":c}

        data=opendatei()
        data.append(meine_sammlung)
        storedatei(data)

        return render_template("formular.html")




#Auswertungseite
@app.route ("/auswertung")
def auswertung():
    return render_template("auswertung.html")

#Alarm
@app.route ("/entsorgungsalarm")
def entsorgungsalarm():
    return render_template("entsorgungsalarm.html")

#Seite mit About
@app.route ("/About")
def about():
    return render_template("About.html")






if __name__ == "__main__":
    app.run(debug=True, port=5000)
