Initial form data – Django Forms



After creating a Django Form, if one requires some or all fields of the form
be filled with some initial data, one can use functionality of Django forms to
do so. It is not the same as a placeholder, but this data will be passed into
the view when submitted. There are multiple methods to do this, most common
being to pass the data dictionary when we initialize the form in Django view.
Other methods include passing initial values through form fields or overriding
the __init__ method.

### How to pass initial data to a Django form ?

Illustration of passing initial data using an Example. Consider a project
named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Now let’s create a demo form in “geeks/forms.py”,

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

 

// creating a django form

class GeeksForm(forms.Form):

 title = forms.CharField()

 description = forms.CharField()

 available = forms.BooleanField()

 email = forms.EmailField()  
  
---  
  
 __

 __

Now to render this form we need to create the view and template which will be
used to display the form to user. In geeks/views.py, create a view

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

from .forms import GeeksForm

 

# creating a home view

def home_view(request):

 context = {}

 form = GeeksForm(request.POST or None)

 context['form'] = form

 return render(request, "home.html", context)  
  
---  
  
 __

 __

and in templates/home.html,

 __

 __  
 __

 __

 __  
 __  
 __

<form method="POST">

 {% csrf_token %}

 {{ form.as_p }}

 <input type="submit" value="Submit">

</form>  
  
---  
  
 __

 __

Now let’s display the form by running

    
    
    Python manage.py runserver

visit http://127.0.0.1:8000/  
![initial-form-data-django-forms](https://media.geeksforgeeks.org/wp-
content/uploads/20191223131629/initial-form-data-django-forms.png)

### Method 1 – Adding initial form data in views.py

This first and most commonly used method to add initial data through a
dictionary is in view.py during the initialization of a form. Here is the code
of views.py with some added data.

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

from .forms import GeeksForm

 

def home_view(request):

 context ={}

 

 # dictionary for initial data with 

 # field names as keys

 initial_dict = {

 "title" : "My New Title",

 "description" : " A New Description",

 "available":True,

 "email":"abc@gmail.com"

 }

 

 # add the dictionary during initialization

 form = GeeksForm(request.POST or None, initial =
initial_dict)

 

 context['form']= form

 return render(request, "home.html", context)  
  
---  
  
 __

 __

Now openhttp://127.0.0.1:8000/. This method is senior of all and will override
any data provided during other methods.  
![initial-data-django-forms](https://media.geeksforgeeks.org/wp-
content/uploads/20191223132248/initial-data-django-forms.png)

### Method 2 – Adding initial form data using fields in forms.py

One can add initial data using fields in forms.py. An attribute **initial** is
there for this purpose.  
In forms.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

 

class GeeksForm(forms.Form):

 # adding initial data using initial attribute

 title = forms.CharField(initial = "Method 2 ")

 description = forms.CharField(initial = "Method 2 description")

 available = forms.BooleanField(initial = True)

 email = forms.EmailField(initial = "abc@gmail.com")  
  
---  
  
 __

 __

Now visit,http://127.0.0.1:8000/. One can see the data being updated to method
2.

![django-forms-initial-data-method-2](https://media.geeksforgeeks.org/wp-
content/uploads/20191223132803/django-forms-initial-data-method-2.png)

This way one can add initial data to a form in order to ease the work by a
user or any related purpose. This data will be passed to models or views as
defined by user and would act as normal data entered by user in the form.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

