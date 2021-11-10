from flask import Flask, render_template, request
import requests
from api_manager import callLigne, callStation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
# Methode responsable du render de la l'index
def home():
    current_stations = callLigne(1)
    if request.method == "POST":
        current_station_slug = request.form.get("station")
        current_station_name = request.form.get("station").replace("+", " ").title()
        current_schedules = callStation(1, current_station_slug)
    return render_template("index.html", stations=current_stations, station=current_station_name, schedules=current_schedules)

if __name__ == '__main__':
    app.run(debug=True)