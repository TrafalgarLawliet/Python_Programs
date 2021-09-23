import requests, time, threading
from win10toast import ToastNotifier

ipinfo = requests.get("https://ipapi.co/json").json()
coordinates = {"lat": ipinfo["latitude"], "lon": ipinfo["longitude"]}
apiKey = 'ed02dec75b9653c5b89188520fcce49e'
weatherApi = "https://api.openweathermap.org/data/2.5/weather"

def showWeather():
    weather = requests.get(weatherApi, params={**coordinates, "appid":apiKey}).json()
    condition = weather["weather"][0]["description"]
    temp = weather["main"]["temp"] - 273.15
    notif = ToastNotifier()
    print(f"Not it's {condition}, currently {temp} °C")
    notif.show_toast("The Current weather is" , f"Not it's {condition}, currently {temp} °C")
    threading.Timer(1000*60*60,showWeather()).start()
    

showWeather()
