Python | Django News App



 **Django** is a high-level framework which is written in Python which allows
us to create server-side web applications. In this article, we will see how to
create a News application using Django.  
We will be using **News Api** and fetch all the headline news from the api.
Read more about the api here news api.  
Do the Following steps in command prompt or terminal:  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190626135553/Capture34-3.png)

Open the newsproject folder using a text editor. The directory structure
should look like this  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190626135924/Capture239.png)

Create a “templates” folder in your newsapp and it in settings.py  
 **Settings .py**  

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190626140243/Capture34-3.png)

**In views.py –**  
In views, we create a view named index which takes a request and renders an
html as a response. Firstly we import newsapi from NewsApiClient.  

__

__  
__

__

__  
__  
__

# importing api

from django.shortcuts import render

from newsapi import NewsApiClient

 

# Create your views here. 

def index(request):

 

 newsapi = NewsApiClient(api_key ='YOURAPIKEY')

 top = newsapi.get_top_headlines(sources ='techcrunch')

 

 l = top['articles']

 desc =[]

 news =[]

 img =[]

 

 for i in range(len(l)):

 f = l[i]

 news.append(f['title'])

 desc.append(f['description'])

 img.append(f['urlToImage'])

 mylist = zip(news, desc, img)

 

 return render(request, 'index.html', context
={"mylist":mylist})  
  
---  
  
 __

 __

  
Create a index.html in **templates** folder.  

## html

 __

 __  
 __

 __

 __  
 __  
 __

<!DOCTYPE html>

<html lang="en" dir="ltr">

 <head>

 <meta charset="utf-8">

 <title></title>

 

<link rel="stylesheet"
href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
crossorigin="anonymous">

<!-- Optional theme -->

 </head>

 <body>

 <div class="jumbotron" style="color:black">

 

 <h1 style ="color:white">

 Get The latest news on our website

 </h1>

 

 </div>

 

 

 <div class="container">

 {% for new, des, i in mylist %}

 <img src="{{ i }}" alt="">

 <h1>news:</h1> {{ new }}

 {{ value|linebreaks }}

 

 <h4>description:</h4>{{ des }}

 {{ value|linebreaks }}

 

 {% endfor %}

 </div>

 

 </body>

</html>  
  
---  
  
 __

 __

  
Now map the views to **urls.py**  

__

__  
__

__

__  
__  
__

from django.contrib import admin

from django.urls import path

from newsapp import views

 

urlpatterns = [

 path('', views.index, name ='index'),

 path('admin/', admin.site.urls),

]  
  
---  
  
 __

 __

Your output of the project should look like this –  

https://media.geeksforgeeks.org/wp-
content/uploads/20190626143109/screen_recorder_video_2019_26_6_14_29_59.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

