for loop – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow paassing data from view to template, but also provides some limited
features of a programming such as variables, for loops, comments, extends etc.  
This article revolves about how to use **for tag** in Templates. **for tag**
loops over each item in an array, making the item available in a context
variable.

###### Syntax

    
    
    {% for i in list %}
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

{% endfor %}

</ul>  
  
---  
  
 __

 __

## for – Django template Tags Explanation

Illustration of How to use for tag in Django templates using an Example.
Consider a project named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
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

#### Advanced Usage

One can use variables, too. For example, if you have two template variables,
rowvalue1 and rowvalue2, you can alternate between their values like this:

 __

 __  
 __

 __

 __  
 __  
 __

{% for o in some_list %}

 <tr class="{% cycle rowvalue1 rowvalue2 %}">

 ...

 </tr>

{% endfor %}  
  
---  
  
 __

 __

#### Advanced Usage

One can loop over a list in reverse by using {% for obj in list reversed %}.

If you need to loop over a list of lists, you can unpack the values in each
sublist into individual variables. For example, if your context contains a
list of (x, y) coordinates called points, you could use the following to
output the list of points:

    
    
    {% for x, y in points %}
        There is a point at {{ x }}, {{ y }}
    {% endfor %}

This can also be useful if you need to access the items in a dictionary. For
example, if your context contained a dictionary data, the following would
display the keys and values of the dictionary:

    
    
    {% for key, value in data.items %}
        {{ key }}: {{ value }}
    {% endfor %}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

