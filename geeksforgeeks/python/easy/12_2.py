Create a Weather app using Flask | Python



 **Prerequisite :** Flask installation

Flask is a lightweight framework written in Python. It is lightweight because
it does not require particular tools or libraries and allow rapid web
development. today we will create a weather app using flask as a web
framework. this weather web app will provide current weather updates of cities
searched.

 **Basic setup :**

Create a file and name it as ****weather.py****

Linux command to create a file

  

  

    
    
    touch weather.py 

Now, create a folder _templates_ with a file name index.html

Linux command to create a folder and a file

    
    
     mkdir templates && cd templates && touch index.html 

The project folder will look like :  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190826191659/Screenshot-from-2019-08-26-19-16-35.png)

 **Editing files :**  
Use your own API key from Weather API and place it in API variable. Now edit
weather.py file.

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask, render_template, request

 

# import json to load JSON data to a python dictionary

import json

 

# urllib.request to make a request to api

import urllib.request

 

 

app = Flask(__name__)

 

@app.route('/', methods =['POST', 'GET'])

def weather():

 if request.method == 'POST':

 city = request.form['city']

 else:

 # for default name mathura

 city = 'mathura'

 

 # your API key will come here

 api = api_key_here

 

 # source contain json data from api

 source =
urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q
=' + city + '&appid; =' + api).read()

 

 # converting JSON data to a dictionary

 list_of_data = json.loads(source)

 

 # data for variable list_of_data

 data = {

 "country_code": str(list_of_data['sys']['country']),

 "coordinate": str(list_of_data['coord']['lon']) + ' '

 + str(list_of_data['coord']['lat']),

 "temp": str(list_of_data['main']['temp']) + 'k',

 "pressure": str(list_of_data['main']['pressure']),

 "humidity": str(list_of_data['main']['humidity']),

 }

 print(data)

 return render_template('index.html', data = data)

 

 

 

if __name__ == '__main__':

 app.run(debug = True)  
  
---  
  
 __

 __

Navigate to templates/index.html and edit it:link to the index file.

Now you can run the server to see the weather app –

    
    
     python weather.py 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

