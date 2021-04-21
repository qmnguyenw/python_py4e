lorem – Django Template Tags



A Django template is a text document or a Python string marked-up using the
Django template language. Django being a powerful Batteries included framework
provides convenience to rendering data in a template. Django templates not
only allow passing data from view to template, but also provides some limited
features of programming such as variables, for loops, comments, extends,
include, lorem etc.  
This article revolves about how to use **lorem tag** in Templates. lorem tag
displays random “lorem ipsum” Latin text. This is useful for providing sample
data in templates.

###### Syntax

    
    
    {% lorem [count] [method] [random] %}
    

**count** – A number (or variable) containing the number of paragraphs or
words to generate (default is 1).  
 **method** – Either w for words, p for HTML paragraphs or b for plain-text
paragraph blocks (default is b).  
 **random** – The word random, which if given, does not use the common
paragraph (“Lorem ipsum dolor sit amet…”) when generating text.

###### Examples –

  * {% lorem %} will output the common “lorem ipsum” paragraph.
  * {% lorem 3 p %} will output the common “lorem ipsum” paragraph and two random paragraphs each wrapped in HTML

tags.

  * {% lorem 2 w random %} will output two random Latin words.

## lorem – Django template Tags Explanation

Illustration of How to use lorem tag in Django templates using an Example.
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

Now we will create s template to demonstrate **lorem tag**. Create a base
template in geeks.html,

 __

 __  
 __

 __

 __  
 __  
 __

<html>

 {% lorem %}

</html>  
  
---  
  
 __

 __

Now visithttp://127.0.0.1:8000/,

![lorem-Django-Template-Tags](https://media.geeksforgeeks.org/wp-
content/uploads/20200204130420/lorem-Django-Template-Tags.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

