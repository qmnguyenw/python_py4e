How to build a URL Shortener with Django ?



Building a URL Shortener, Is one of the Best Beginner Project to Hone your
Skills. In this article, we have shared the steps to build a URL shortener
using Django Framework. To know more about Django visit – Django Tutorial

### Setup

We need some things setup before we start with our project. We will be using
Virtual Environment for our project.

    
    
    pip install virtualenv
    virtualenv urlShort
    source urlShort/bin/activate
    

Above Command will create, activate virtual environment named _urlShort_.

### Installing Important Packages

We need to Install some packages before hand,

    
    
    pip install django
    

### Starting With Our Project

First of all, We need to create our project by,

  

  

    
    
    django-admin startproject urlShort
    cd urlShort
    

Above Command, Creates A Django Project and then cd into that directory. After
that, We also need to create an app inside of our project. App is sort of a
container, where we will store our code. A project can have Multiple Apps and
they can be interconnected

    
    
    python manage.py startapp url
    

Above Command Creates an App named URL in our Project. Our File Structure Now
will be —

    
    
    urlShort
    ├── manage.py
    ├── url
    │ ├── admin.py
    │ ├── apps.py
    │ ├── __init__.py
    │ ├── migrations
    │ │ └── __init__.py
    │ ├── models.py
    │ ├── tests.py
    │ └── views.py
    └── urlShort
     ├── asgi.py
     ├── __init__.py
     ├── __pycache__
     │ ├── __init__.cpython-37.pyc
     │ └── settings.cpython-37.pyc
     ├── settings.py
     ├── urls.py
     └── wsgi.py
    

### Checking If all is Great…

You can check if all is working by just typing this in Command Line. But cd
into the main folder, here urlShort.

    
    
    python manage.py runserver
    

_runserver_ will run a local server where our website will load. Move to url

    
    
    https://localhost:8000
    

Keep Your Console Window Open.

## How to Build a URL Shortener Project?

Tighten your seat belts as we are starting to Code. First of all, we will play
with _views.py_. _views.py_ is basically used to connect our database, api
with our Frontend. Open _views.py_ and type

    
    
    from django.http import HttpResponse
    
    
    def index(request):
        return HttpResponse("Hello World")

Save it and open localhost and check if it changes.It does not change because
we have not map it to any route.Basically, If you write any function inside
_views.py_ it does not work but we need to map it inside _urls.p_ y. So,
Create a _urls.py_ inside _url_ folder.

    
    
    from django.urls import path
    from . import views
    app_name = "url"
    urlpatterns = [
        path("", views.index, name="home")
    ]

Don’t forget to add your _app – “_ url _”_ in _INSTALLED_APPS_ in
_settings.py_

### Creating Django Models –

First of all, we need a Database to store our Shorten URL’s. For That, We need
to create a Schema for our Database Table in models.py.

  

  

 _models.py_

    
    
    from django.db import models
    class UrlData(models.Model):
        url = models.CharField(max_length=200)
        slug = models.CharField(max_length=15)
    def __str__(self):
            return f"Short Url for: {self.url} is {self.slug}"
    

Above Code Creates a Table _UrlData_ in our Database with Columns _url_ ,
_slug_. We will use url column to store Original URL and _slug_ to store
10-character string which will be used for shortening the URL.

 _ **For Example,**_

    
    
     _Original URL_ — https://medium.com/satyam-kulkarni/
    _Shorten Form_ — https://localhost:8000/sEqlKdsIUL

URL’s maximum length is 200 Characters and Slug’s maximum length is 15
(Considering our Website’s Address). After Creating Models for our Website,
Let’s create some Forms for taking input from User.

### Creating a Form

Create a _forms.p_ y in our Django App Folder.

fo _rms.py_

    
    
    from django import forms
    class Url(forms.Form):
        url = forms.CharField(label="URL")
    

We simply import _forms_ from _django_ and create a Class _Url_ which we will
use in _views_. _py_ and render it in our HTML. _Url_ form has only a _url_
field to take input of Original URL.

### Creating Views

Now, We will create the Interface of our App using _views_. _py_. Let’s divide
this part in Functions.

 _ **urlShort()**_ — This Function is where our _Main Algorithm_ works. It
takes a _url_ from form after User submits it, then it generates a Random Slug
which is then stored in Database with Original Url. It is also the function
which render _index_. _html_ (entrypoint of our app)

 _views.py urlShort()_

    
    
    def urlShort(request):
        if request.method == 'POST':
            form = Url(request.POST)
            if form.is_valid():
                slug = ''.join(random.choice(string.ascii_letters)
                               for x in range(10))
                url = form.cleaned_data["url"]
                new_url = UrlData(url=url, slug=slug)
                new_url.save()
                request.user.urlshort.add(new_url)
                return redirect('/')
        else:
            form = Url()
        data = UrlData.objects.all()
        context = {
            'form': form,
            'data': data
        }
        return render(request, 'index.html', context)
    
    
    

_**urlRedirect()**_ — This Function tracks the slug to Original URL and
redirects it to Original URL.

 _views.py urlRedirect()_

    
    
    def urlRedirect(request, slugs):
        data = UrlData.objects.get(slug=slugs)
        return redirect(data.url)
    

### Creating Routes

Before Running This App, We need to specify URL paths in App’s _urls.py_

 _urls.py_

    
    
    from django.urls import path
    from . import views
    app_name = "url"
    urlpatterns = [
        path("", views.urlShort, name="home"),
        path("u/<str:slugs>", views.urlRedirect, name="redirect")
    ]
    

### Run the Project

Open Console in Main Project Directory.

    
    
    python manage.py runserver
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201023014740/1Yj6cKL32MRuVT9MipFyaw-300x210.png)

### Final Project Output –

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201023014848/1wuIWxgi5BjPQafl1TnDUpA-300x223.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

