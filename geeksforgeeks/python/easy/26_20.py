Flask – (Creating first simple application)



 **Building an webpage using python.**

There are many modules or frameworks which allows to build your webpage using
python like bottle, django, flask etc. But the real popular ones are Flask and
Django. Django is easy to use as compared to Flask but FLask provides you the
versatility to program with.

To understand what Flask is you have to understand few general terms.

  1.  **WSGI** Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications.
  2.  **Werkzeug** It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.
  3.  **jinja2** jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.

 **Flask:**

Flask is a web application framework written in Python. Flask is based on the
Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.

  

  

 **Installation:**  
We will require two package to setup your environment. _virtualenv_ for a user
to create multiple Python environments side-by-side. Thereby, it can avoid
compatibility issues between the different versions of the libraries and the
next will be _Flask_ itself.

  1.  **virtualenv**
    
        pip install virtualenv

  2.  **Flask**
    
        pip install Flask

After completing the installation of the package, let’s get our hands on the
code.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing flask module in the project is mandatory

# An object of Flask class is our WSGI application.

from flask import Flask

 

# Flask constructor takes the name of 

# current module (__name__) as argument.

app = Flask(__name__)

 

# The route() function of the Flask class is a decorator, 

# which tells the application which URL should call 

# the associated function.

@app.route('/')

# ‘/’ URL is bound with hello_world() function.

def hello_world():

 return 'Hello World'

 

# main driver function

if __name__ == '__main__':

 

 # run() method of Flask class runs the application 

 # on the local development server.

 app.run()  
  
---  
  
 __

 __

Save it in a file and then run the script we will be getting a output like
this.

![](https://media.geeksforgeeks.org/wp-content/uploads/1-21.jpg)

Then go to the url given there you will seeing your first webpage displaying
hello world there on your local server.

Digging further into the context, the **route()** decorator in Flask is used
to bind URL to a function. Now to extend this functionality our small web app
is also equipped with another method **add_url_rule()** which is a function of
an application object is also available to bind a URL with a function as in
the above example, route() is used.

Example:

    
    
    def gfg():
       return ‘geeksforgeeks’
    app.add_url_rule(‘/’, ‘g2g’, gfg)
    

Output:

  

  

    
    
    geeksforgeeks

You can also add variables in your webapp, well you might be thinking how
it’ll help you, it’ll help you to build an url dynamically. So lets figure it
out with an example.

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask

app = Flask(__name__)

 

@app.route('/hello/<name>')

def hello_name(name):

 return 'Hello %s!' % name

 

if __name__ == '__main__':

 app.run()  
  
---  
  
 __

 __

and go to the url _http://127.0.0.1:5000/hello/geeksforgeeks_ it’ll give you
the following output.

![](https://media.geeksforgeeks.org/wp-content/uploads/2-18.jpg)

We can also use HTTP methods in Flask lets see how to do that

HTTP protocol is the foundation of data communication in world wide web.
Different methods of data retrieval from specified URL are defined in this
protocol. The methods are described down below.

>  **GET :** Sends data in simple or unencrypted form to the server.
>
>  **HEAD :** Sends data in simple or unencrypted form to the server without
> body.  
>  **  
> HEAD :** Sends form data to the server. Data is not cached.
>
>  **PUT :** Replaces target resource with the updated content.
>
>  **DELETE :** Deletes target resource provided as URL.

By default, the Flask route responds to the GET requests. However, this
preference can be altered by providing methods argument to route() decorator.

In order to demonstrate the use of POST method in URL routing, first let us
create an HTML form and use the POST method to send form data to a URL.

Now let’s create a html login page.

Below is source code of the file

 __

 __  
 __

 __

 __  
 __  
 __

<html>

 <body> 

 <form action = "http://localhost:5000/login" method =
"post">

 <p>Enter Name:</p>

 <p><input type = "text" name = "nm" /></p>

 <p><input type = "submit" value = "submit" /></p>

 </form> 

 </body>

</html>  
  
---  
  
 __

 __

Now save this file html as try this python script to create the server.

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

 

@app.route('/success/<name>')

def success(name):

 return 'welcome %s' % name

 

@app.route('/login',methods = ['POST', 'GET'])

def login():

 if request.method == 'POST':

 user = request.form['nm']

 return redirect(url_for('success',name = user))

 else:

 user = request.args.get('nm')

 return redirect(url_for('success',name = user))

 

if __name__ == '__main__':

 app.run(debug = True)  
  
---  
  
 __

 __

After the development server starts running, open login.html in the browser,
enter name in the text field and click _submit_ button. The output would be
the following.

![](https://media.geeksforgeeks.org/wp-content/uploads/4-7.jpg)

Result will be something like this

![](https://media.geeksforgeeks.org/wp-content/uploads/5-8.jpg)

And there’s much more to Flask than this. If you are interested in this web
framework of Python you can dig into the links provided down below for further
information.

 **Reference Links:**  
1) http://flask.pocoo.org/  
2) http://flask.pocoo.org/docs/0.12/  
3) TutorialsPoint – Flask

This article is contributed by **Subhajit Saha**. If you like GeeksforGeeks
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

