Python Virtual Environment | Introduction



A virtual environment is a tool that helps to keep dependencies required by
different projects separate by creating isolated python virtual environments
for them. This is one of the most important tools that most of the Python
developers use.

 **Why do we need a virtual environment?**

Imagine a scenario where you are working on two web based python projects and
one of them uses a Django 1.9 and the other uses Django 1.10 and so on. In
such situations virtual environment can be really useful to maintain
dependencies of both the projects.

 **When and where to use a virtual environment?**

By default, every project on your system will use these same directories to
store and retrieve site packages (third party libraries). How does this
matter? Now, in the above example of two projects, you have two versions of
Django. This is a real problem for Python since it can’t differentiate between
versions in the “site-packages” directory. So both v1.9 and v1.10 would reside
in the same directory with the same name. This is where virtual environments
come into play. To solve this problem, we just need to create two separate
virtual environments for both the projects.The great thing about this is that
there are no limits to the number of environments you can have since they’re
just directories containing a few scripts.

  

  

Virtual Environment should be used whenever you work on any Python based
project. It is generally good to have one new virtual environment for every
Python based project you work on. So the dependencies of every project are
isolated from the system and each other.

 **How does a virtual environment work?**

We use a module named **virtualenv** which is a tool to create isolated Python
environments. virtualenv creates a folder which contains all the necessary
executables to use the packages that a Python project would need.

 **Installing virtualenv**

    
    
    $ pip install virtualenv
    

Test your installation:

    
    
    $ virtualenv --version
    

**Using virtualenv**

You can create a virtualenv using the following command:

    
    
    $ virtualenv my_name
    

After running this command, a directory named my_name will be created. This is
the directory which contains all the necessary executables to use the packages
that a Python project would need. This is where Python packages will be
installed.  
If you want to specify Python interpreter of your choice, for example Python
3, it can be done using the following command:

  

  

    
    
    $ virtualenv -p /usr/bin/python3 virtualenv_name
    

To create a Python 2.7 virtual environment, use the following command:

    
    
    $ virtualenv -p /usr/bin/python2.7 virtualenv_name
    

Now after creating virtual environment, you need to activate it. Remember to
activate the relevant virtual environment every time you work on the project.
This can be done using the following command:

    
    
    $ source virtualenv_name/bin/activate
    

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2017-06-02-03-02-49.png)

Once the virtual environment is activated, the name of your virtual
environment will appear on left side of terminal. This will let you know that
the virtual environment is currently active. In the image below, venv named
virtual environment is active.  
Now you can install dependencies related to the project in this virtual
environment. For example if you are using Django 1.9 for a project, you can
install it like you install other packages.

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2017-06-02-03-03-07.png)

    
    
    (virtualenv_name)$ pip install Django==1.9
    

The Django 1.9 package will be placed in virtualenv_name folder and will be
isolated from the complete system.  
Once you are done with the work, you can deactivate the virtual environment by
the following command:

    
    
    (virtualenv_name)$ deactivate
    

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2017-06-02-03-40-53.png)  
Now you will be back to system’s default Python installation.

This article is contributed by **Mayank Agrawal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

