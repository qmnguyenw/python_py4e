Createview – Class Based Views Django



Create View refers to a view (logic) to create an instance of a table in the
database. We have already discussed basics of Create View in Create View –
Function based Views Django. Class-based views provide an alternative way to
implement views as Python objects instead of functions. They do not replace
function-based views, but have certain differences and advantages when
compared to function-based views:

  * Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
  * Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.

Class based views are simpler and efficient to manage than function-based
views. A function based view with tons of lines of code can be converted into
a class based views with few lines only. This is where Object Oriented
Programming comes into impact.

## Django Create View – Class Based Views

Illustration of **How to create and use create view** using an Example.
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
    

Class Based Views automatically setup everything from A to Z. One just needs
to specify which model to create Create View for and the fields. Then Class
based CreateView will automatically try to find a template in
app_name/modelname_form.html. In our case it is
geeks/templates/geeks/geeksmodel_form.html. Let’s create our class based
view. In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.views.generic.edit import CreateView

from .models import GeeksModel

 

class GeeksCreate(CreateView):

 

 # specify the model for create view

 model = GeeksModel

 

 # specify the fields to be displayed

 

 fields = ['title', 'description']  
  
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

from .views import GeeksCreate

urlpatterns = [

 path('', GeeksCreate.as_view() ),

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

<form method="POST" enctype="multipart/form-data">

 

 <!-- Security token -->

 {% csrf_token %}

 

 <!-- Using the formset -->

 {{ form.as_p }}

 

 <input type="submit" value="Submit">

</form>  
  
---  
  
 __

 __

Let’s check what is there onhttp://localhost:8000/  
![django-create-view-function-based](https://media.geeksforgeeks.org/wp-
content/uploads/20200107131257/django-create-view-function-based.png)

Now let’s try to enter data in this form,  
![create-view-function-enter-data](https://media.geeksforgeeks.org/wp-
content/uploads/20200107131255/create-view-function-enter-data.png)

Bingo.! Create view is working and we can verify it using the instance created
through the admin panel.  
![django-mopdel-created-create-view](https://media.geeksforgeeks.org/wp-
content/uploads/20200107131253/django-mopdel-created-create-view.png)  
This way one can create create view for a model in Django.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

