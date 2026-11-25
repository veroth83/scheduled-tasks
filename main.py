import requests
from twilio.rest import Client
import os


ACCOUNT_SID ="ACb7d76af3bde11fd8d2d09bfc9bbb2508"
#AUTH_TOKEN ="9bc99cc4b012767232f0dc6fb17f08f2"



API_KEY =os.environ.get("OWM_API_KEY")
AUTH_TOKEN =os.environ.get("OWM_AUTH_TOKEN")
ACCOUNT_SID =os.environ.get("OWM_ACCOUNT_SID")
print(API_KEY)
#API_KEY="d3942f549005e2c2244ac3c5fbc16883"
city_name="lima,PE"

# LAT=-12.046373
# LONG=-77.042755


LAT=16.756932
LONG=-93.129235

#https://api.openweathermap.org/data/2.5/forecast?lat=-12.046373&lon=-77.042755&appid=d3942f549005e2c2244ac3c5fbc16883

# parameters={
#     "q":city_name,
#     "appid":API_KEY,
# }

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid":API_KEY,
    "cnt":4,
}


request=requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
request.raise_for_status()
weather_data=request.json()




llovera=[clima["weather"][0]["id"] for clima in weather_data["list"] if clima["weather"][0]["id"] <700]
if len(llovera)==0:
    print("No llovera")
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to="whatsapp:+51991359498",
        from_="whatsapp:+17372212163",
        content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
    )
    print(message.sid)


