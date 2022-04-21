
from flask import Flask
from flask import render_template
from flask import request



app = Flask("__name__")

#Hauptseite
@app.route("/")
def index():
    return render_template("index.html")



@app.route("/form", methods=["get", "post"])
def form():
    if request.method.lower() == "get":
        return render_template("formular.html")
    if request.method.lower() == "post":
        return render_template("formular.html")



@app.route ("/auswertung")
def auswertung():
    return render_template("auswertung.html")


@app.route ("/entsorgungsalarm")
def entsorgungsalarm():
    return render_template("entsorgungsalarm.html")


@app.route ("/About")
def about():
    return render_template("About.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
