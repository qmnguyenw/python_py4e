Python Django | Google authentication and Fetching mails from scratch



Google Authentication and Fetching mails from scratch mean without using any
module which has already set up this authentication process. We’ll be using
Google API python client and oauth2client which is provided by Google.
Sometimes, it really hard to implement this Google authentication with these
libraries as there was no proper documentation available. But after completing
this read, things will be clear completely.

Now Let’s create Django 2.0 project and then implement Google authentication
services and then extract mails. We are doing extract mail just to show how
one can ask for permission after authenticating it.

![](https://media.geeksforgeeks.org/wp-content/uploads/django-google.png)

 **Step #1:** Creating Django Project

The first step is to create virtual environment and then install the
dependencies. So We’ll be using venv:

  

  

    
    
    mkdir google-login && cd google-login
    
    python3.5 -m venv myvenv
    source myvenv/bin/activate
    

This command will create one folder myvenv through which we just activated
virtual environment. Now type

    
    
    pip freeze

Then you must see no dependencies installed in it. Now first thing first let’s
install Django:

    
    
    pip install Django==2.0.7

That is Django version which we used but feel free to use any other version.
Now next step is to create one project, let’s name it gfglogin:

    
    
    django-admin startproject gfglogin .

Since we are inside google-login directory that’s why we want django project
to be on that present directory only so for that you need to use ‘ . ‘ at the
end for present directory indication. Then create one app to separate logic
from main project, so create one app called gfgauth:

    
    
    django-admin startapp gfgauth

So overall terminal will look like:  
![](https://media.geeksforgeeks.org/wp-content/uploads/django_project1.png)

Since we created one app. Add that app name into settings.py in
INSTALLED_APP list. Now we have Django project up running, so let’s migrate
it first and then check if there is any error or not.

    
    
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

So after migrating, one should be able to run the server and see the starting
page of Django on that particular url.  
![](https://media.geeksforgeeks.org/wp-content/uploads/django_project2.png)  
  
**Step #2:** Installing dependencies

Since we have the project up running successfully, let’s install basic
requirements. First, we need googleapiclient, this is needed because we have
to create one resource object which helps to interact with the API. So to be
precise we will make use of build method from it.

  

  

To install:

    
    
    pip install google-api-python-client==1.6.4

Now the second module is oauth2client, this will make sure of all the
authentication, credential, flows and many more complex thing so it is
important to use this.

    
    
    pip install oauth2client==4.1.2

And at last, install jsonpickle, (just in case if it is not installed)
because it will be used by oauth2client while making CredentalsField.

    
    
    pip install jsonpickle==0.9.6

So these are the only dependencies which we need. Now let’s step into the
coding part and see how it works.  
  
**Step #3:** Creating models

Use models to store the credentials which we get from an API, so there are
only 2 main field which needed to take care of. First is id , which will be
ForeignKey and second is credential which will be equal to CredentialsField.
This field needs to be imported from oauth2client. So our models.py will
look like:

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.contrib.auth.models import User

from django.db import models

from oauth2client.contrib.django_util.models import CredentialsField

 

 

class CredentialsModel(models.Model):

 id = models.ForeignKey(User, primary_key = True, on_delete =
models.CASCADE)

 credential = CredentialsField()

 task = models.CharField(max_length = 80, null = True)

 updated_time = models.CharField(max_length = 80, null =
True)

 

 

class CredentialsAdmin(admin.ModelAdmin):

 pass,  
  
---  
  
 __

 __

Currentlytask and updated_time are simply extra fields added, hence can be
removed. So this credential will hold the credential data in the database.

 **Important guideline:**

When we import CredentialsField, then automatically __init__ method gets
executed at back and if you’ll notice the code in path  
/google-login/myvenv/lib/python3.5/site-
packages/oauth2client/contrib/django_util/__init__.py Line 233

They are importing urlresolvers so that they can make use of the reverse
method from it. Now the problem is that this urlresolvers has been removed
after Django 1.10 or Django 1.11, If you are working on Django 2.0 then it
will give an error that urlresolvers cannot be found or not there.

Now to overcome this problem we need to change 2 lines, first replace that
import from django.core import urlresolvers to from django.urls import
reverse

And then replace Line 411 urlresolvers.reverse(...) to reverse(...)

Now you should be able to run it successfully.

After creating these models:

    
    
    python manage.py makemigrations
    python manage.py migrate
    

  
**Step #4:** Creating Views

Right now we have only 3 main views to handle requests. First is to show the
home page, status, Google button so that we can send requests for
Authentication. Second view will get triggered when the google button is
clicked, means an AJAX request. Third will be to handle the return request
from google so that we can accept the access_token from it and save it in our
database.

First, let’s do the Google authentication thing:

So right now we need to specify the flow to the API that what permissions we
need to ask, what is my secret key and redirect url. So to do that enter:

    
    
    FLOW = flow_from_clientsecrets(
        settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
        scope='https://www.googleapis.com/auth/gmail.readonly',
        redirect_uri='http://127.0.0.1:8000/oauth2callback',
        prompt='consent')
    

As you can notice settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON, so go to
settings.py file and type:

    
    
    GOOGLE_OAUTH2_CLIENT_SECRETS_JSON = 'client_secrets.json'

This tells Django that where json file is present. We will later download
this file. After specifying the flow, let’s start logic.

Whenever we need to see if someone is authorized or not we first check our
database whether that user credentials is already present or not. If not then
we make requests to API url and then get credentials.

 __

 __  
 __

 __

 __  
 __  
 __

def gmail_authenticate(request):

 storage = DjangoORMStorage(CredentialsModel, 'id', request.user,
'credential')

 credential = storage.get()

 

 if credential is None or credential.invalid:

 FLOW.params['state'] =
xsrfutil.generate_token(settings.SECRET_KEY,

 request.user)

 authorize_url = FLOW.step1_get_authorize_url()

 return HttpResponseRedirect(authorize_url)

 else:

 http = httplib2.Http()

 http = credential.authorize(http)

 service = build('gmail', 'v1', http = http)

 print('access_token = ', credential.access_token)

 status = True

 

 return render(request, 'index.html', {'status': status})  
  
---  
  
 __

 __

We use DjangoORMStorage (which is provided byoauth2client) so that we can
store and retrieve credentials from Django datastore. So we need to pass 4
parameters for it. First is the model class which has CredientialsField inside
it. Second is the unique id that has credentials means key name, third is the
key value which has the credentials and last is the name of that
CredentialsField which we specified in models.py.

Then we get the value from storage and see if it is valid or not. If it is not
valid then we create one user token and get one to authorize url, where we
redirect the user to the Google login page. After redirecting user will fill
up the form and once user is authorized by google then google will send data
to _callback url_ with access_token which we will do later. Now in case, if
user credentials was already present then it will re-verify the credentials
and give you back the access_token or sometimes the refreshed access_token in
case if the previous one was expired.

Now we need to handle the callback url, to do that:

 __

 __  
 __

 __

 __  
 __  
 __

def auth_return(request):

 get_state = bytes(request.GET.get('state'), 'utf8')

 if not xsrfutil.validate_token(settings.SECRET_KEY, get_state,

 request.user):

 return HttpResponseBadRequest()

 

 credential = FLOW.step2_exchange(request.GET.get('code'))

 storage = DjangoORMStorage(CredentialsModel, 'id', request.user,
'credential')

 storage.put(credential)

 

 print("access_token: % s" % credential.access_token)

 return HttpResponseRedirect("/")  
  
---  
  
 __

 __

Now inside callback url when we get one response from google then we capture
the data and get state from it, state is nothing but the token which we
generated by generateToken. So what we do is that we validate the token with
secret_key, the token which we generated and with the user who generated it.
These things get verified byxsrfutil.validate_token method which make sure
that the token is not too old with the time and it was generated at given
particular time only. If these things doesn’t work out well then it will give
you error else you will go to the next step and share the code from callback
response with google so that you can get the access_token.

So this was 2 step verification and after successfully getting the credential
we save it in Django datastore by using DjangoORMStorage because through that
only we can fetch and store credential into CredentialsField. Once we will
store it we can redirect the user to any particular page and that’s how you
can get access_token.

Now let’s create one home page which will tell whether the user is logged in
or not.

 __

 __  
 __

 __

 __  
 __  
 __

def home(request):

 status = True

 

 if not request.user.is_authenticated:

 return HttpResponseRedirect('admin')

 

 storage = DjangoORMStorage(CredentialsModel, 'id', request.user,
'credential')

 credential = storage.get()

 

 try:

 access_token = credential.access_token

 resp, cont =
Http().request("https://www.googleapis.com/auth/gmail.readonly",

 headers ={'Host': 'www.googleapis.com',

 'Authorization': access_token})

 except:

 status = False

 print('Not Found')

 

 return render(request, 'index.html', {'status': status})  
  
---  
  
 __

 __

Right now we are assuming that the user is authenticated in Django, means that
user is no more anonymous and has info saved in database. Now to have support
for the anonymous user, we can remove the checks for credentials in database
or create one temporary user.

Coming back to home view, first we will check whether the user is
authenticated or not, means that user is not anonymous, if yes then make him
do log in else check for credentials first. If user has already logged in from
Google then it will show Status as True else it will show False.

Now coming to templates let’s create one. First go to root folder and create
one folder named as ‘templates’, then inside that create index.html:

 __

 __  
 __

 __

 __  
 __  
 __

{% load static %}

<!DOCTYPE html>

<html lang="en">

 

<head>

 <meta charset="UTF-8">

 <script src="{% static 'js/main.js' %}"></script>

 <title>Google Login</title>

</head>

<body>

 

<div>

 <div>

 {% if not status %}

 <a href="/gmailAuthenticate" onclick="gmailAuthenticate()"
title="Google">Google</a>

 {% else %}

 <p>Your are verified</p>

 {% endif %}

 </div>

 

</div>

</body>

</html>  
  
---  
  
 __

 __

Now this page is very much simplified so no css or styling is there, just one
simple link to check. Now you will notice _js file_ also. so again go to root
folder and create one directory as static/js/

And inside _js_ create one javascript file main.js:

 __

 __  
 __

 __

 __  
 __  
 __

function gmailAuthenticate(){

 $.ajax({

 type: "GET",

 url: "ajax/gmailAuthenticate",

 // data: '',

 success: function (data) {

 console.log('Done')

 }

 });

};  
  
---  
  
 __

 __

This _js file_ was used to separate the logic from HTML file and also to make
one AJAX call to Django. Now we have all the parts done for views.  
  
**Step #5:** Creating urls and basic settings

In the main project urls means gfglogin/urls.py edit and put:

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path, include

 

urlpatterns = [

 path('admin/', admin.site.urls),

 path('', include('gfgauth.urls')),

]  
  
---  
  
 __

 __

Because we need to test gfgauth app working. Now insidegfgauth/urls.py type:

 __

 __  
 __

 __

 __  
 __  
 __

from django.conf.urls import url

from . import views

 

urlpatterns = [

 url(r'^gmailAuthenticate', views.gmail_authenticate, name
='gmail_authenticate'),

 url(r'^oauth2callback', views.auth_return),

 url(r'^$', views.home, name ='home'),

]  
  
---  
  
 __

 __

As you can see, gmailAuthenticate is for AJAX calls, oauth2callback is for
callback url and the last one is home page url. Now before running there are
few settings which we haven’t talked about:

In settings.py you need to edit:

  1. In TEMPLATES list add ‘templates’ inside DIRS list.
  2. At last of settings.py file add:
    
    
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    
    GOOGLE_OAUTH2_CLIENT_SECRETS_JSON = 'client_secrets.json'
    

So we just specified where templates and static files are present and most
importantly where is google oauth2 client secret json file. Now we will
download this file.  
  
**Step #6:** Generating Oauth2 Client secret file

Head over to Google Developer Console page and create one project and name it
anything you like. After creating it, head over to the project dashboard and
click on the Navigation menu which is on the top left. Then click on API
services and then credentials page. Click on create credentials (you might
need to set product name before going ahead so do that first). Now select web
application since we are using Django. After this specifies the name and then
simply go to redirect URIs and over there type:

    
    
    http://127.0.0.1:8000/oauth2callback
    

And then save it. You need not specify the Authorized Javascript origins so
leave it blank for now. After saving it, you will be able to see all your
credentials, just download the credentials, it will get saved in some random
names so simply reformat the filename and type ‘client_secrets’ and make sure
it is of json format. Then save it and paste it on Django project root folder
(where manage.py is there).  
  
**Step #7:** Running it

Now recheck if everything is correct or not. Make sure you have migrated it.
Also before going ahead create one superuser so that you are no more
anonymous:

    
    
    python3.5 manage.py createsuperuser

Type all the necessary details and then do:

    
    
    python3.5 manage.py runserver

And go to http://127.0.0.1:8000

You will see this:  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-07-06-14-58-16.png)

Which is perfectly fine, now type your superuser credentials over here and
then you will be able to see the admin dashboard. Just avoid that and again go
to http://127.0.0.1:8000

Now you should be able to see the Google link, now click on it and you will
see:

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-07-06-15-02-06.png)

Now as you can see it is saying Sign in to continue to GFG, here GFG is my
Project name. So it is working fine. Now enter your credentials and after
submitting you will see:

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-07-06-15-04-28.png)

Since we are requesting for mails permission that’s why it is asking the user
to allow it. In case if it is showing error then in Google console you might
need to activate Gmail API into your project. Now once you will allow it you
will get the credentials and get saved inside your database. In case if the
user clicks on Cancel then you will need to write a few more codes to handle
such flow.

Now in case if you allowed it then you will be able to see the access_token on
your console/database. After getting access_token you can make use of this to
fetch user email and all other stuff.

See full code in this repository **here**.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

