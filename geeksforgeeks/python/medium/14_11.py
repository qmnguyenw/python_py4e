Django Project MVT Structure



Django is based on **MVT (Model-View-Template)** architecture. MVT is a
software design pattern for developing a web application.

 **MVT Structure has the following three parts –**

 **Model:** Model is going to act as the interface of your data. It is
responsible for maintaining data. It is the logical data structure behind the
entire application and is represented by a database (generally relational
databases such as MySql, Postgres). To check more, visit – Django Models

 **View:** The View is the user interface — what you see in your browser when
you render a website. It is represented by HTML/CSS/Javascript and Jinja
files. To check more, visit – Django Views.

 **Template:** A template consists of static parts of the desired HTML output
as well as some special syntax describing how dynamic content will be
inserted. To check more, visit – Django Templates

  

  

### Project Structure :

A Django Project when initialised contains basic files by default such as
manage.py, view.py, etc. A simple project structure is enough to create a
single page application. Here are the major files and there explanations.
Inside the geeks_site folder ( project folder ) there will be following files-

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-77.png)  
 **manage.py-** This file is used to interact with your project via the
command line(start the server, sync the database… etc). For getting the full
list of command that can be executed by manage.py type this code in the
command window-

    
    
    $ python manage.py help

  
**folder ( geeks_site ) –** This folder contains all the packages of your
project. Initially it contains four files –  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-78.png)

  *  **_init_.py –** It is python package.
  *  **settings.py –** As the name indicates it contains all the website settings. In this file we register any applications we create, the location of our static files, database configuration details, etc.
  *  **urls.py –** In this file we store all links of the project and functions to call.
  *  **wsgi.py –** This file is used in deploying the project in WSGI. It is used to help your Django application communicate with the web server.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

