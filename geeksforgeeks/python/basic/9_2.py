Class Based Generic Views Django (Create, Retrieve, Update, Delete)



Django is a Python-based web framework that allows you to quickly create web
applications. It has built-in admin interface which makes easy to work with
it. It is often called **Batteries included framework** because it provides
built-in facilities for every functionality. Class Based Generic Views are
advanced set of Built-in views which are used for implementation of selective
view strategies such as Create, Retrieve, Update, Delete. Class based views
simplify the use by separating GET, POST requests for a view. They do not
replace function-based views, but have certain differences and advantages when
compared to function-based views:

  * Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
  * Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.

This article revolves around complete implementation of **Class Based Views in
Django** (Create, Retrieve, Update, Delete). Let’s discuss what actually CRUD
means,

![Untitled-Diagram-316](https://media.geeksforgeeks.org/wp-
content/uploads/20200114185631/Untitled-Diagram-316-1024x630.jpg)

 **CreateView** – create or add new entries in a table in the database.  
 **Retrieve Views** – read, retrieve, search, or view existing entries as a
list( **ListView** ) or retrieve a particular entry in detail ( **DetailView**
)  
 **UpdateView** – update or edit existing entries in a table in the database  
 **DeleteView** – delete, deactivate, or remove existing entries in a table in
the database  
 **FormView** – render a form to template and handle data entered by user

## Django CRUD (Create, Retrieve, Update, Delete) Class Based Views

Illustration of **How to create and use CRUD views** using an Example.
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
    

Now we will create a Django ModelForm for this model. Refer this article for
more on modelform – Django ModelForm – Create form from Models. create a file
forms.py in geeks folder,

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

from .models import GeeksModel

 

 

# creating a form

class GeeksForm(forms.ModelForm):

 

 # create meta class

 class Meta:

 # specify model to be used

 model = GeeksModel

 

 # specify fields to be used

 fields = [

 "title",

 "description",

 ]  
  
---  
  
 __

 __

### Using Class Based Views

At its core, a class-based view allows you to respond to different HTTP
request methods with different class instance methods, instead of with
conditionally branching code inside a single view function.

So where the code to handle HTTP GET in a view function would look something
like:

 __

 __  
 __

 __

 __  
 __  
 __

from django.http import HttpResponse

 

def my_view(request):

 if request.method == 'GET':

 # <view logic>

 return HttpResponse('result')  
  
---  
  
 __

 __

In a class-based view, this would become:

 __

 __  
 __

 __

 __  
 __  
 __

from django.http import HttpResponse

from django.views import View

 

class MyView(View):

 def get(self, request):

 # <view logic>

 return HttpResponse('result')  
  
---  
  
 __

 __

Similarly inurls.py, one needs to use as_view() method to diffrentiate a
class based view from function based view.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# urls.py

from django.urls import path

from myapp.views import MyView

 

urlpatterns = [

 

 path('about/', MyView.as_view()),

 

]  
  
---  
  
 __

 __

### CreateView

Create View refers to a view (logic) to create an instance of a table in the
database. We have already discussed basics of Create View in Create View –
Function based Views Django. Class Based Views automatically setup everything
from A to Z. One just needs to specify which model to create Create View for
and the fields. Then Class based CreateView will automatically try to find a
template in app_name/modelname_form.html. In our case it is
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
To check complete implementation of Class based CreateView, visit Createview –
Class Based Views Django.

### Retrieve Views

#### ListView

List View refers to a view (logic) to display multiple instances of a table in
the database. We have already discussed basics of List View in List View –
Function based Views Django. Class Based Views automatically setup everything
from A to Z. One just needs to specify which model to create ListView for,
then Class based ListView will automatically try to find a template in
app_name/modelname_list.html. In our case it is
geeks/templates/geeks/geeksmodel_list.html. Let’s create our class based
view. In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.views.generic.list import ListView

from .models import GeeksModel

 

class GeeksList(ListView):

 

 # specify the model for list view

 model = GeeksModel  
  
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

from .views import GeeksList

urlpatterns = [

 path('', GeeksList.as_view()),

]  
  
---  
  
 __

 __

Create a template intemplates/geeks/geeksmodel_list.html,

 __

 __  
 __

 __

 __  
 __  
 __

<ul>

 <!-- Iterate over object_list -->

 {% for object in object_list %}

 <!-- Display Objects -->

 <li>{{ object.title }}</li>

 <li>{{ object.description }}</li>

 

 <hr/>

 <!-- If objet_list is empty -->

 {% empty %}

 <li>No objects yet.</li>

 {% endfor %}

</ul>  
  
---  
  
 __

 __

Let’s check what is there onhttp://localhost:8000/  
![django-listview-class-based-views](https://media.geeksforgeeks.org/wp-
content/uploads/20200116152134/django-listview-class-based-views.png)  
To check complete implementation of Class based ListView, visit ListView –
Class Based Views Django

#### DetailView

Detail View refers to a view (logic) to display one instances of a table in
the database. We have already discussed basics of Detail View in Detail View –
Function based Views Django. Class Based Views automatically setup everything
from A to Z. One just needs to specify which model to create DetailView for,
then Class based DetailView will automatically try to find a template in
app_name/modelname_detail.html. In our case it is
geeks/templates/geeks/geeksmodel_detail.html. Let’s create our class based
view. In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.views.generic.detail import DetailView

 

from .models import GeeksModel

 

class GeeksDetailView(DetailView):

 # specify the model to use

 model = GeeksModel  
  
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

from .views import GeeksDetailView

urlpatterns = [

 # <pk> is identification for id field,

 # slug can also be used

 path('<pk>/', GeeksDetailView.as_view()),

]  
  
---  
  
 __

 __

Create a template intemplates/geeks/geeksmodel_detail.html,

 __

 __  
 __

 __

 __  
 __  
 __

<h1>{{ object.title }}</h1>

<p>{{ object.description }}</p>  
  
---  
  
 __

 __

Let’s check what is there onhttp://localhost:8000/1/  
![django-detailview-class-based](https://media.geeksforgeeks.org/wp-
content/uploads/20200118000848/django-detailview-class-based.png)  
To check complete implementation of Class based DetailView, visit DetailView –
Class Based Views Django

### UpdateView

UpdateView refers to a view (logic) to update a particular instance of a table
from the database with some extra details. It is used to update enteries in
the database for example, updating an article at geeksforgeeks. We have
already discussed basics of Update View in Update View – Function based Views
Django. Class Based Views automatically setup everything from A to Z. One just
needs to specify which model to create UpdateView for, then Class based
UpdateView will automatically try to find a template in
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

To check complete implementation of Class based UpdateView, visit UpdateView –
Class Based Views Django.

### DeleteView

Delete View refers to a view (logic) to delete a particular instance of a
table from the database. It is used to delete enteries in the database for
example, deleting an article at geeksforgeeks. We have already discussed
basics of Delete View in Delete View – Function based Views Django. Class
Based Views automatically setup everything from A to Z. One just needs to
specify which model to create DeleteView for, then Class based DeleteViewde
will automatically try to find a template in
app_name/modelname_confirm_delete.html. In our case it is
geeks/templates/geeks/geeksmodel_confirm_delete.html. Let’s create our class
based view. In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

# import generic UpdateView

from django.views.generic.edit import DeleteView

 

# Relative import of GeeksModel

from .models import GeeksModel

 

class GeeksDeleteView(DeleteView):

 # specify the model you want to use

 model = GeeksModel

 

 # can specify success url

 # url to redirect after successfully

 # deleting object

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

from .views import GeeksDeleteView

urlpatterns = [

 # <pk> is identification for id field,

 # slug can also be used

 path('<pk>/delete/', GeeksDeleteView.as_view()),

]  
  
---  
  
 __

 __

Create a template intemplates/geeks/geeksmodel_confirm_delete.html,

 __

 __  
 __

 __

 __  
 __  
 __

<form method="post">{% csrf_token %}

 <p>Are you sure you want to delete "{{ object }}"?</p>

 <input type="submit" value="Confirm">

</form>  
  
---  
  
 __

 __

Let’s check what is there onhttp://localhost:8000/1/delete  
![django-deleteview-class-based-views](https://media.geeksforgeeks.org/wp-
content/uploads/20200121124942/django-deleteview-class-based-views.png).  
To check complete implementation of Class based DeleteView, visit DeleteView –
Class Based Views Django

### FormView

FormView refers to a view (logic) to display and verify a Django Form. For
example a form to register users at geeksforgeeks. Class Based Views
automatically setup everything from A to Z. One just needs to specify which
form to create FormView for and template_name, then Class based FormView will
automatically render that form. Let’s create our class based view. In
geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

# import generic FormView

from django.views.generic.edit import FormView

 

# Relative import of GeeksForm

from .forms import GeeksForm

 

class GeeksFormView(FormView):

 # specify the Form you want to use

 form_class = GeeksForm

 

 # sepcify name of template

 template_name = "geeks / geeksmodel_form.html"

 

 # can specify success url

 # url to redirect after successfully

 # updating details

 success_url ="/thanks/"  
  
---  
  
 __

 __

Create a template for this view ingeeks/geeksmodel_form.html,

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

Map a url to this view ingeeks/urls.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path

 

# importing views from views..py

from .views import GeeksFormView

urlpatterns = [

 path('', GeeksFormView.as_view()),

]  
  
---  
  
 __

 __

Now visithttp://127.0.0.1:8000/,  
![django-create-view-function-based](https://media.geeksforgeeks.org/wp-
content/uploads/20200107131257/django-create-view-function-based.png)  
To check complete implementation of Class based FormView, visit FormView –
Class Based Views Django

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

