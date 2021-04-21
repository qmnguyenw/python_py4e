How to perform multiplication using CherryPy in Python?



CherryPy also known as a web application library is a Python web framework
that provides a friendly interface to the HTTP protocol for Python developers.
It allows developers to build web applications the same way as in traditional
object-oriented Python programs. Thereby, resulting in smaller source code
developed in no time.

This framework is mainly for the developers who want to create a portable
database-driven web application using Python, as it provides Create, Retrieve,
Update, and Delete functionalities.

The basic requirements for the installation of CherryPy include:

  * Python with version 2.4 or above
  * Cherrypy 3.0

To install cherrypy run the following command in terminal:

    
    
    pip install cherrypy

 **Approach:**

  

  

  * Create a user interface to take input from the user.
  * Write cherrypy program to perform required operations

HTML code to create a user interface to take input from the user:

## HTML

 __

 __  
 __

 __

 __  
 __  
 __

<html>

 

<body> 

 

 <div class="container"> 

 <h2><u><i>Operation</i></u></h2> 

 <form action="store" id="form" method="GET"> 

 <input type="number" name="number1" /><br /> 

 <input type="number" name="number2" /><br /> 

 

 

 <input style="margin-left: 250px;" id=" submit"
type="submit"/></div> 

 </div> 

 </form> 

 </div> 

 

</body> 

</html>  
  
---  
  
 __

 __

 **Cherrypy code for multiplication**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cherrypy

 

 

class Root(object):

 

 @cherrypy.expose

 def index(self):

 return """<html> 

<head> 

 

</head> 

<body> 

 

<div class="container"> 

 <h2><u><i>Multiplication</i></u></h2> 

 <form action="store" id="form" method="GET"> 

 <input type="number" name="num1" /><br /> 

 <input type="number" name="num2" /><br /> 

 

 

 <input style="margin-left: 250px;" id=" submit" type="submit"/></div> 

</div>

 </form> 

</div> 

 

</body> 

</html>"""

 

 @cherrypy.expose

 def store(self, num1, num2):

 

 mul1 = int(num1)

 mul2 = int(num2)

 

 result = mul1*mul2

 

 out = """<html> 

 <body> 

 

 

 

<p> Sum: %s</p>

 

 

 

 

 <a style="color:red; font-size:35px;" id="shutdown";
href="./shutdown"><i>Shutdown Server</i></a> 

 </body> 

 </html> 

 

 """

 

 return out % (result)

 

 @cherrypy.expose

 def shutdown(self):

 cherrypy.engine.exit()

 

 

if __name__ == "__main__":

 cherrypy.config.update({'server.socket_port': 8087})

 

 cherrypy.quickstart(Root())  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201009151605/eform-200x90.JPG)![](https://media.geeksforgeeks.org/wp-
content/uploads/20201009151724/afterm-200x71.JPG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

