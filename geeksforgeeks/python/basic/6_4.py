Best practices for Professional Developer – Django Framework



Django is an open-source, Python-based framework for building web
applications. To make our Django code more readable and efficient we should
follow a certain set of rules/practices. These should not be seen as the right
way or the only way to work with Django, but instead best practices to work
with Django framework

##  _Coding style_

In general, code should be clean, concise, readable, Testable and DRY __
(Don’t repeat yourself).Try to follow PEP8 guidelines as closely as
reasonable.

##  _Using virtual environment_

Avoid using global environment for project dependencies, since it can produce
dependency conflicts. Python can’t use multiple package versions at the same
time. This can be a problem if different projects require different
incompatible versions of the same package. Always isolate your project
requirements and dependencies in a virtual environment. Most common way to do
it is by using virtualenv.

##  _Requirements.txt File_

Requirements are the list of Python packages (dependencies) your project is
using while it runs, including the version for each package. It is important
to update your requirements.txt file for collaborating properly with other
developers. This file, when included in your code repository, enables you to
update all the packages installed in your virtual environment by executing a
single line in the terminal.

In order to generate a new requirements.txt file or update the existing one
use this command. Make sure that you are in a correct directory.

  

  

    
    
    (virtualenv) $ pip freeze > requirements.txt
    

It is a good practice to update the requirements.txt file before pushing code
to the repository and install requirements.txt file after pulling code from
the repository.

##  _Avoid writing fat views_

You should write fat models, skinny views, which means try to write most of
your logic in model itself.

For example: Suppose we are implementing a functionality of sending an email
to user, it is better to extend the model with an email function instead of
writing this logic in your controller/view. This makes your code easier to
unit test because you can test the email logic in one place, rather than
repeatedly in every controller/view where this takes place.

##  _Correct model naming_

Generally models represent a single object or entity so model names should be
a singular noun.

 __

 __  
 __

 __

 __  
 __  
 __

# Bad practice

class Users(models.Model):

 pass

 

# Good practice

class User(models.Model): # use 'User' instead of 'Users'

 pass  
  
---  
  
 __

 __

##  _Using the correct related-name in model relationships_

Related name specifies the reverse relation from the parent model back to the
child model. It is reasonable to indicate related-name in plural as it returns
a queryset

 __

 __  
 __

 __

 __  
 __  
 __

# parent model

class Owner(models.Model):

 pass

 

# child model

class Item(models.Model):

 # use "items" instead of "item"

 owner = models.ForeignKey(Owner, related_name ='items')  
  
---  
  
 __

 __

##  _Django templates_

 **Location** : **** Templates can be placed at two places, either in the app
directory itself or at the root of project. It is recommended to put templates
in the root directory but if you want to make your app reusable (use it at
multiple places) than you should place it in app directory.

    
    
    #Good practice
    root_folder/
        my_app1/
        my_app2/
        my_app3/
        templates/
    
    #If you want to make your app reusable
    root_folder/
        my_app1/
            templates/
        my_app2/
            templates/
        my_app3/
            templates/
    

**Naming** :Correctly naming your templates helps any new developer
immediately picking up your django code. Good template name looks like this

    
    
    [application]/[model]_[function].html
    

For example, creating a template to list all of the contacts (Contact model)
in my address book (address_book application), I would use the following
template:

    
    
    address_book/contact_list.html
    

Similarly, a detail view of contact would use

    
    
    address_book/contact_detail.html
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

