import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "b3f6b991186822870453f3f1accbdba0"
account_sid = "ACdcf77fab92faec809a55bed7a38e05dd"
auth_token = "f8208bffe9a66fea55b3b1b71b84d6ce"

weather_params = {
    "lat": 51.593819,
    "lon": -0.382170,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+18652726709",
        to="+44XXXXXXXX"
    )
    print(message.status)
