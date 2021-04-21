Deploy Python Flask App on Heroku



Flask is a web application framework written in Python. Flask is based on the
Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.
This article revolves around **how to deploy a flask app on Heroku**. To
demonstrate this, we are first going to create a sample application for a
better understanding of the process.

#### Prequisites

  * Python
  * pip
  * Heroku CLI
  * Git

#### Deploying Flask App on Heroku

Let’s create a simple flask application first and then it can be deployed to
heroku. Create a folder named **“eflask”** and open the command line and cd
inside the **“eflask”** directory. Follow the following steps to create the
sample application for this tutorial.

 **STEP 1 :** Create a virtual environment with pipenv and install **Flask**
and **Gunicorn**.

    
    
    $ pipenv install flask gunicorn 

**STEP 2 :** Create a **“Procfile”** and write the following code.

    
    
    $ touch Procfile 

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200125194807/Screenshot-from-2020-01-25-19-47-03.png)  
**STEP 3 :** Create **“runtime.txt”** and write the following code.

  

  

    
    
    $ touch runtime.txt 

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200125194746/Screenshot-from-2020-01-25-19-47-27.png)

**STEP 4 :** Create a folder named **“app”** and enter the folder.

    
    
    $ mkdir app
    $ cd app
      

**STEP 5 :** Create a python file, **“main.py”** and enter the sample code.

    
    
     touch main.py 

__

__  
__

__

__  
__  
__

from flask import Flask

 

app = Flask(__name__)

 

@app.route("/")

def home_view():

 return "<h1>Welcome to Geeks for Geeks</h1>"  
  
---  
  
 __

 __

 **STEP 6 :** Get back to the previous directory “eflask”.Create a file
**“wsgi.py”** and insert the following code.

    
    
    $ cd ../
    $ touch wsgi.py
    

__

__  
__

__

__  
__  
__

from app.main import app

 

if __name__ == "__main__":

 app.run()  
  
---  
  
 __

 __

 **STEP 7 :** Run the vitual environment.

    
    
    $ pipenv shell 

**STEP 8 :** Initialize an empty repo, add the files in the repo and commit
all the changes.

    
    
    $ git init 
    $ git add .
    $ git commit -m "Initial Commit"
    

**STEP 9 :** Login to heroku CLI using

    
    
    heroku login

Now, Create a unique name for your Web app.

    
    
    $ heroku create eflask-app
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200125194147/Screenshot-from-2020-01-25-19-41-24.png)

**STEP 10 :** Push your code from local to the heroku remote.

    
    
    $ git push heroku master
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200125194339/Screenshot-from-2020-01-25-19-43-24.png)

Finally, web app will be deployed on http://eflask-app.herokuapp.com.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200125194948/Screenshot-from-2020-01-25-19-49-28.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

