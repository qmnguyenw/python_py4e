Integrating Facebook Comments Plugin in Django Project



Django is a Python-based web framework that allows you to quickly create
efficient web applications. It is also called batteries included framework
because Django provides built-in features for everything including Django
Admin Interface, default database – SQLlite3, etc. In this article we will
learn to integrate facebook comment plugin in django.

### How to integrate facebook comments plugin?

First we have to install django. Open cmd or terminal

    
    
    pip install django

To Create new django project –

    
    
    django-admin startproject fbcomm

Then write command –

    
    
    cd fbcomm

create new app –

  

  

    
    
    python manage.py startapp main

 **Folder Structure :-**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111001852/Screenshotfrom20210110234202-70x200.png)

Then add the app name in INSTALLED_APPS in **settings.py .**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210105233722/Screenshotfrom202101052331151-300x171.png)

fbcomm/ **urls.py** :-

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path,include

 

urlpatterns = [

 path('admin/', admin.site.urls),

 path('',include("main.urls")),

]  
  
---  
  
 __

 __

 **views.py**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

 

# Create your views here.

 

def home(request):

 return render(request,'main/index.html')  
  
---  
  
 __

 __

Then create the new file in main folder and name it as **urls.py**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path

from .views import *

 

urlpatterns = [

 path('',home,name="home")

]  
  
---  
  
 __

 __

Go to Facebook comment plugin link and get the code of comment plugin

  

  

https://developers.facebook.com/docs/plugins/comments

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111003531/Screenshotfrom20210110232535.png)

Click on get code and copy that code

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111003728/Screenshotfrom20210110232550.png)

Inside main create the folder templates inside create another main folder

Then create the file and name it as **index.html**

## HTML

 __

 __  
 __

 __

 __  
 __  
 __

<html>

 <head>

 <title>FBCOMM</title>

 </head>

<script async defer crossorigin="anonymous"

 src="https://connect.facebook.net/en_GB/sdk.js#xfbml=1&version;=v9.0"

 nonce="tQBFzkBF">

</script>

<body>

 <h1>Facebook Comment Plugin</h1>

 <div class="fb-comments" data-
href="http://127.0.0.1:8000/index"

 data-width="" data-numposts="5"></div>

</body>

</html>  
  
---  
  
 __

 __

To run django app open cmd or terminal and write command

    
    
    python manage.py runserver

 **Output :-**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111003726/Screenshotfrom20210110233928.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

