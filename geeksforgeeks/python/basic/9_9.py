List View – Function based Views Django



List View refers to a view (logic) to list all or particular instances of a
table from the database in a particular order. It is used to display multiple
types of data on a single page or view, for example, products on an eCommerce
page. Django provides extra-ordinary support for List Views but let’s check
how it is done manually through a function-based view. This article revolves
around list View which involves concepts such as Django Forms, Django Models.  
For List View, we need a project with some models and multiple instances which
will be displayed.

## Django List View – Function Based Views

Illustration of **How to create and use List view** using an Example. Consider
a project named geeksforgeeks having an app named geeks.

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
    

Now we have everything ready for back end. Verify that instnaces have been
created from http://localhost:8000/admin/geeks/geeksmodel/

![django-listview-check-models-instances](https://media.geeksforgeeks.org/wp-
content/uploads/20200108120217/django-listview-check-models-instances.png)

Let’s create a view and template for the same. In geeks/views.py,

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

 

# relative import of forms

from .models import GeeksModel

 

 

def list_view(request):

 # dictionary for initial data with 

 # field names as keys

 context ={}

 

 # add the dictionary during initialization

 context["dataset"] = GeeksModel.objects.all()

 

 return render(request, "list_view.html", context)  
  
---  
  
 __

 __

Create a template intemplates/list_view.html,

 __

 __  
 __

 __

 __  
 __  
 __

<div class="main">

 

 {% for data in dataset %}.

 

 {{ data.title }}<br/>

 {{ data.description }}<br/>

 <hr/>

 

 {% endfor %}

 

</div>  
  
---  
  
 __

 __

Let’s check what is there onhttp://localhost:8000/  
![django-listview-function-based](https://media.geeksforgeeks.org/wp-
content/uploads/20200108120919/django-listview-function-based.png)

Bingo..!! list view is working fine. One can also display filtered items or
order them in different orders based on various features. Let’s order the
items in reverse manner.  
In geeks/views.py,

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

 

# relative import of models

from .models import GeeksModel

 

 

def list_view(request):

 # dictionary for initial data with 

 # field names as keys

 context ={}

 

 # add the dictionary during initialization

 context["dataset"] =
GeeksModel.objects.all().order_by("-id")

 

 return render(request, "list_view.html", context)  
  
---  
  
 __

 __

#### order_by to arrange instances in diffrent orders

Now visit http://localhost:8000/  
![django-listview-order-by](https://media.geeksforgeeks.org/wp-
content/uploads/20200108121345/django-listview-order-by.png)

#### filter to show selective instances

Let’s create a diffrent instance to show how filter works. Run

    
    
    Python manage.py shell

Now, create another instance,

    
    
    from geeks.models import GeeksModel
    GeeksModel.objects.create(title = "Naveen", description = "GFG is Best").save()
    

Now visit http://localhost:8000/  
![django-listview-models](https://media.geeksforgeeks.org/wp-
content/uploads/20200108122001/django-listview-models.png)  
Let’s filter this data to those containing word “title” in their title.  
In **geeks/views.py** ,

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

 

# relative import of forms

from .models import GeeksModel

 

 

def list_view(request):

 # dictionary for initial data with 

 # field names as keys

 context ={}

 

 # add the dictionary during initialization

 context["dataset"] = GeeksModel.objects.all().filter(

 title__icontains = "title"

 )

 

 return render(request, "list_view.html", context)  
  
---  
  
 __

 __

Now visithttp://localhost:8000/ again,  
![django-listview-function-based2](https://media.geeksforgeeks.org/wp-
content/uploads/20200108122144/django-listview-function-based2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

