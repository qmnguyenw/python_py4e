UpdateView – Class Based Views Django



UpdateView refers to a view (logic) to update a particular instance of a table
from the database with some extra details. It is used to update entries in the
database, for example, updating an article at geeksforgeeks. We have already
discussed basics of Update View in Update View – Function based Views Django.
Class-based views provide an alternative way to implement views as Python
objects instead of functions. They do not replace function-based views, but
have certain differences and advantages when compared to function-based views:

  * Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
  * Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.

Class based views are simpler and efficient to manage than function-based
views. A function based view with tons of lines of code can be converted into
a class based views with few lines only. This is where Object Oriented
Programming comes into impact.

## Django UpdateView – Class Based Views

Illustration of **How to create and use UpdateView** using an Example.
Consider a project named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

After you have a project and an app, let’s create a model of which we will be
creating instances through our view. In geeks/models.py,

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the standard Django Model

# from built-in library

from django.db import models

 

# declare a new model with a name "GeeksModel"

class GeeksModel(models.Model):

 

 # fields of the model

 title = models.CharField(max_length = 200)

 description = models.TextField()

 

 # renames the instances of the model

 # with their title name

 def __str__(self):

 return self.title  
  
---  
  
 __

 __

After creating this model, we need to run two commands in order to create
Database for the same.

    
    
    Python manage.py makemigrations
    Python manage.py migrate
    

Now let’s create some instances of this model using shell, run form bash,

    
    
    Python manage.py shell

Enter following commands

    
    
    >>> from geeks.models import GeeksModel
    >>> GeeksModel.objects.create(
                           title="title1",
                           description="description1").save()
    >>> GeeksModel.objects.create(
                           title="title2",
                           description="description2").save()
    >>> GeeksModel.objects.create(
                           title="title2",
                           description="description2").save()
    

Now we have everything ready for back end. Verify that instances have been
created from http://localhost:8000/admin/geeks/geeksmodel/

![django-listview-check-models-instances](https://media.geeksforgeeks.org/wp-
content/uploads/20200108120217/django-listview-check-models-instances.png)

Class Based Views automatically setup everything from A to Z. One just needs
to specify which model to create UpdateView for, then Class based UpdateView
will automatically try to find a template in app_name/modelname_form.html.
In our case it is geeks/templates/geeks/geeksmodel_form.html. Let’s create
our class based view. In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

# import generic UpdateView

from django.views.generic.edit import UpdateView

 

# Relative import of GeeksModel

from .models import GeeksModel

 

class GeeksUpdateView(UpdateView):

 # specify the model you want to use

 model = GeeksModel

 

 # specify the fields

 fields = [

 "title",

 "description"

 ]

 

 # can specify success url

 # url to redirect after successfully

 # updating details

 success_url ="/"  
  
---  
  
 __

 __

Now create a url path to map the view. In geeks/urls.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path 

 

# importing views from views..py 

from .views import GeeksUpdateView 

urlpatterns = [ 

 # <pk> is identification for id field, 

 # <slug> can also be used 

 path('<pk>/update', GeeksUpdateView.as_view()), 

]   
  
---  
  
__

__

Create a template intemplates/geeks/geeksmodel_form.html,

 __

 __  
 __

 __

 __  
 __  
 __

<form method="post"> 

 {% csrf_token %} 

 {{ form.as_p }} 

 <input type="submit" value="Save"> 

</form>   
  
---  
  
__

__

Let’s check what is there onhttp://localhost:8000/1/update/  
![django-updateview-class-based-view](https://media.geeksforgeeks.org/wp-
content/uploads/20200120134704/django-updateview-class-based-view.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

