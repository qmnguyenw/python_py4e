Create virtual environment using venv | Python



A virtual environment is a tool that helps to keep dependencies required by
different projects separate by creating isolated python virtual environments
for them. This is one of the most important tools that most of the Python
developers use.

## Need of virtual environment

Imagine a scenario where a web app is hosted on a cloud hosting service
provider with a python development environment. The configuration for the web
app comes with an option for installing the newest version of the Flask web
framework. Suppose, the web app is created on the local system with an older
version of the framework and as soon as it is uploaded on the site, there will
be a version conflict as some of the modules used are depreciated  
in the latest versions of Flask.

## Use of virtual environment

The above scenario can be solved using virtual environment. Python development
environments can be separated by making use of some virtual environment. A
virtual environment, here, is an isolated Python installation that allows to
manage dependencies and work on separate Python projects without affecting
other projects.

When a virtual environment is created, it creates a separate folder from the
global Python or other virtual environments and copies Python into it along
with a site-packages folder among a couple of others. For older versions of
Python, virtual machines require installing a third-party tool called
virtualenv. It’s been integrated into newer versions of Python3 under the
module venv. To know more about virtualenv click here.

## Implementing venv

First, check whether the pip has the same version of the interpreter as that
on the system and where the Python environment currently resides:  
To check where the python currently resides type the below command in the
terminal.

  

  

    
    
    where python
    
    where pip
    

**Output:**

> C:\Users\GeeksforGeeks\AppData\Local\Programs\Python\Python37\python.exe
>
>
> C:\Users\GeeksforGeeks\AppData\Local\Programs\Python\Python37\Scripts\pip.exe

To create a virtualenv use the following command:

    
    
    python -m venv ./venv
    

After running this command, a directory named venv will be created. This is
the directory which contains all the necessary executables to use the packages
that a Python project would need. This is where Python packages will be
installed.

To list the files in the folder type below command in the terminal:

    
    
     dir ./venv
    

**Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20191017181006/venv-
dir.png)

The pip command still points to the global environment. We need to
explicitly activate the created virtual environment to configure the current
shell session to use pip commands from the virtualenv folder and don’t end up
installing packages in the global environment:  
To activate venv first change the directory to venv\Scripts.

  

  

    
    
    cd venv\Scripts
    

After changing the directory type the below command.

    
    
    $ Source venv_name\Scripts> activate
    

Once the virtual environment is activated, the name of your virtual
environment will appear on left side of terminal. This will let you know that
the virtual environment is currently active. In the image below, venv named
virtual environment is active.

![](https://media.geeksforgeeks.org/wp-content/uploads/20191018094021/venv-
activate.png)

The Python interpreter as well would run the version from the virtual
environment and not the global one. We can verify where the Python environment
currently resides by below command:

    
    
    where python
    

**Output:**

    
    
    E:\distribution\venv\Scripts\python.exe
    C:\Users\GeeksforGeeks\AppData\Local\Programs\Python\Python37\python.exe
    

The virtual environment is an almost clean Python environment. Run pip list
to see a list with packages installed:  
 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20191017181741/pip-
list.png)

Now you can install dependencies related to the project in this virtual
environment. For example if you are using Django 1.9 for a project, you can
install it like you install other packages.

    
    
    (venv_name)$ pip install Django==1.9
    

Once you are done with the work, you can deactivate the virtual environment by
the following command:

    
    
    (venv_name)$ deactivate
    

![](https://media.geeksforgeeks.org/wp-content/uploads/20191018094604/venv-
deactivate.png)

Now you will be back to system’s default Python installation.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

