now – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow passing data from view to template, but also provides some limited
features of programming such as variables, for loops, comments, extends, now,
etc.  
This article revolves about how to use **now tag** in Templates. now tag
displays the current date and/or time, using a format according to the given
string. Such string can contain format specifiers characters as described in
the date filter section.

###### Syntax

    
    
    {% now "D M Y H T " %}

###### Example

    
    
    It is {% now "D d M Y" %}
    

Above tag will display, **Tue 04 Feb 2020**

## now – Django template Tags Explanation

Illustration of How to use now tag in Django templates using an Example.
Consider a project named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
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

 return render(request, "geeks.html.html")  
  
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

Now we will create a template to demonstrate **now tag**. Create a base
template in geeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

<html>

 It is the {% now "jS \o\f F" %}

</html>  
  
---  
  
 __

 __

Now visithttp://127.0.0.1:8000/,

![now-Django-TEmplate-TAgs](https://media.geeksforgeeks.org/wp-
content/uploads/20200204132206/now-Django-TEmplate-TAgs.png)

#### Advanced Usage

one can also use the syntax {% now "Y" as current_year %} to store the
output (as a string) inside a variable. This is useful if you want to use
{% now %} inside a template tag like blocktrans for example:

    
    
    {% now "Y" as current_year %}
    {% blocktrans %} Copyright {{ current_year }}{% endblocktrans %}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

