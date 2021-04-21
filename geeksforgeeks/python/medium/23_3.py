Handling 404 Error in Flask



Prerequisite: Creating simple application in Flask

A 404 Error is showed whenever a page is not found. Maybe the owner changed
its URL and forgot to change the link or maybe they deleted the page itself.
Every site needs a Custom Error page to avoid the user to see the default Ugly
Error page.

GeeksforGeeks also has a customized error page. If we type a URL like  
www.geeksforgeeks.org/ajneawnewiaiowjf

 **Default 404 Error**  
![](https://media.geeksforgeeks.org/wp-content/uploads/Capture-68.jpg)

 **GeeksForGeeks Customized Error Page**  
![](https://media.geeksforgeeks.org/wp-content/uploads/404.jpg)

  

  

It will show an Error 404 page since this URL doesn’t exist. But an error page
provides a beautiful layout, helps the user to go back, or even takes them to
the homepage after a specific time interval. That is why Custom Error pages
are necessary for every website.

Flask provides us with a way to handle the error and return our Custom Error
page.

For this, we need to download and import flask. Download the flask through the
following commands on CMD.

    
    
    pip install flask
    

Using app.py as our Python file to manage templates, 404.html be the file we
will return in the case of a 404 error and header.html be the file with header
and navbar of a website.

 **app.py**  
Flask allows us to make a python file to define all routes and functions. In
app.py we have defined the route to the main page (‘/’) and error handler
function which is a flask function and we passed 404 error as a parameter.

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask, render_template

 

app = Flask(__name__)

 

# app name

@app.errorhandler(404)

 

# inbuilt function which takes error as parameter

def not_found(e):

 

# defining function

 return render_template("404.html")  
  
---  
  
 __

 __

The above python program will return 404.html file whenever the user opens a
broken link.

 **404.html**  
The following code exports header and navbar from header.html.  
Both files should be stored in templates folder according to the flask.

 __

 __  
 __

 __

 __  
 __  
 __

{% extends "header.html" %}

<!-- Exports header and navbar from header.html

 or any file you want-->

{% block title %}Page Not Found{% endblock %}

{% block body %}

 

 <h1>Oops! Looks like the page doesn't exist anymore</h1>

 <a href="{{ url_for('index') }}"><p>Click Here</a>To go
to the Home Page</p>

 

<!-- {{ url_for('index') }} is a var which returns url of index.html-->

{% endblock %}  
  
---  
  
 __

 __

### Automatically Redirecting to the Home page after 5 seconds

The app.py code for this example stays the same as above.  
The following code Shows the Custom 404 Error page and starts a countdown of 5
seconds.  
After 5 seconds are completed, it redirects the user back to the homepage.  
 **404.html**  
The following code exports header and navbar from header.html.  
Both files should be stored in the templates folder according to the flask.  
After 5 seconds, the user will get redirected to the Home Page Automatically.

 __

 __  
 __

 __

 __  
 __  
 __

<html>

<head>

<title>Page Not Found</title>

<script language="JavaScript" type="text/javascript">

 

var seconds =6;

// countdown timer. took 6 because page takes approx 1 sec to load

 

var url="{{url_for(index)}}";

// variable for index.html url

 

function redirect(){

 if (seconds <=0){

 

 // redirect to new url after counter down.

 window.location = url;

 } else {

 seconds--;

 document.getElementById("pageInfo").innerHTML="Redirecting to Home Page
after "

+seconds+" seconds."

 setTimeout("redirect()", 1000)

 }

}

</script>

</head>

 

{% extends "header.html" %}

//exporting navbar and header from header.html

{% block body %}

 

 <body onload="redirect()">

<p id="pageInfo"></p>

{% endblock %}

 

 

</html>  
  
---  
  
 __

 __

 **Sample header.html**  
This is a sample header.html which includes a navbar just like shown in the
image.  
It’s made up of bootstrap. You can also make one of your own.  
For this one, refer the bootstrap documentation.

 __

 __  
 __

 __

 __  
 __  
 __

<!DOCTYPE html>

<html>

<head>

 

<!-- LINKING ALL SCRIPTS/CSS REQUIRED FOR NAVBAR -->

 

 <link rel="stylesheet"
href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/

css/bootstrap.min.css"

 integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E26 

3XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

 

 <title>Flask</title>

</head>

<body>

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
integrity=

"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"

crossorigin="anonymous"></script>

 

<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd

/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K

/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
crossorigin="anonymous"></script>

 

<script
src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"


integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"

 crossorigin="anonymous"></script>

 

<header>

 <!-- Starting header -->

 

 <nav class="navbar navbar-expand-lg navbar-light bg-light">

 <a class="navbar-brand" href="#">Navbar</a>

 <!-- bootstrap classes for navbar -->

 <button class="navbar-toggler" type="button" data-
toggle="collapse" data-target=

"#navbarSupportedContent" aria-controls="navbarSupportedContent"

 aria-expanded="false" aria-label="Toggle navigation">

 <span class="navbar-toggler-icon"></span>

 </button>

 

 <div class="collapse navbar-collapse"
id="navbarSupportedContent">

 <ul class="navbar-nav mr-auto">

 <li class="nav-item active">

 <a class="nav-link" href="#">Home <span class="sr-
only">(current)</span></a>

 </li>

 <li class="nav-item">

 <a class="nav-link" href="#">Link</a>

 </li>

 <li class="nav-item dropdown">

 <a class="nav-link dropdown-toggle" href="#"
id="navbarDropdown"

 role="button data-toggle="dropdown" aria-haspopup="true"
aria-expanded="false">

 Dropdown

 </a>

 <div class="dropdown-menu" aria-
labelledby="navbarDropdown">

 <a class="dropdown-item" href="#">Action</a>

 <a class="dropdown-item" href="#">Another action</a>

 <div class="dropdown-divider"></div>

 <a class="dropdown-item" href="#">Something else
here</a>

 </div>

 </li>

 <li class="nav-item">

 <a class="nav-link disabled" href="#">Disabled</a>

 </li>

 </ul>

 <form class="form-inline my-2 my-lg-0">

 <input class="form-control mr-sm-2" type="search"

 placeholder="Search" aria-label="Search">

 <button class="btn btn-outline-success my-2 my-sm-0"

 type="submit">Search</button>

 </form>

 </div>

</nav>

</head>

 

 <body >

 

 {%block body%}

 

 {%endblock%}

 

</body>

</html>  
  
---  
  
 __

 __

 **Output:**  
The output will be a custom error page with header.html that the user
exported.  
The following is an example output with my custom header, footer, and 404.html
file.

![](https://media.geeksforgeeks.org/wp-content/uploads/404e.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

