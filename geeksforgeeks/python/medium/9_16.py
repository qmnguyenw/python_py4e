Post/Redirect/Get (PRG) Design Pattern



Prerequisite- HTTP Protocol, GET and POST requests using Python

 **Introduction:**

 _PRG_ is one of many design patterns used in web development. It is used to
prevent the resubmission of a form caused by reloading the same web page after
submitting the form. It removes redundancy of content to strengthen the SEO
and makes the website user friendly.  
It is used by large, trusted online shops and other robust websites which are
intended to be user friendly.

 **Problem:**

When we try to submit a web form then a HTTP POST request is sent to the
server. The server process the request and send response to the client with
response code 2XX. When the client try to refresh/reload the web page, he/she
unintentionally sends another HTTP POST request to the server with the same
data as just before. This may cause undesired results, such as duplicate web
purchases.

  

  

 _The browser pops up a warning message box after reload as shown below:_

![](https://media.geeksforgeeks.org/wp-content/uploads/20200417200037/Post-
Redirect-Get-pattern.png)

 **Internal working:**

Below is the block diagram of internal working of the above problem.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200403143342/problem1.png)

 **Solution:**

To avoid this problem many web developer use the _POST/REDIRECT/GET_ pattern,
instead of returning a web page directly, the _POST_ returns a redirect to
another web page or same depending on the requirements.

 **Internal working:**

  

  

Below is the block diagram of internal working of the above solution.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200403160213/sol5.png)  
  
 **A minimal python and HTML code using flask framework to demonstrate above
concept.**

  * Create a file called _app.py_ in the project root directory and write the below code in it. And install flask using-
    
    
    $pip install flask
    

__

__  
__

__

__  
__  
__

from flask import Flask, render_template, redirect, request, url_for

 

# Initiate flask app

app = Flask(__name__)

 

# Declare routes and methods

@app.route('/', methods =['GET', 'POST'])

def home():

 # If it is POST request the redirect

 if request.method =='POST':

 return redirect(url_for('home'))

 

 return render_template('home.html', title ='Home')

 

if __name__=='__main__':

 app.run()  
  
---  
  
 __

 __

  * Create a folder _templates_ in the project root directory and create a file _home.html_ inside the templates directory and write the below code in it.

 __

 __  
 __

 __

 __  
 __  
 __

<!-- Create a form -->

<form action="" method="post">

 <!-- Create a input box -->

 <input type="text", value="Suraj
Yadav"><br><br>

 <!-- Create a submit button -->

 <input type="submit" value="Submit">

</form>  
  
---  
  
 __

 __

  *  **To run the web server type in console:**
    
    
    $python app.py
    **Output:**
    Running on http://127.0.0.1:5000/
    

  * Go to web browser and type _localhost:5000_ and hit enter.

 **Console output:**  
In the below image, the first GET request is made when we use localhost:5000,
then we POST data to the server. Now, after processing the data server
redirects us by making a GET request so the third GET request is made by the
server and finally the fourth GET request is made when we try to refresh the
page.  
  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200417204943/Post-
Redirect-Get-pattern-Final-Output.png)

 **Note: Try to play with code without redirecting.**

![design-pattern-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102105/GFG-OODL-Article-2.png)

My Personal Notes _arrow_drop_up_

Save

