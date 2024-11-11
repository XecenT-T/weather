from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'delhi'

    api = '0383efdbfa9528f52c9bed05cd2f67e8'

    try:
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}').read()
        list_of_data = json.loads(source)

        data = {
            "cityname": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "temp": f"{list_of_data['main']['temp'] - 273.15:.2f}°C",
            "feels_like": f"{list_of_data['main']['feels_like'] - 273.15:.2f}°C",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    except KeyError:
        data = {"error": "Could not retrieve data. Please check the city name."}
    except Exception as e:
        data = {"error": str(e)}

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
