import os  
from flask import Flask,redirect  
import pyowm
import json  

app = Flask(__name__)  

"""Set the env key for the weather key using cf set-env <app> <keyname> <keyval>"""
owm = pyowm.OWM(str(os.getenv('WEATHER_KEY'))) 
def getWeather(city):
   """Abstracts out getting weather. Pass it the city name"""
   observation = owm.weather_at_place(city)
   return observation.get_weather()
def getTemperature(city):
   """Abstracts out getting temperature. Pass it the city name"""
   weather = getWeather(city)
   return weather.get_temperature('fahrenheit')
def getDetailedWeather(city):
   """Abstracts out getting detailed weather. Pass it the city name"""
   weather = getWeather(city)
   return weather.get_detailed_status()
@app.route('/')  
def index():  
   return redirect('/weather/NYC')  
@app.route('/weather/<city>')  
def renderWeatherPage(city):  
   """Renders the weather page. hit <url>/weather/<city> to get the weather for that city"""
   temp = getTemperature(city)
   page='<title>current weather for '+city+'</title>'  
   page +='<h1><u>Current weather for '+city+'</u></h1>'  
   page +='<br/>Current Temp. '+str(temp['temp'])+'<br/>'  
   page += '<br/>Weather: '+str(getDetailedWeather(city))+'<br/>'  
   return page  
port = os.getenv('PORT', '5000')  
if __name__ == "__main__":  
   app.run(host='0.0.0.0', port=int(port))  
