url – Django Template Tag



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow passing data from view to template, but also provides some limited
features of programming such as variables, for loops, comments, extends, url,
etc.  
This article revolves about how to use **url tag** in Templates. url tag
Returns an absolute path reference (a URL without the domain name) matching a
given view and optional parameters. This is a way to output links without
violating the DRY principle by having to hard-code URLs in your templates:

###### Syntax

    
    
    {% url 'some-url-name' v1 v2 %}
    

The first argument is a URL pattern name. It can be a quoted literal or any
other context variable. Additional arguments are optional and should be space-
separated values that will be used as arguments in the URL.

###### Example

    
    
    {% url 'template1' %}
    

## url – Django template Tags Explanation

Illustration of How to use url tag in Django templates using an Example.
Consider a project named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Now create two views through which we will access the template,  
In geeks/views.py,

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import Http Response from django

from django.shortcuts import render

 

# create a function

def geeks_view(request):

 # return response

 return render(request, "geeks.html")

 

def nav_view(request):

 # return response

 return render(request, "nav.html")  
  
---  
  
 __

 __

Create a url path to map to this view. URLs need to have a name which then can
be used in templates and with **url tag**. In geeks/urls.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path

 

# importing views from views..py

from .views import geeks_view, nav_view

 

urlpatterns = [

 path('1/', geeks_view, name = "template1"),

 path('2/', nav_view, name = "template2"),

]  
  
---  
  
 __

 __

Now we will create two templates to demonstrate **now tag**. Create a template
in geeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

<html>

<h1>Template 1</h1>

<!-- Link to template 2 -->

<a href = "{% url 'template2' %}">Go to template 2</a>

</html>  
  
---  
  
 __

 __

Create a template ingeeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

<html>

<<h2>Template 2</h2>

<!-- Link to template 1 -->

<a href = "{% url 'template1' %}">Go to template 1</a>

</html>  
  
---  
  
 __

 __

Now visithttp://127.0.0.1:8000/1,

![url-django-template-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200205115549/url-django-template-tags.png)  
Click on the link and it willl redirect to other url.

![url-djago-templtae-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200205115547/url-djago-templtae-tags.png)

#### Advanced Usage

suppose you have a view, **app_views.client** , whose URLconf takes a client
ID (here, client() is a method inside the views file app_views.py). The
URLconf line might look like this:

    
    
    path('client/<int:id>/', app_views.client, name='app-views-client')

If this app’s URLconf is included into the project’s URLconf under a path such
as this:

    
    
    path('clients/', include('project_name.app_name.urls'))

…then, in a template, you can create a link to this view like this:

    
    
    {% url 'app-views-client' client.id %}

The template tag will output the string **/clients/client/123/.**

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

