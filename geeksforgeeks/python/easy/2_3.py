Create a new Django project in Pycharm using Pycharm Terminal



PyCharm is one of the most popular Python-IDE developed by JetBrains used for
performing scripting in Python language. PyCharm provides many useful features
like Code completion and inspection, Debugging process, support for various
programming frameworks such as Flask and Django, Package Management, etc.
PyCharm provides various tools for productive development mainly in Python.

Django is a Python-based web framework which allows you to quickly create web
application without all of the installation or dependency problems that you
normally will find with other frameworks. It is very scalable.

Let’s Start Creating a new Django Project in PyCharm using Pycharm Terminal.

 **Step By Step Implementation**

 **Step 1:** Open Your PyCharm and Click on **Create New Project**.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220160248/Screenshot279.png)

 **Step 2:** Select Your Directory and then give a name to your project and
then Click on **Create**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220160228/Screenshot280.png)

 **Step 3 :** Then Check if Django is installed or not in your Computer.

Type the following Command in pycharm Terminal located at Bottom Left.:

    
    
    python -m django --version

If it is Already installed then you will see the Django version installed in
Your Compter. If not Then You can refer to Django Introduction and
Installation.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220160232/Screenshot282.png)

 **Step 4:** Start a project by using following command-

  

  

    
    
    django-admin startproject firstproject

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220161126/Screenshot286.png)

 **Step 5:** Change directory to firstproject.

    
    
    cd firstproject

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220160233/Screenshot283.png)

 **Step 6:** Start the server by typing following command in **cmd** –

    
    
    python manage.py runserver

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220160235/Screenshot284.png)

After You Click on the given Url **(http://127.0.0.1:8000/) .** You Will See
your Development Server as shown in Below Image.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220162029/Screenshot278.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

