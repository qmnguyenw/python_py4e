How to Create a Basic Project using MVT in Django ?



 **Prerequisite –** Django Project MVT Structure

Assuming you have gone through the previous article. This article focusses on
creating a basic project to render a template using MVT architecture. We will
use MVT (Models, Views, Templates) to render data to a local server.

 **Create a basic Project:**

  * To initiate a project of Django on Your PC, open Terminal and Enter the following command
    
        django-admin startproject projectName

  * A New Folder with name projectName will be created. To enter in the project using terminal enter command
    
        cd projectName

  * Create a new file **views.py** inside the project folder where settings.py, urls.py and other files are stored and save the following code in it-

 __

 __  
 __

 __

 __  
 __  
 __

# HttpResponse is used to

# pass the information 

# back to view

from django.http import HttpResponse

 

# Defining a function which

# will receive request and

# perform task depending 

# upon function definition

def hello_geek (request) :

 

 # This will return Hello Geeks

 # string as HttpResponse

 return HttpResponse("Hello Geeks")  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-72.png)

  * Open **urls.py** inside project folder (projectName) and add your entry-
    * Import **hello_geek** function from views.py file.
        
                from projectName.views import hello_geeks

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-73.png)

    * Add an entry in url field inside url patterns-
        
                path('geek/', hello_geek), 

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-74.png)

  * Now to run the server follow these steps-
    * Open command prompt and change directory to env_site by this command-
        
                $ cd env_site

    * Go to Script directory inside env_site and activate virtual environment-
        
                $ cd Script
        
                $ activate

    * Return to the env_site directory and goto the project directory-
        
                $ cd ..
        
                $ cd geeks_site

    *  **Start the server-** Start the server by typing following command in cmd-
        
                $ python manage.py runserver

 **Note-** Take the help of previous django article if any issue arises in
starting the server.

  *  **Checking –** Open the browser and type this url-
    
        http://127.0.0.1:8000/geek/

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-75.png)

Bingo…!! You are done with creating and rendering a basic Project.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

