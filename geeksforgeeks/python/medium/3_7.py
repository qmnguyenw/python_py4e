How to use User model in Django?



The Django’s built-in authentication system is great. For the most part we can
use it out-of-the-box, saving a lot of development and testing effort. It fits
most of the use cases and is very safe. But sometimes we need to do some fine
adjustment so to fit our Web application. Commonly we want to store a few more
data related to our User but the next question might be that how should a
Django developer reference a User? The official Django docs list three
separate ways:

  * User
  * AUTH_USER_MODEL
  * get_user_model()

 **Explanation:**

Illustration of how to reference user model by an example. Consider a project
named **mysite** having an app name **blog**.

> Refer to the following article to check how to create a project and an app
> in Django.  
>
>
> How to Create Basic Project using MVT in Django ?  
>
>
>  
>
>
>  
>
>
> How to Create an App in Django?

 **Method 1 – User model Directly :**

Inside the models.py add the following code:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

 author = models.ForeignKey(User, on_delete=models.CASCADE)

 title = models.CharField(max_length=50)

 content= models.TextField()

 def __str__(self):

 return self.title  
  
---  
  
 __

 __

Register this model by adding the following code inside the admin.py.

    
    
    from django.contrib import admin
    from .models import Post
    
    # Register your models here.
    admin.site.register(Post)

Some kinds of projects may have authentication requirements for which Django’s
built-in User model is not always appropriate. For instance, on some sites it
makes more sense to use an email address as your identification token instead
of a username.

Django allows you to override the default user model by providing a value for
the AUTH_USER_MODEL setting that references a custom model.

 **Method 2 – AUTH_USER_MODEL :**

  

  

AUTH_USER_MODEL is the recommended approach when referring to a user model in
a models.py file.

For this you need to create custom User Model by either subclassing
AbstractUser or AbstractBaseUser.

  * AbstractUser: Use this option if you are happy with the existing fields on the User model and just want to remove the username field.
  * AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new User model.

> Refer Below Article for Creating Custom User model:  
>
>
> Creating Custom User Model

If you’ve already created a custom user model say CustomUser in an app called
users , you’d reference it in your settings.py file as follows:

    
    
    #settings.py
    
    AUTH_USER_MODEL = 'users.CustomUser'

Then in blog models.py add the following code:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# blog/models.py

from django.conf import settings

from django.db import models

 

class Post(models.Model):

 author =
models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

 title = models.CharField(max_length=50)

 content = models.TextField()  
  
---  
  
 __

 __

Register this model by adding the following code inside the admin.py.

    
    
    from django.contrib import admin
    from .models import Post
    
    # Register your models here.
    admin.site.register(Post)

 **Method 3 – get_user_model() :**

If you reference User directly (for example, by referring to it in a foreign
key), your code will not work in projects where the AUTH_USER_MODEL setting
has been changed to a different user model.

The other way to reference the user model is via get_user_model which returns
the currently active user model: either a custom user model specificed in
AUTH_USER_MODEL or else the default built-in User.

Inside the models.py add the following code:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class Post(models.Model):

 author = models.ForeignKey(User, on_delete=models.CASCADE)

 title = models.CharField(max_length=50)

 content= models.TextField()

 def __str__(self):

 return self.title  
  
---  
  
 __

 __

Register this model by adding the following code inside the admin.py.

    
    
    from django.contrib import admin
    from .models import Post
    
    # Register your models here.
    admin.site.register(Post)

 **Output –**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201229130430/Screenshot139.png)

Creating instances with author as user

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

