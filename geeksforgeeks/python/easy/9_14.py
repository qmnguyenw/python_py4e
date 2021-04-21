firstof – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow paassing data from view to template, but also provides some limited
features of a programming such as variables, for loops, comments, firstof,
etc.  
This article revolves about how to use **firstof tag** in Templates.
**firstof** tag Outputs the first argument variable that is not “false”
(i.e. exists, is not empty, is not a false boolean value, and is not a zero
numeric value). Outputs nothing if all the passed variables are “false”.

###### Syntax

    
    
    
    {% firstof var1 var2 var3... %}
    
    

###### Example

    
    
    {% firstof var1 var2 var3 %}

This is equivalent to:

    
    
    {% if var1 %}
        {{ var1 }}
    {% elif var2 %}
        {{ var2 }}
    {% elif var3 %}
        {{ var3 }}
    {% endif %}

One can also use a literal string as a fallback value in case all passed
variables are False:

    
    
    {% firstof var1 var2 var3 "fallback value" %}

## firstof – Django template Tags Explanation

Illustration of How to use firstof tag in Django templates using an Example.
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

# import Http Response from django

from django.shortcuts import render

 

# create a function

def geeks_view(request):

 # create a dictionary

 context = {

 "var1":None,

 "var2":None,

 "var3":"GeeksForGeeks"

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

Create a template intemplates/geeks.html.

 __

 __  
 __

 __

 __  
 __  
 __

<h3>Variable displayed : </h3>

 

{% firstof var1 var2 var3 %}  
  
---  
  
 __

 __

Let’s check if data is displayed from the third variable ingeeks.html  
![firstof-Django-template-tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200130171455/firstof-Django-template-tags.png)

#### Advanced Usage

This tag auto-escapes variable values. You can disable auto-escaping with:

    
    
    {% autoescape off %}
        {% firstof var1 var2 var3 " **fallback value** " %}
    {% endautoescape %}

Or if only some variables should be escaped, you can use:

    
    
    {% firstof var1 var2|safe var3 " **fallback value** "|safe %}

You can use the syntax {% firstof var1 var2 var3 as value %} to store the
output inside a variable.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

