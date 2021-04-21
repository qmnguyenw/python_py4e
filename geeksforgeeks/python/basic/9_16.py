Django ModelForm – Create form from Models



 **Django ModelForm** is a class that is used to directly convert a model into
a Django form. If you’re building a database-driven app, chances are you’ll
have forms that map closely to Django models. For example, a User Registration
model and form would have same quality and quantity of model fields and form
fields. So instead of creating a redundant code to first create a form and
then map it to the model in a view, we can directly use ModelForm. It takes as
argument the name of the model and converts it into a Django Form. Not only
this, ModelForm offers a lot of methods and features which automate the entire
process and help remove code redundancy.

### How to convert a model into a Django Form?

To explain the working of the project, we will use project **geeksforgeeks** ,
create a model and map it to Django forms.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Now when we have our project ready, create a model in geeks/models.py,

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

 last_modified = models.DateTimeField(auto_now_add = True)

 img = models.ImageField(upload_to = "images/")

 

 # renames the instances of the model

 # with their title name

 def __str__(self):

 return self.title  
  
---  
  
 __

 __

Now, run following commands to create the model,

  

  

    
    
    Python manage.py makemigrations
    Python manage.py migrate
    

We can check that model has been successfully created at
http://127.0.0.1:8000/admin/geeks/geeksmodel/add/,  
![django-modelform-model](https://media.geeksforgeeks.org/wp-
content/uploads/20191226121102/django-modelform-model-1024x585.png)

To create a form directly for this model, dive into geeks/forms.py and Enter
following code,

 __

 __  
 __

 __

 __  
 __  
 __

# import form class from django

from django import forms

 

# import GeeksModel from models.py

from .models import GeeksModel

 

# create a ModelForm

class GeeksForm(forms.ModelForm):

 # specify the name of model to use

 class Meta:

 model = GeeksModel

 fields = "__all__"  
  
---  
  
 __

 __

This form takes two arguments **fields** or **exclude**.

  *  **fields –** It is strongly recommended that you explicitly set all fields that should be edited in the form using the fields attribute. Failure to do so can easily lead to security problems when a form unexpectedly allows a user to set certain fields, especially when new fields are added to a model. Depending on how the form is rendered, the problem may not even be visible on the web page. Set the fields attribute to the special value **‘__all__’** to indicate that all fields in the model should be used.
  *  **exclude –** Set the exclude attribute of the ModelForm’s inner Meta class to a list of fields to be excluded from the form.

