Python | Django Admin Interface



 **Prerequisites :** django-introduction-and-installation | django-
introduction-set-2-creating-a-project

 **Django** provides a default admin interface which can be used to perform
create, read, update and delete operations on the model directly. It reads set
of data that explain and gives information about data from the model, to
provide an instant interface where the user can adjust contents of the
application . This is an in-built module and design to execute admin related
work to the user.

 **Activating and Using the Admin Interface**  
The admin app(django.contrib.admin) is enabled by default and already added
into the INSTALLED_APPS list present in the settings.py file.

![installed_packs](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-534-1.png)

To access this admin interface on browser write ‘/admin/’ at
‘localhost:8000/admin/’ and it shows the output as given below:

  

  

![login ](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-531-1.png)

It prompts for login details, if no login id is created before, then a new
superuser can be created by using the command given below:

    
    
    python manage.py createsuperuser
    

![https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-529.png](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-529.png)

Now, access the admin login page after starting the Development Server which
can be done by using the command given below.

    
    
    python manage.py runserver
    

![runserver](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-535.png)

Enter username and password, then hit login .

![login](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-533.png)

After logging in successfully, it shows the interface as shown below: .

![Django Admin Interface](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-532.png)

This is what is called a Django Admin Dashboard where one can add, delete and
update data belonging to any registered model.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

