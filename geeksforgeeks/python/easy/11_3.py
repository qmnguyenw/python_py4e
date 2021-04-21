BooleanField – Django Forms



BooleanField in Django Forms is a checkbox field which stores either **True**
or **False**. It is used for taking boolean inputs from the user. The default
widget for this input is CheckboxInput. It normalizes to: A Python **True** or
**False** value.

 **Syntax**

    
    
    field_name = forms.BooleanField(**options)

## Django form BooleanField Explanation

Illustration of BooleanField using an Example. Consider a project named
geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Enter the following code into forms.py file of **geeks** app.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

 

# creating a form 

class GeeksForm(forms.Form):

 geeks_field = forms.BooleanField( )  
  
---  
  
 __

 __

Add the geeks app toINSTALLED_APPS

 __

 __  
 __

 __

 __  
 __  
 __

# Application definition

 

INSTALLED_APPS = [

 'django.contrib.admin',

 'django.contrib.auth',

 'django.contrib.contenttypes',

 'django.contrib.sessions',

 'django.contrib.messages',

 'django.contrib.staticfiles',

 'geeks',

]  
  
---  
  
 __

 __

Now to render this form into a view we need a view and a URL mapped to that
URL. Let’s create a view first in views.py of geeks app,

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

from .forms import GeeksForm

 

# Create your views here.

def home_view(request):

 context = {}

 context['form'] = GeeksForm()

 return render( request, "home.html", context)  
  
---  
  
 __

 __

Here we are importing that particular form from forms.py and creating an
object of it in the view so that it can be rendered in a template.  
Now, to initiate a Django form you need to create home.html where one would be
designing the stuff as they like. Let’s create a form in home.html.

 __

 __  
 __

 __

 __  
 __  
 __

<form method = "GET">

 {{ form }}

 <input type = "submit" value = "Submit">

</form>  
  
---  
  
 __

 __

Finally, a URL to map to this view in urls.py

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path

 

# importing views from views..py

from .views import home_view

 

urlpatterns = [

 path('', home_view ),

]  
  
---  
  
 __

 __

Let’s run the server and check what has actually happened, Run

    
    
    Python manage.py runserver

![django-booleanfiled-forms](https://media.geeksforgeeks.org/wp-
content/uploads/20191121112633/django-booleanfiled-forms.png)

Thus, an geeks_field **BooleanField** is created by replacing “_” with ” “.
It is a field to store boolean values – True or False.

## How to use BooleanField ?

BooleanField is used for input of boolean values in the database. One can
input boolean fields such as is_admin, is_teacher, is_staff, etc. Till now we
have discussed how to implement BooleanField but how to use it in the view for
performing the logical part. To perform some logic we would need to get the
value entered into field into a python string instance.  
In views.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

from .forms import GeeksForm

 

# Create your views here.

def home_view(request):

 context ={}

 form = GeeksForm()

 context['form']= form

 if request.GET:

 temp = request.GET['geeks_field']

 print(temp)

 return render(request, "home.html", context)  
  
---  
  
 __

 __

Now let’s try turning on the field button.  
![django-booleanfiled-forms](https://media.geeksforgeeks.org/wp-
content/uploads/20191121112631/django-booleanfield-forms-1.png)

Now this data can be fetched using corresponding request dictionary. If method
is GET, data would be available in **request.GET** and if post,
**request.POST** correspondingly. In above example we have the value in temp
which we can use for any purpose.

![django-booleanfiled-forms](https://media.geeksforgeeks.org/wp-
content/uploads/20191121112629/django-forms-booleanfield.png)

## Core Field Arguments

Core Field arguments are the arguments given to each field for applying some
constraint or imparting a particular characteristic to a particular Field. For
example, adding an argument required = False to BooleanField will enable it
to be left blank by the user. Each Field class constructor takes at least
these arguments. Some Field classes take additional, field-specific arguments,
but the following should always be accepted:

Field Options| Description| required| By default, each Field class assumes the
value is required, so to make it not required you need to set
required=False| label| The label argument lets you specify the “human-
friendly” label for this field. This is used when the Field is displayed in a
Form.| label_suffix| The label_suffix argument lets you override the form’s
label_suffix on a per-field basis.| widget| The widget argument lets you
specify a Widget class to use when rendering this Field. See Widgets for more
information.| help_text| The help_text argument lets you specify descriptive
text for this Field. If you provide help_text, it will be displayed next to
the Field when the Field is rendered by one of the convenience Form methods.|
error_messages| The error_messages argument lets you override the default
messages that the field will raise. Pass in a dictionary with keys matching
the error messages you want to override.| validators| The validators argument
lets you provide a list of validation functions for this field.| localize| The
localize argument enables the localization of form data input, as well as the
rendered output.| disabled.| The disabled boolean argument, when set to True,
disables a form field using the disabled HTML attribute so that it won’t be
editable by users.  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

