Overriding the save method – Django Models



The save method is an inherited method from models.Model which is executed
to save an instance into a particular Model. Whenever one tries to create an
instance of a model either from admin interface or django shell, save()
function is run. We can override save function before storing the data in the
database to apply some constraint or fill some ready only fields like
SlugField.  
Technically it is not recommended to override the save method to implement
such functionalities because any error in save method lets to crash of whole
database. So either if you are perfect at writing save method and error
handling or don’t try save method and try to implement these functionalities
either in forms, views, models, etc.

## Django Overriding the Save Method Explanation

Illustration of **overriding the save method** using an Example. Consider a
project named geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Enter the following code into models.py file of **geeks** app. We will be
using CharField for experimenting for all field options. We will override the
save method to fill up the SlugField automatically.

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

 

# importing slugify from django

from django.utils.text import slugify 

 

# Create your models here.

class GeeksModel(models.Model):

 title = models.CharField(max_length = 200)

 slug = models.SlugField()

 

 def save(self, *args, **kwargs):

 self.slug = slugify(self.title)

 super(GeeksModel, self).save(*args, **kwargs)  
  
---  
  
 __

 __

Let us explain what happens in above code. **save() method** from its parent
class is to be overridden so we use **super keyword**. slugify is a function
that converts any string into a slug. so we are converting the title to form a
slug basically. Let us try to create an instance with “Gfg is the best
website”.  
![django-models-overriding-save-method](https://media.geeksforgeeks.org/wp-
content/uploads/20191105183348/django-models-overriding-save-method.png)  
Let us check what we have created in admin interface.  
![django-overriding-save-method](https://media.geeksforgeeks.org/wp-
content/uploads/20191105183352/django-overriding-save-method.png)

  

  

#### Advanced concepts with overriding the save methd

As defined in the starting of this article it is often not recommended to
override the save method. Let us check why?  
The above code recreates the slug every time the save method is used or if any
change is done to the model.  
The second reason is if one needs to change the title only but not slug since
slug is redirecting to a particular link and is ranking on some search engine.
A great issue would be created in a production server. This makes the use of
this method of validation unfortunately incorrect. There can be multiple ways
to solve above problem, one can declare slug as read-only field and then
before making any changes to slug in overridden method we can check if it is
empty. This may resolve the problem. So as recommended until you are able to
handle errors in save method, don’t override it.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

