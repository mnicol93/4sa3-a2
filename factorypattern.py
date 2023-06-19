################################################################################
# Assignment #2 Factory Pattern Starter Code
#
# Starter code for Assignment #2...
#
# The Open Weather Map API allows to to request the weather for a given city:
#   - Documentation: https://openweathermap.org/api
# In order to use this API, we do need to create an account to obtain an API
# key: https://home.openweathermap.org/users/sign_in.  And it does take a few
# minutes for the API key to start working after we've signed up for it...
#
# This API also has a "wrapper", a Python module that makes accessing the API
# easier for us... rather than manually making and sending requests, we
# can call functions that do this for us and just return the results.
#  - Wrapper documentation: https://github.com/csparpa/pyowm
#
# See the WebAPI Examples on Avenue for an example of using this wrapper!
#
# To install a Python module locally to make it available in your own solutions,
# you generally need to use pip3:
#    pip3 install pylast
#

# import the open weather data wrapper module
from pyowm import OWM



# Implement these classes: Factory, WeatherData, Wind, Humidity, Temperature
class Factory():
    def getWeather():
        return 'Hola'

class WatherData(Factory):

class Wind(WeatherData):

class Humidity(WeatherData):

class Temperature(WeatherData):
    
# Create factory object
factory = Factory()
owm = OWM('0c26196096af56fb6a9cf51b734a63e2')

# Create a WeatherData object of each type (Wind, Temperature, Humidity) at
# different locations so we can test our factory's createData instance method
weatherdata = [factory.createData("Hamilton,ON,CA","wind"), \
               factory.createData("Toronto,ON,CA","humidity"), \
               factory.createData("Ottawa,ON,CA","temperature")]

# Call the output method for each WeatherData object
for data in weatherdata:
    data.output()

# When I run the above code with my factory object and WeatherData objects
# implemented, I get the following:
#
#   Wind speed of 6.7 meter/sec in Hamilton,ON,CA
#   Humidity of 35% in Toronto,ON,CA
#   Temperature of 30.71C in Ottawa,ON,CA
#


