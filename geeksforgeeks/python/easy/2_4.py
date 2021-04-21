Creating first web application using Bottle Framework – Python



There are many frameworks in python which allow you to create a webpage like
bottle, flask, django. In this article, you will learn how to create a simple
app using bottle web framework. Bottle is a fast, simple and lightweight WSGI
micro web-framework for Python. It is distributed as a single file module and
has no dependencies other than the Python Standard Library.

  *  **Routing:** Requests to function-call mapping with support for clean and dynamic URLs.
  *  **Templates:** Fast and pythonic built-in template engine and support for mako, jinja2 and cheetah templates.
  *  **Utilities:** Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.
  *  **Server:** Built-in HTTP development server and support for paste, fapws3, bjoern, gae, cherrypy or any other WSGI capable HTTP server.

In order to create the app using bottle, we have to install it first

    
    
    pip install bottle

 **Example 1:**

Create a file called app.py

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from bottle import route, run

 

@route('/')

def index():

 return f'<b>Hello GFG</b>!'

 

run(host='localhost', port=8000,debug=True)  
  
---  
  
 __

 __

