if – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow paassing data from view to template, but also provides some limited
features of a programming such as variables, for loops, comments, extends, if
else etc.  
This article revolves about how to use **if tag** in Templates. The {% if %}
tag evaluates a variable, and if that variable is “ **true** ” (i.e. exists,
is not empty, and is not a false boolean value) the contents of the block are
output.

###### Syntax

    
    
    {% if variable %}
    // statements
    {% else %}
    // statements
    {% endif %}
    

###### Example

 __

 __  
 __

 __

 __  
 __  
 __

{% if athlete_list %}

 Number of athletes: {{ athlete_list|length }}

{% elif athlete_in_locker_room_list %}

 Athletes should be out of the locker room soon!

{% else %}

 No athletes.

{% endif %}  
  
---  
  
 __

 __

In the above, if athlete_list is not empty, the number of athletes will be
displayed by the{{ athlete_list|length }} variable.

As one can see, the if tag may take one or several {% elif %} clauses, as
well as an {% else %} clause that will be displayed if all previous
conditions fail. These clauses are optional.

## if – Django template Tags Explanation

Illustration of How to use if tag in Django templates using an Example.
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

Now create a view through which we will pass the context dictionary,  
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

 # create a dictionary

 context = {

 "data" : 99,

 }

 # return response

 return render(request, "geeks.html", context)  
  
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

Create a template intemplates/geeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

{% if data %}

Value in data is : - {{ data }}

{% else %}

Data is empty

{% endif%}  
  
---  
  
 __

 __

Let’s check what is displayed on “/” are displayed in the template.  
![if-django-template-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200131115749/if-django-template-tags.png)

### {% else %}

Let’s check if {% else %} statement is working or not.  
Now let’s pass an empty array and use empty tag along with for tag.  
In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

## import Http Response from django

from django.shortcuts import render

 

# create a function

def geeks_view(request):

 # create a dictionary

 context = {

 "data" : False,

 }

 # return response

 return render(request, "geeks.html", context)  
  
---  
  
 __

 __

Now, checkhttp://127.0.0.1:8000/,  
![empty-tag-Django-template-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200131123820/empty-tag-Django-template-tags.png)

### Advanced Usage

if tags may use and, or or not to test a number of variables or to negate a
given variable:

    
    
    {% if athlete_list and coach_list %}
        Both athletes and coaches are available.
    {% endif %}
    
    {% if not athlete_list %}
        There are no athletes.
    {% endif %}
    
    {% if athlete_list or coach_list %}
        There are some athletes or some coaches.
    {% endif %}
    
    {% if not athlete_list or coach_list %}
        There are no athletes or there are some coaches.
    {% endif %}
    
    {% if athlete_list and not coach_list %}
        There are some athletes and absolutely no coaches.
    {% endif %}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

