#!/usr/bin/env python

# weather.py - Retrieve Weather Forecast From Dark Sky (darksky.net)

# Get An API Key And Longitude / Latitude At: https://darksky.net/dev/

# Install 'forecastio' module with: pip install python-forcastio

import forecastio

# Weather For Berlin, Germany

api_key = "e3f8667cb539171dc2f4b389d33648ce"

lat = 52.520008
lng = 13.404954

forecast = forecastio.load_forecast(api_key, lat, lng)
byHour = forecast.currently()
currentTemp = int(byHour.temperature)

print("The weather is currently {0} ...".format(byHour.summary))

print("The temperature is {0} degrees Celsius ...".format(currentTemp))

byHour = forecast.hourly()
print(byHour.summary)

byHour = forecast.daily()
print(byHour.summary)