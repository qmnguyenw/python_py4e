for … empty loop – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow paassing data from view to template, but also provides some limited
features of a programming such as variables, for loops, comments, extends etc.  
This article revolves about how to use **for tag with empty** in Templates.
**for tag** loops over each item in an array, making the item available in a
context variable. The for tag can take an optional {% empty %} clause whose
text is displayed if the given array is empty or could not be found. This is
basically used as a condition to be followed to check **if queryset is empty**
and what action to be performed in the same scenario.

###### Syntax

    
    
    {% for i in list %}
    // Do this in non - empty condition
    {% empty %}
    // Do this in empty condition
    {% endfor %}
    

###### Example

For example, to display a list of athletes provided in athlete_list:

 __

 __  
 __

 __

 __  
 __  
 __

<ul>

{% for athlete in athlete_list %}

 <li>{{ athlete.name }}</li>

{% empty %}

 <li>Sorry, no athletes in this list.</li>

{% endfor %}

</ul>  
  
---  
  
 __

 __

The above is equivalent to – but shorter, cleaner, and possibly faster than –
the following:

 __

 __  
 __

 __

 __  
 __  
 __

<ul>

 {% if athlete_list %}

 {% for athlete in athlete_list %}

 <li>{{ athlete.name }}</li>

 {% endfor %}

 {% else %}

 <li>Sorry, no athletes in this list.</li>

 {% endif %}

</ul>  
  
---  
  
 __

 __

## for … empty – Django template Tags Explanation

Illustration of How to use for …empty tag in Django templates using an
Example. Consider a project named geeksforgeeks having an app named geeks.

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

 "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9,
10],

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

{% for i in data %}

 <div class="row">

 {{ i }}

 </div>

{% endfor %}  
  
---  
  
 __

 __

Let’s check what is displayed on “/” are displayed in the template.  
![cycle-django-template-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200129122627/cycle-django-template-tags.png)  
Anything enclosed between for tag would be repeated, the number of times the
loop is run.

Now let’s pass an empty array and use empty tag along with for tag.  
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

 "data" : [],

 }

 # return response

 return render(request, "geeks.html", context)  
  
---  
  
 __

 __

Now intemplates/geeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

{% for i in data %}

 <div class="row">

 {{ i }}

 </div>

 {% empty %}

 <h4>There is nothing in this list</h4>

{% endfor %}  
  
---  
  
 __

 __

Now, checkhttp://127.0.0.1:8000/,  
![for-empty-django-template-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200131112336/for-empty-django-template-tags.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

