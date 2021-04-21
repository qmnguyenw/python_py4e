Python | Extending and customizing django-allauth



Prerequisite: Django-allauth setup and Configuration  
Let’s deal with customizing django-allauth signup forms, intervening in
registration flow to add custom processes and validations.

**Extending Signup Form or adding custom fields in django-allauth:**  
One of the most common queries about allauth is about adding additional fields
or custom fields to the signup form. You can extend the SignupForm class from
allauth.account.forms. All you need to do is create a custom class pass the
SignupForm to the custom class and define the custom fields and save it. It’s
_vital_ to return the user object as it will be passed to other modules for
validations. You also need to include a variable in settings.py.  
Let’s see this using an example forms.py  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from allauth.account.forms import SignupForm

from django import forms

class CustomSignupForm(SignupForm):

 first_name = forms.CharField(max_length=30, label='First
Name')

 last_name = forms.CharField(max_length=30, label='Last
Name')

 def signup(self, request, user):

 user.first_name = self.cleaned_data['first_name']

 user.last_name = self.cleaned_data['last_name']

 user.save()

 return user  
  
---  
  
 __

 __

In the above snippet CustomSignupForm is extended the class which inherits all
the features of SignupForm class and adds the necessary features. Here custom
fields by the name first_nameand last_name are created and saved in using the
signup module in the same class.  

The ACCOUNT_FORMS in settings.py for the above code is

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

ACCOUNT_FORMS= {

'signup': 'YourProject.forms.CustomSignupForm',

}  
  
---  
  
 __

 __

Any other custom forms created can be extended in ACCOUNT_FORMS. The list is
illustrated in thedocumentation.  
Similarly, _LoginForm UserForm AddEmailForm_ and others can be extended.
However, remember that when you extend these forms and link them in
settings.py. Don’t forget to pass the original form (For example _SignupForm_
) as a parameter to your class and sometimes you might have to handle custom
validations and return users or some other value. Please refer to the source
code to follow the correct flow.  
  
**User Intervention and Custom validations:**  
Let’s discuss adding custom validations and intervening in the user
registration flow. _DefaultAccountAdapter_ is very useful and indeed can be
used to solve most of the customization problems that a user might encounter
while using _django_ – _allauth_.  

**Example #1: Restricted List of email’s**  
After figuring out a way to store and fetch the restricted list, you can use
the adapters and raise validation errors in the registration form when a
restricted email tries to register. Extend a _DefaultAccountAdapter_ and
override the _clean_email_ method. Create an adapter.py in your project
directory and extend the default adapter class.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from allauth.account.adapter import DefaultAccountAdapter

from django.forms import ValidationError

class RestrictEmailAdapter(DefaultAccountAdapter):

 def clean_email(self, email):

 RestrictedList = ['Your restricted list goes here.']

 if email in RestrictedList

 raise ValidationError('You are restricted from registering.\

 Please contact admin.')

 return email  
  
---  
  
 __

 __

Finally, point the account adapter in settings.py to your extended class.

    
    
    ACCOUNT_ADAPTER='YourProject.adapter.RestrictEmailAdapter'

 **Example #2: Add a Maximum length to a username**

As ACCOUNT_USERNAME_MAX_LENGTH doesn’t exist in the allauth library,
_DefaultAccountAdaptercan_ is used to achieve this feature without much pain.
Extend the _DefaultAccountAdapterclass_ and overriding the _clean_username_
method. You need to also reference the _clean_username_ once again after our
custom validation to complete other inbuilt validations.

The last sentence in the above paragraph is the key to work with
_DefaultAccountAdapter_. You should never forget to reference the original
module name for the module to complete other validations.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from allauth.account.adapter import DefaultAccountAdapter

from django.forms import ValidationError

class UsernameMaxAdapter(DefaultAccountAdapter):

 def clean_username(self, username):

 if len(username) > 'Your Max Size':

 raise ValidationError('Please enter a username value\

 less than the current one')

 

 # For other default validations.

 return DefaultAccountAdapter.clean_username(self, username)  
  
---  
  
 __

 __

Finally, point to the subclass in your settings.py  

    
    
    ACCOUNT_ADAPTER = 'YourProject.adapter.UsernameMaxAdapter'
    

You can refer to the _adapters.py_file in the source code and extend other
modules and add a process or change their flow. The modules such as
_populate_username_ , _clean_password_ (which can be customized to restrict
commonly used passwords) can have the custom process and flow without
rewriting them.  
 _DefaultAccountAdapter_ can be a potent tool if used in the right
circumstances to intervene in allauth’s default process. allauth comes with a
vast variety of inbuilt settings, and they are here. You can also download the
entire source code from the link in the references below.  
 **References:**  
django-allauth documentation  
stack overflow thread on Example 1  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

