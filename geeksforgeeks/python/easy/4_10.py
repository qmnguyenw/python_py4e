Template Inheritance in Flask



Template inheritance is a very good feature of Jinja templating . Jinja is a
web template engine for the Python programming language . We have seen that
webpages of a website contains same footer , navigation bar etc. So instead of
making same footer and navigation bar in all webpages separately , we make use
of template inheritance , which allows us to create the part which is same in
all webpages (eg. footer,navigation bar) only once and we also don’t need to
write the html , head , title tag again and again . Lets define the common
structure of web pages in base.html file. First of all we will render template
using flask from main.py file .

 ** _Prerequisite_** – Flask – (Creating first simple application)

**Step 1 –** Create a flask app to render the main template

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask, render_template

 

# Setting up the application

app = Flask(__name__)

 

# making route

 

 

@app.route('/')

def home():

 return render_template('home.html')

 

 

# running application

if __name__ == '__main__':

 app.run(debug=True)  
  
---  
  
 __

 __

