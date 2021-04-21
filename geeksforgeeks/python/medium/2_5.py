How to use Flask-Session in Python Flask ?



Install the extension with the following command

    
    
    $ easy_install Flask-Session

 **Alternatively** , if you have pip installed

    
    
    $ pip install Flask-Session

### Configuring Session in Flask

  * The Session instance is not used for direct access, you should always use flask_session.
  * The First line (session) from the flask is in such a way that each of us as a user gets our own version of the session.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask, render_template, redirect, request, session

from flask_session import Session  
  
---  
  
 __

 __

This specific to the flask_session library only

  

  

  *  **SESSION_PERMANENT = False –** So this session has a default time limit of some number of minutes or hours or days after which it will expire.
  *  **SESSION_TYPE = “filesystem” –** It will store in the hard drive (these files are stored under a /flask_session folder in your config directory.) or any online ide account and it is an alternative to using a Database or something else like that.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

app= Flask(__name__)

app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "filesystem"

Session(app)  
  
---  
  
 __

 __

### Remember User After Login

So we will start making two basic pages **** and their route called
**index.html** and **login.html**

  *  **login.html** contains a form in which the user can fill their name and submit 
  * **index.html** is the main page 

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

@app.route("/")

def index():

 return render_template('index.html')

 

 

@app.route("/login", methods=["POST", "GET"])

def login():

 return render_template("login.html")  
  
---  
  
 __

 __

  * We need to record the username in the session when they submit the form
  * And we are using a dictionary in python where “name” is the key = request.form.get(“name”) is a value

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

@app.route("/login", methods=["POST", "GET"])

def login():

 # if form is submited

 if request.method == "POST":

 # record the user name

 session["name"] = request.form.get("name")

 # redirect to the main page

 return redirect("/")

 return render_template("login.html")  
  
---  
  
 __

 __

  * After storing the user name we need to check whenever user lands on the index page that any session with that user name exists or not.
  * If the user name doesn’t exist then redirect to the login page.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

@app.route("/")

def index():

 # check if the users exist or not

 if not session.get("name"):

 # if not there in the session then redirect to the login page

 return redirect("/login")

 return render_template('index.html')  
  
---  
  
 __

 __

  * After successfully remember the **user we also need a way to logout the users.**
  * So whenever the user **clicks logout** change the user **value to none** and redirect them to the **index page.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

@app.route("/logout")

def logout():

 session["name"] = None

 return redirect("/")  
  
---  
  
 __

 __

### Complete Project –

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask, render_template, redirect, request, session

# The Session instance is not used for direct access, you should always use
flask.session

from flask_session import Session

 

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "filesystem"

Session(app)

 

 

@app.route("/")

def index():

 if not session.get("name"):

 return redirect("/login")

 return render_template('index.html')

 

 

@app.route("/login", methods=["POST", "GET"])

def login():

 if request.method == "POST":

 session["name"] = request.form.get("name")

 return redirect("/")

 return render_template("login.html")

 

 

@app.route("/logout")

def logout():

 session["name"] = None

 return redirect("/")

 

 

if __name__ == "__main__":

 app.run(debug=True)  
  
---  
  
 __

 __

#### index.html

  * We can also use **session.name** to excess the value from the **session**.

## HTML

 __

 __  
 __

 __

 __  
 __  
 __

{% extends "layout.html" %}

 

{% block y %}

 

 {% if session.name %}

 You are Register {{ session.name }} <a
href="/logout">logout</a>.

 {% else %}

 You are not Register. <a href="/login">login</a>.

 {% endif %}

 

{% endblock %}  
  
---  
  
 __

 __

#### login.html

## HTML

 __

 __  
 __

 __

 __  
 __  
 __

{% extends "layout.html" %}

 

{% block y %}

 

 <h1> REGISTER </h1>

 

 <form action="/login" method="POST">

 <input placeholder="Name" autocomplete="off"
type="text" name="name">

 <input type="submit" name="Register">

 </form>

 

{% endblock %}  
  
---  
  
 __

 __

#### layout.html

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

 <meta name="viewport" content="initial-scale=1,
width=device-width">

 <title> flask </title>

 </head>

 <body>

 {% block y %}{% endblock %}

 </body>

</html>  
  
---  
  
 __

 __

### Output –

#### login.html

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101195901/login.PNG)

#### index.html

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101195911/index.PNG)

### You can also see your generated session

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101201039/cookies.PNG)![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101201112/session4.PNG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

