import requests

# Methode reponsable de récuperer les names et slug de toutes les stations d'une ligne
def callLigne(ligne):
    url = "https://api-ratp.pierre-grimaud.fr/v4/stations/metros/"+str(ligne)
    response = requests.request("GET", url)
    data = response.json()
    stations=data["result"]["stations"]
    return stations

# Methode responsable de récuperer les destinations et messages d'une station
def callStation(ligne, station):
    schedules = []
    url = "https://api-ratp.pierre-grimaud.fr/v4/schedules/metros/"+str(ligne)+"/"+station+"/A+R"
    response = requests.request("GET", url)
    data = response.json()
    schedules = data["result"]["schedules"]
    return schedules