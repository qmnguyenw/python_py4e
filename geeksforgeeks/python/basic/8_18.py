extends – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow paassing data from view to template, but also provides some limited
features of a programming such as variables, for loops, comments, extends etc.  
This article revolves about how to use **extends tag** in Templates. extends
tag is used for inheritance of templates in django. One needs to repeat the
same code again and again. Using extends we can inherit templates as well as
variables.

###### Syntax

    
    
    
    {% extends 'template_name.html' %}
    
    

###### Example

assume the following directory structure:

    
    
    dir1/
        template.html
        base2.html
        my/
            base3.html
    base1.html

In template.html, the following paths would be valid:

 __

 __  
 __

 __

 __  
 __  
 __

{% extends "./base2.html" %}

{% extends "../base1.html" %}

{% extends "./my/base3.html" %}  
  
---  
  
 __

 __

## extends – Django template Tags Explanation

Illustration of How to use extends tag in Django templates using an Example.
Consider a project named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>  
>
>
>  
>
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Now create a view through which we will access the template,  
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

 return render(request, "extendedgeeks.html")  
  
---  
  
 __

 __

Create a url path to map to this view. Ingeeks/urls.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path

 

# importing views from views.py

from .views import geeks_view

 

urlpatterns = [

 path('', geeks_view),

]  
  
---  
  
 __

 __

extends is always used with block tags so that can be inherited and
overriden. Create a template as base template in templates/geeks.html.

 __

 __  
 __

 __

 __  
 __  
 __

<h1>Main Template</h1>

 

{% block content %}

{% endblock %}  
  
---  
  
 __

 __

Now create a template which will use geeks.html as base template. Create a new
templateextendedgeeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

{% extends "geeks.html" %}

 

{% block content %}

<h2> GeeksForGeeks is the Best

{% endblock %}  
  
---  
  
 __

 __

Let’s check if data is displayed from both the templates
inextendedgeeks.html  
![extends-django-templates-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200130165644/extends-django-templates-tags.png)

#### Advanced Usage

{% extends variable %} uses the value of variable. If the variable evaluates
to a string, Django will use that string as the name of the parent template.
If the variable evaluates to a Template object, Django will use that object as
the parent template.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

