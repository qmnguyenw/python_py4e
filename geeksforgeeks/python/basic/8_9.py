Associate user to its upload (post) in Django



Django provides built-in facilities of ForeignKey, ManytoManyField for
associating one model to other model. To associate a user model to a post
model, one can use various options. This article revolves around how to
associate a user to its post (post model). This tutorial uses the concept of
foreign keys in Django and at the end, one will be able to create application
of post upload and also profile app which contains all the past uploads of the
user.

 **Prerequisites –**

  1. Creation of Django project
  2. Creation of application which can register login and logout the user
  3. Make migrations in application and add database

We have already created a user application for registration and so we will
create a new app that can be named as userblog (blog upload from the user) .To
do this create an app in main project file by writing this code in your
PowerShell or terminal

    
    
    django-admin startapp userblog
    

Now this application is available in your project file and you should first
add this application to settings.py file in the project and add this
application to **INSTALLED_APPS**

Now make migrations in your project and add this application to your project

  

  

    
    
    python manage.py makemigrations
    python manage.py migrate
    

Now we have to use models in this application so that Django can create a
table for the information which we are going to store in our database and the
user can input the information. We have to create a class in the models.py
file of userblog application which is named as Snippet. We will use a
ForeignKey class which will hold the id value of the user and it holds one to
many relationship and so you can use this class to associate the user to any
other activities where there is user involvement.

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.conf import settings

 

User = settings.AUTH_USER_MODEL

 

# Create your models here.

class Snippet(models.Model):

 user = models.ForeignKey(User,

 default = 1,

 null = True, 

 on_delete = models.SET_NULL

 )

 blogname = models.CharField(max_length = 100)

 blogauth = models.CharField(max_length = 100)

 blogdes = models.TextField(max_length = 400)

 img = models.ImageField(upload_to ='pics')

 

 def __str__(self):

 return self.blogname  
  
---  
  
 __

 __

Also create a python file named asforms.py and create a ModelForm for the
same to input data from user.

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

from .models import Snippet

 

class SnippetForm(forms.ModelForm):

 class Meta:

 model = Snippet

 fields = ['blogname',

 'img',

 'blogauth',

 'blogdes'

 ]  
  
---  
  
 __

 __

We need to migrate the class model of Snippet so that Django administration
creates a database for the post upload and details so makemigrations of the
class Snippet and you will see this in django administration –  
![cool](https://media.geeksforgeeks.org/wp-
content/uploads/20200112124246/screencapture-127-0-0-1-8000-admin-userblog-
snippet-add-2020-01-12-12_41_03.png)  
Here User is a foreign key which will show all the users and it will store the
key number of last instance of post upload by a user by default it is set to
superuser  
Now we will go to views.py file of application and add the main code which
will be storing the information in database using model form object.

  *  **usblog** – This will display all the posts in our homepage
  *  **snippet_detail** – This will get the data from the user in the form ad it will associate blog to user

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

from django.http import HttpResponse

from .forms import SnippetForm

from .models import Snippet

from django.contrib import messages

# Create your views here.

def usblog(request):

 snipps = Snippet.objects.all()

 return render(request, 'indexg.html', {'snipps' : snipps})

 

def snippet_detail(request):

 form = SnippetForm(request.POST or None, request.FILES or
None)

 if request.method =='POST':

 

 if form.is_valid():

 

 obj = form.save(commit = False)

 obj.user = request.user;

 obj.save()

 form = SnippetForm()

 messages.success(request, "Successfully created")

 

 

 return render(request, 'form.html', {'form':form})  
  
---  
  
 __

 __

So by now the Django administration has created the database of Snippet class
and you can see it by visiting Django administration. Now we have to create a
simpleform.html file which we will contain a form from where user can enter
the queries which we have stated in the class. Here comes the beauty of Django
that since we have used model forms for our application Django has created
HTML code of form which will have all those queries which we needed. So simply
create an HTML file in your templates file(form.html).

 __

 __  
 __

 __

 __  
 __  
 __

<!DOCTYPE html>

<html lang="en">

 

<head>

 <meta charset="UTF-8">

 <meta name="viewport" content="width=device-width, initial-
scale=1.0">

 <meta http-equiv="X-UA-Compatible" content="ie=edge">

 <title>Your Blog</title>

</head>

 

<body>

 <form method="post" enctype="multipart/form-data">

 {% csrf_token %}

 {{form.as_p}}

 <button type="submit">Submit</button>

 </form>

</body>

 

</html>  
  
---  
  
 __

 __

Now we will need a homepage where we will see all the posts of the users so
create another HTML file indexg.html and import the objects of function which
we have created in views.py file. (Placed image of only body part of html to
show the python code you can make your own indexg with features )

 __

 __  
 __

 __

 __  
 __  
 __

<body>

 <h1>Post play<h4>Only for geeks</h4>

 </h1>

 

 <div class="topnav">

 {% if user.is_authenticated %}

 <a href="#">Hi {{user.username}}</a>

 <a href="accounts/logout">Logout</a>

 <a href="snippet_detail">Write post</a>

 {% else %}

 <a href="accounts/register">Register</a>

 <a href="accounts/login">Login</a>

 {% endif %}

 </div>

 <p>

 {% for snips in snipps %}

 

 <img src="{{snips.img.url}}" alt="Image" class="img-
fluid">

 <h2 class="font-size-regular"><a
href="#">{{snips.blogname}}</a></h2>

 <h3>{{snips.user}}</h3>

 {% if user.is_authenticated %}

 <p>{{snips.blogdes}}</p>

 {% else %}

 <p>Register/Login to know more</p>

 {% endif %}

 

 

 {% endfor %}

 

 </p>

 </div>

</body>  
  
---  
  
 __

 __

Let us go to our main urls file where we will have an account app and now make
the userblog application as default and add the URLs of your application. Also
in your userblog application add urls.py and add the links of 2 functions
which are form.html and homepage(indexg.html).  
 **Main Urls**

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

 path('', include('userblog.urls')),

 

 path('admin/', admin.site.urls),

 path('accounts/', include('accounts.urls'))

 

]  
  
---  
  
 __

 __

 **userblog urls –**

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

 

 path("snippet_detail", views.snippet_detail),

 path('', views.usblog, name ='usblog')

]  
  
---  
  
 __

 __

Start the application and register the user to your application and make a
post

    
    
    python manage.py runserver
    

Your browser does not support playing video  

GITHUB LINK – Github Repo

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

