from flask import Flask, render_template, request  #imports jo use honge aage
import json
import urllib.request

app = Flask(__name__) #flask mai heading daalni padti hai 

@app.route('/', methods=['POST','GET']) # POST matlab server/website ko kuch input/data dena aur GET matlab server se data lena
def weather():  #main cheez chalu idhar se
    if request.method == 'POST':
        city = request.form['city'] #ye check kar raha ki kya koi city naam ka input aaya and agar aya hai to usko city variable mai store kr raha hai jo ham python file(ye wali) mai use kr rhe hai 
    else:
        city = 'delhi'  # Default city jo dikhayega jab website kholenge initially y

    api = '0383efdbfa9528f52c9bed05cd2f67e8' #https://www.geeksforgeeks.org/what-is-an-api/ basically api ki wajah se ham har city ke weather ka data access kar pa rahe hai

    try: #https://www.w3schools.com/python/python_try_except.asp
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}').read() #apne browser mai ye website ko daalo,{city} and {api} ki jagah delhi ya koi bhi city aur api ki jagah vo upar key hai vo daalke tab smjh aayega iska matlab
        list_of_data = json.loads(source) #ye website se data leke 1 list mai store kr raha hai  https://www.w3schools.com/js/js_json_intro.asp

        data = {   #ye ham vo list(list_of_data) se data extract kr rahe hai jo hamare kaam ka hai 1 dictionary mai
            "cityname": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "temp": f"{list_of_data['main']['temp'] - 273.15:.2f}°C",  #Converts Kelvin to Celsius
            "feels_like":f"{list_of_data['main']['feels_like']-273.15:.2f}°C",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    except KeyError:
        data = {"error": "Could not retrieve data. Please check the city name."}
    except Exception as e:
        data = {"error": str(e)}

    return render_template('index.html', data=data) #html wali file ko data dera hai jo hamare kaam ke liye chahiye and jiski wajah se ham display kar pa rahe hai data website pe

if __name__ == '__main__': #isse start hoti hai website basially jab ham python file run krte hai to __name__ change hojata hai to __main__
    app.run() #finally start
