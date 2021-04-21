How to Create an App in Django ?



 **Prerequisite –**How to Create a Basic Project using MVT in Django?

Django is famous for its unique and fully managed app structure. For every
functionality, an app can be created like a completely independent module.
This article will take you through how to create a basic app and add
functionalities using that app.  
For example, if you are creating a Blog, Separate modules should be created
for Comments, Posts, Login/Logout, etc. In Django, these modules are known as
apps. There is a different app for each task.  

### Benefits of using Django apps –

  * Django apps are reusable i.e. a Django app can be used with multiple projects.
  * We have loosely coupled i.e. almost independent components
  * Multiple developers can work on different components
  * Debugging and code organization is easy. Django has an excellent debugger tool.

 **Pre-installed apps –**  
Django provides some pre-installed apps for users. To see pre-installed apps,
navigate to projectName –> projectName –> settings.py  
In your settings.py file, you will find INSTALLED_APPS. Apps listed in
INSTALLED_APPS are provided by Django for developers comfort.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190923140305/Screenshot-from-2019-09-23-14-02-16.png)

  

  

#### Also, Visit :

Django ORM – Inserting, Updating & Deleting Data  

### Creating an App in Django :

Let us start building an app.

**_Method-1_**

  * To create a basic app in your Django project you need to go to the directory containing manage.py and from there enter the command :   

    
    
    python manage.py startapp projectApp

**_Method-2_**

  * To create a basic app in your Django project you need to go to the directory containing manage.py and from there enter the command :

    
    
    django-admin startapp projectApp

Now you can see your directory structure as under :  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190923142649/directory-structure-of-app-django.png)

  * To consider the app in your project you need to specify your project name in INSTALLED_APPS list as follows in settings.py:   

## Python3

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

 'projectApp'

]  
  
---  
  
 __

 __

  * So, we have finally created an app but to render the app using URLs we need to include the app in our main project so that URLs redirected to that app can be rendered. Let us explore it.   
Move to projectName-> projectName -> urls.py and add below code in the header  

    
    
    from django.urls import include

  * Now in the list of URL patterns, you need to specify app name for including your app URLs. Here is the code for it –   

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path, include

urlpatterns = [

 path('admin/', admin.site.urls),

 # Enter the app name in following

 # syntax for this to work

 path('', include("projectApp.urls")),

]  
  
---  
  
 __

 __

  * Now You can use the default MVT model to create URLs, models, views, etc. in your app and they will be automatically included in your main project.  

The main feature of Django Apps is independence, every app functions as an
independent unit in supporting the main project.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

