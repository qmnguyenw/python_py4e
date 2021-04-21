How to Deploy Django project on PythonAnywhere?



Django has become one of popular frameworks over the past few years. Often,
after creating your django project, you are confused, how to share it with
people around you. This article revolves around how you can host your django
application on pythonanywhere for free. So let’s get started ..!!

### Step 1: Setup your Django Project (Local Changes)

Let’s create a simple application in Django for showing the deployment.

  * Initialize your Django Project 

    
    
    django-admin startproject deploy_on_pythonanywhere
    
    

  * Open project in your editor and under settings.py make:

    
    
    ALLOWED_HOSTS = ['*']
    

  * Create requirements.txt file using the command

    
    
    pip3 freeze > requirements.txt
    
    

  * File structure of our project looks like this:

    
    
    deploy_on_pythonanywhere
    ├── db.sqlite3
    ├── deploy_on_pythonanywhere
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── settings.cpython-38.pyc
    │   │   ├── urls.cpython-38.pyc
    │   │   └── wsgi.cpython-38.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── requirements.txt
    
    

  * Let’s Start our Django Server

    
    
    cd deploy_on_pythonanywhere
    python3 manage.py runserver
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117212718/MuThJ1bDR-660x361.png)

Yahooooo, your server is running on localhost 🙂 But wait, wait… that’s not
over, let’s make it live for the world

### Step 2: Upload Project to GitHub

  * Follow this link to push the project on github – How to Upload a Project on Github?

### Step 3: Deploy Project on pythonanywhere

  * Create an account on pythonanywhere – Click Here
  * After Register, you can see the page like this

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117213610/1TIKlZ5Nj-660x324.png)

  

  

  * Now click on Console then select Bash you’ll see like this

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117213826/2X1DkyzD7-660x324.png)

  *  **Run following commands on bash:**
  * Clone GitHub repo

    
    
    git clone https://github.com/Prakhar-Mangal/deploy_on_pythonanywhere.git
    

  * Now create and setup environment variables

    
    
    python3 -m venv env #create virtual environment
    source env/bin/activate #activate virtual environment
    cd deploy_on_pythonanywhere #navigate inside your project 
    pip install -r requirements.txt #installing dependencies using requirements.txt
    

  * Now copy the path of your directories which you installed on bash
  * Type command on bash

    
    
    cd
    ls # get list of directories
    pwd #copy the path for future use
    
    

  * Here it looks like:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117214245/b0HPXtGh0-300x148.png)

Hurree, we set up our project successfully : ) But wait wait, follow the final
process and we’re ready to go

  * Now click on Web then select Add a new web app

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117214348/laQ8DY2yH-660x359.png)

  *  **Click on next and follow the procedure**
  * select Django as the framework

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117214553/bKLw4iUS.png)

  * Select python3.8 (latest) and click on next till last.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117214705/sAIVypFlJ.png)

  * Now under the Web section open the WSGI configuration file

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117214752/I4SULdcq-660x153.png)

  * Edit WSGI configuration file on line no. 12 and 17 remove the word **mysite** with your project name which you cloned from GitHub, in my case it is **deploy_on_pythonanywhere**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117214923/TDk1L3PEd.png)

  

  

  * Now it looks like this and then click on save:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117215027/TxhmMezct.png)

  * Select Virtualenv section under Web:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117215114/kwYBwMzVr.png)

  * Enter the path of Virtualenv as we created using bash (refer above pwd command for path)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117215206/95t6liIf2.png)

  * Click on Reload under the Web section and visit the link

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201117215258/QJjDj7w1y.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

