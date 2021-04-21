How to create Abstract Model Class in Django?



Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Built by experienced developers, it takes care of
much of the hassle of Web development, so you can focus on writing your app
without needing to reinvent the wheel. It’s free and open source.

#### What is model Inheritance?

Model Inheritance in Django works almost identically to the way normal class
inheritance works in python. In this article we will revolve around how to
create abstract base class in Django Models.

 **Abstract Base Class :-**

Abstract Base Class are useful when you want to put some common information
into a number of other models. You write your base class and put abstract =
True in the Meta Class. Suppose you have two model Student and Teacher.

 **models.py**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

 

 

class Student(models.Model): # STUDENT

 name = models.CharField(max_length=100)

 rollno = models.IntergerField()

 

 

class Teacher(models.Model): # TEACHER

 name = models.CharField(max_length=100)

 ID = models.IntergerField()  
  
---  
  
 __

 __

So have you notice that one field name is common on both models.

So instead of adding common fields in both models ,we have create a another
model and put those common fields in that model.

 **models.py**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

 

 

class common(models.Model): # COMM0N

 name = models.CharField(max_length=100)

 

 class Meta:

 abstract = True  
  
---  
  
 __

 __

So here I create a model common and put the common fields in that model.

Put abstract = True in the Meta class. After set abstract True, now it becomes
an abstract class not a model,so now you can’t generate a database table.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Student(common): # STUDENT

 rollno = models.IntegerField()

 

 

class Teacher(common): # TEACHER

 ID = models.IntegerField()  
  
---  
  
 __

 __

Ubuntu

    
    
    python3 manage.py makemigrations
    
    
    python3 manage.py migrate

Now you can inherit the common name field in both Student and Teacher. Just
like normal python inheritance.

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210121234732/Screenshotfrom20210121234546.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

