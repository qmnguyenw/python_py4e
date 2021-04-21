How to create a new project in Django using Firebase Database?



 **Django**is a Python-based web framework that allows you to quickly create
efficient web applications. If you are new to Django then you can refer to
Django Introduction and Installation. Here we are going to learn How to create
a Django project using Firebase as Database .

### **How to create a new project in Firebase ?**

 **Step 1:** Firstly, We are going to **Create a project** on Firebase to
connect our static web page. Visit Firebase Page For Configuring Your Project
– https://console.firebase.google.com/u/0/?pli=1

Click On **Add Project** Button.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215337/Screenshot203.png)

 **Step 2:** Give a Name To your Project and Click On **Continue** Button.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215333/Screenshot204.png)

 **Step 3:** Now Click On **Continue** Button.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215330/Screenshot205.png)

 **Step 4:** Now Choose Default Account For Firebase and Click On **Create
Project**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215325/Screenshot206.png)

 **Step 5:** Now Your Project is created. You are Good to Go. Click on
**Continue .**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215322/Screenshot207.png)

 **Step 6:** Now Click On 3rd icon that’s **Web Button( </>)**.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215319/Screenshot208.png)

 **Step 7:** Give a nickname to your Web Project and Click On **Register App**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215316/Screenshot209.png)

 **Step 8:** Now you will see the configuration of your App like this. Copy
this Code somewhere .You wlll need it later.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215312/Screenshot210.png)

 **Step 9 :** Click On The **Realtime Database** button As Shown In Figure.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215309/Screenshot211.png)

**Step 10:** Now Click On **Create Database.**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215304/Screenshot212.png)

 **Step 11:** Now Click On **Test Mode** and then Click On **Enable**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225215300/Screenshot213.png)

Now, We will Add Some Data and will try to Retrieve that using our Website

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225220131/Screenshot362.png)

### Integrating Firebase Database to Django Project –

Now, I hope that you have already create a project in Django. If not then
Refer to How to Create a Basic Project using MVT in Django ? Since we are
using firebase as Database , We need to install pyrebase . For this Type the
following Command in terminal

    
    
    $pip install pyrebase4

Create a views.py file in your project directly. The Structure should be like
this .

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225222516/Screenshot369.png)

 **Urls.py file**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path

from . import views

 

urlpatterns = [

 path('admin/', admin.site.urls),

 path('', views.home),

]  
  
---  
  
 __

 __

 **Views.py**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render

import pyrebase

 

config={

 apiKey: "Use Your Api Key Here",

 authDomain: "Use Your authDomain Here",

 databaseURL: "Use Your databaseURL Here",

 projectId: "Use Your projectId Here",

 storageBucket: "Use Your storageBucket Here",

 messagingSenderId: "Use Your messagingSenderId Here",

 appId: "Use Your appId Here"

}

firebase=pyrebase.initialize_app(config)

authe = firebase.auth()

database=firebase.database()

 

def home(request):

 day = database.child('Data').child('Day').get().val()

 id = database.child('Data').child('Id').get().val()

 projectname =
database.child('Data').child('Projectname').get().val()

 return
render(request,"Home.html",{"day":day,"id":id,"projectname":projectname
})  
  
---  
  
 __

 __

 **Home.html**

## HTML

 __

 __  
 __

 __

 __  
 __  
 __

<!DOCTYPE html>

<html lang="en">

<head>

 <meta charset="UTF-8">

 <title>Sample Poject</title>

</head>

<body>

<H1>

Project Name is {{ projectname }}

 </H1>

<br/>

<h2>

Project Id is {{ id }}

 </h2>

<br>

<h3>

Day {{ day }}

 </h3>

<br>

</body>

</html>  
  
---  
  
 __

 __

Now move to your project directory and run our project using the given command
:

    
    
    python manage.py runserver

 **Project Output will be as Follow –**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201225222839/Screenshot370.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

