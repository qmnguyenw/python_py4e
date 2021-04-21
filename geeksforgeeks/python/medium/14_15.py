Todo list app using Flask | Python



There are many frameworks that allow building your webpage using Python, like
Django, flask, etc. Flask is a web application framework written in Python.
Flask is based on WSGI(Web Server Gateway Interface) toolkit and Jinja2
template engine. Its modules and libraries that help the developer to write
applications without writing the low-level codes such as protocols, thread
management, etc.

In this article, we will learn how to make a todo list app using the Flask
framework. In this app, you can add your todo items and mark them as complete
or incomplete.

 **Installation:**

    
    
     pip install Flask

 **Basic setup :**  
 **Step 1:** First make basic folders

    
    
    mkdir app && cd app && mkdir static && mkdir templates

 **Step 2:** Make some basic python files to write the code and name it as you
desire.

  

  

 **Step 3:** Run the below command to start the server

    
    
    touch run.py the app

 **Step 4:** Change directory to _app_ –

    
    
     cd app

 **Step 5:** create models.py for database, routes.py for urls/views and
__init__ file to package our app

    
    
     touch models.py routes.py __init__.py 

**Step 6:** Goto _templates/_ directory and create index.html file

    
    
     cd templates && touch index.html 

**Step 7:** Goto _static/_ directory and create main.css

    
    
     cd static && touch main.css

Now, open the project folder using a text editor. The directory structure
should look like this :

![](https://media.geeksforgeeks.org/wp-
content/uploads/20191007031144/Screenshot-from-2019-10-07-03-11-19.png)

 **run.py file**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from app import app

 

if __name__ == '__main__':

 app.run(debug=True)  
  
---  
  
 __

 __

 **app/__init__.py file**

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

import os

 

file_path = os.path.abspath(os.getcwd())+"/todo.db"

 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

db = SQLAlchemy(app)

 

 

from app import routes  
  
---  
  
 __

 __

 **app/routes.py file**

 __

 __  
 __

 __

 __  
 __  
 __

from flask import render_template, request, redirect, url_for

from app import app

from app.models import Todo

from app import db

 

 

@app.route('/')

def index():

 incomplete = Todo.query.filter_by(complete=False).all()

 complete = Todo.query.filter_by(complete=True).all()

 

 return render_template('index.html', incomplete=incomplete,
complete=complete)

 

 

@app.route('/add', methods=['POST'])

def add():

 todo = Todo(text=request.form['todoitem'],
complete=False)

 db.session.add(todo)

 db.session.commit()

 

 return redirect(url_for('index'))

 

 

@app.route('/complete/<id>')

def complete(id):

 

 todo = Todo.query.filter_by(id=int(id)).first()

 todo.complete = True

 db.session.commit()

 

 return redirect(url_for('index'))  
  
---  
  
 __

 __

 **app/models.py file**

 __

 __  
 __

 __

 __  
 __  
 __

from app import db

 

class Todo(db.Model):

 id = db.Column(db.Integer, primary_key=True)

 text = db.Column(db.String(200))

 complete = db.Column(db.Boolean)

 

 def __repr__(self):

 return self.text  
  
---  
  
 __

 __

 **app/main.html**

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

 <meta charset="UTF-8"> 

 <title>Todo App</title> 

 <link rel="stylesheet" type="text/css"
href="{{url_for('static', filename='main.css')}}"> 

 

</head> 

<body> 

 <h1>Todo List</h1> 

 <div>Add a new todo item: 

 <form action="{{ url_for('add') }}" method="POST"> 

 <input type="text" name="todoitem"> 

 <input type="submit" value="Add Item"
class="button"> 

 </form> 

 </div> 

 <div> 

 <h2>Incomplete Items</h2> 

 <ul> 

 {% for todo in incomplete %} 

 <li style="font-size: 30pt" class='mark'>{{ todo.text }}
<a href="{{ url_for('complete', id=todo.id) }}">Mark As
Complete</a></li> 

 {% endfor %} 

 </ul> 

 <h2>Completed Items</h2> 

 <ul> 

 {% for todo in complete %} 

 <li style="font-size: 30pt">{{ todo.text }}</li> 

 {% endfor %} 

 </ul> 

 </div> 

</body> 

</html>   
  
---  
  
__

__

**app/main.css**

 __

 __  
 __

 __

 __  
 __  
 __

body{

 background:black; 

 color:red; 

 margin-top: 5px; 

} 

.button{ 

 color:green; 

} 

.mark{font-size: 10px;}   
  
---  
  
__

__

**Run the todo app using the below command**

    
    
    python run.py

![](https://media.geeksforgeeks.org/wp-
content/uploads/20191007032528/screen-1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

