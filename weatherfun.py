import os  
from flask import Flask,redirect  
import pyowm
import json  

app = Flask(__name__)  
owm = pyowm.OWM('51c9bc8baaaa942e5b88971674a0869c')
def getWeather(city):
   observation = owm.weather_at_place(city)
   return observation.get_weather()
def getTemperature(city):
   weather = getWeather(city)
   return weather.get_temperature('fahrenheit')
def getDetailedWeather(city):
   weather = getWeather(city)
   return weather.get_detailed_status()
@app.route('/')  
def index():  
   return redirect('/weather/NYC')  
@app.route('/weather/<city>')  
def weather(city):  
   temp = getTemperature(city)
   print temp['temp']
   page='<title>current weather for '+city+'</title>'  
   page +='<h1><u>Current weather for '+city+'</u></h1>'  
   page +='<br/>Current Temp. '+str(temp['temp'])+'<br/>'  
   page += '<br/>Weather: '+str(getDetailedWeather(city))+'<br/>'  
   return page  
port = os.getenv('PORT', '5000')  
if __name__ == "__main__":  
   app.run(host='0.0.0.0', port=int(port))  
