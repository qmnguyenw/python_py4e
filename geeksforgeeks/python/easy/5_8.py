Retrieving HTML From data using Flask



Flask is a lightweight WSGI web application framework. It is designed to make
getting started quick and easy, with the ability to scale up to complex
applications. It began as a simple wrapper around Werkzeug and Jinja and has
become one of the most popular Python web application frameworks.

Read this article to know more about Flask  
 **Create form as HTML**

We will create a simple HTML Form, very simple Login form

 __

 __  
 __

 __

 __  
 __  
 __

<form action="{{ url_for("gfg")}}" method="post">

<label for="firstname">First Name:</label>

<input type="text" id="firstname" name="fname"
placeholder="firstname">

<label for="lastname">Last Name:</label>

<input type="text" id="lastname" name="lname"
placeholder="lastname">

<button type="submit">Login</button>  
  
---  
  
 __

 __

Its an simple HTML form using the post method the only thing is unique is
action URL. URL_for is an Flask way of creating dynamic URLs where the first
arguments refers to the function of that specific route in flask. In our form
it will create a Dynamic route which has gfg function in the flask app

 **Create Flask application**

  

  

Start your virtual environment

    
    
    pip install virtualenv
    python3 -m venv env
    pip install flask
    

Now we will create the flask backend which will get user input from HTML form

 __

 __  
 __

 __

 __  
 __  
 __

# importing Flask and other modules

from flask import Flask, request, render_template 

 

# Flask constructor

app = Flask(__name__) 

 

# A decorator used to tell the application

# which URL is associated function

@app.route('/', methods =["GET", "POST"])

def gfg():

 if request.method == "POST":

 # getting input with name = fname in HTML form

 first_name = request.form.get("fname")

 # getting input with name = lname in HTML form 

 last_name = request.form.get("lname") 

 return "Your name is "+first_name + last_name

 return render_template("form.html")

 

if __name__=='__main__':

 app.run()  
  
---  
  
 __

 __

 **Working –**

Almost everything is simple, We have created a simple Flask app, if we look
into code

  * importing flask and creating a home route which has both _get and post methods_
  * defining a function with name **gfg**
  * if requesting method is post, which is the method we specified in the form we get the input data from HTML form
  * you can get HTML input from Form using name attribute and request.form.get() function by passing the name of that input as argument
    * request.form.get("fname") will get input from Input value which has name attribute as fname and stores in first_name variable
    * request.form.get("lname") will get input from Input value which has name attribute as lname and stores in last_name variable
  * The return value of POST method is by replacing the variables with their valuesYour name is "+first_name+last_name
  * the default return value for the function gfg id returning home.html template
  * you can review what-does-the-if-__name__-__main__-dofrom the article

 **Output –**  
 **Code in action**  
![code](https://media.geeksforgeeks.org/wp-
content/uploads/20200613095249/Screenshot-from-2020-06-13-09-50-46.png)  
 **flask server running**  
![flask server running](https://media.geeksforgeeks.org/wp-
content/uploads/20200613095300/Screenshot-from-2020-06-13-09-50-55.png)  
 **html form**  
![html form](https://media.geeksforgeeks.org/wp-
content/uploads/20200613095304/Screenshot-from-2020-06-13-09-51-02.png)  
 **returning data from html template**  
![retutning data](https://media.geeksforgeeks.org/wp-
content/uploads/20200613095307/Screenshot-from-2020-06-13-09-51-06.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

