Weather app using Django | Python



In this tutorial, we will learn how to create a Weather app that uses Django
as backend. Django provides a Python Web framework based web framework that
allows rapid development and clean, pragmatic design.

 **Basic Setup –**  
Change directory to weather –

    
    
    cd weather

Start the server –

    
    
    python manage.py runserver

To check whether the server is running or not go to a web browser and enter
http://127.0.0.1:8000/ as URL. Now, you can stop the server by pressing

    
    
    ctrl-c

## Implementation :

    
    
     python manage.py startapp main

Goto main/ folder by doing :

  

  

    
    
    cd main 

and create a folder with index.html file: _templates/main/index.html_

Open the project folder using a text editor. The directory structure should
look like this :  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190820021205/Screenshot-from-2019-08-20-02-11-40.png)

Now add main app in settings.py  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190820021251/Screenshot-from-2019-08-20-02-12-38.png)

 **Editurls.py file in weather :**

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path, include

 

 

urlpatterns = [

 path('admin/', admin.site.urls),

 path('', include('main.urls')),

]  
  
---  
  
 __

 __

 **editurls.py file in main :**

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path

from . import views

 

urlpatterns = [

 path('', views.index),

]  
  
---  
  
 __

 __

 **edit views.py in main :**

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

# import json to load json data to python dictionary

import json

# urllib.request to make a request to api

import urllib.request

 

 

def index(request):

 if request.method == 'POST':

 city = request.POST['city']

 ''' api key might be expired use your own api_key

 place api_key in place of appid ="your_api_key_here " '''

 

 # source contain JSON data from API

 

 source = urllib.request.urlopen(

 'http://api.openweathermap.org/data/2.5/weather?q ='

 + city + '&appid; = your_api_key_here').read()

 

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

 else:

 data ={}

 return render(request, "main/index.html", data)  
  
---  
  
 __

 __

You can get your own API key from :Weather API

Navigate to templates/main/index.html and edit it: link to index.html file

 **Make migrations and migrate it:**

    
    
    python manage.py makemigrations
    python manage.py migrate
    

now let’s run the server to see your weather app.

    
    
    python manage.py runserver

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190820022051/Screenshot-from-2019-08-20-01-55-39.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

