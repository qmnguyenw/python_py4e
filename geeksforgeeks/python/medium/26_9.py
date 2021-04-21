CGI Programming in Python



 **What is CGI?**  
Common Gateway Interface (also known as CGI) is not a kind of language but
just a **specification(set of rules)** that helps to establish a dynamic
interaction between a web application and the browser (or the client
application). The CGI programs make possible **communication between client
and web servers**. Whenever the client browser sends a request to the
webserver the CGI programs send the output back to the web server based on the
input provided by the client-server.

  1. CGI is the standard for programs to interface with HTTP servers.
  2. CGI programming is written dynamically generating webpages that respond to user input or webpages that interact with software on the server

 **Working of CGI**  
When a request is made by the client-server to the webserver, the CGI uses
**external script files** to handle such requests. These files could be
written in any language. The main objective of these script files is to
retrieve the data from the database quickly and more efficiently. These
scripts convert the retrieved data into an Html format that sends the data to
these web servers in Html formatted page.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200118162044/CGI4.jpg)

 **Install apache2 on your system can we will run ‘hello.py’ on host
‘127.0.0.1’**  
It is recommended to have basic knowledge of HTML before trying this example.  
 **hello.py**

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr/bin/python3

# Importing the 'cgi' module

import cgi

 

 

print("Content-type: text/html\r\n\r\n")

print("<html><body>")

print("<h1> Hello Program! </h1>")

# Using the inbuilt methods

 

form = cgi.FieldStorage()

if form.getvalue("name"):

 name = form.getvalue("name")

 print("<h1>Hello" +name+"! Thanks for using my script!</h1><br
/>")

if form.getvalue("happy"):

 print("<p> Yayy! I'm happy too! </p>")

if form.getvalue("sad"):

 print("<p> Oh no! Why are you sad? </p>")

 

# Using HTML input and forms method

print("<form method='post' action='hello2.py'>")

print("<p>Name: <input type='text' name='name' /></p>")

print("<input type='checkbox' name='happy' /> Happy")

print("<input type='checkbox' name='sad' /> Sad")

print("<input type='submit' value='Submit' />")

print("</form")

print("</body></html>")  
  
---  
  
 __

 __

 **Some advantages of CGI are discussed as below:**  
1 They are portable and can work on almost any web server and operating
system.  
2 They are language-independent.  
3 They are quite scalable programs in nature which means they can perform both
simple and complex tasks.  
4 CGIs enhance dynamic communication in web applications.  
5They also aid in making businesses more profitable by decreasing development
and maintenance costs.

 **Some disadvantages of CGI are as below:**  
1 The interpreter has to evaluate a CGI script every time the program is
initiated this creates a lot of traffic as there are too many requests from
the side of the client-server.  
2 Programming and designing of CGI programs is very complex and ambiguous.  
3 CGI programs may compromise server security as most of them are free and
easily available making them quite vulnerable.

  

  

This article is contributed by **Harsh Wardhan Chaudhary (Intern)**. If you
like GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

