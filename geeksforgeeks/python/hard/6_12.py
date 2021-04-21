Django Sign Up and login with confirmation Email | Python



Django by default provides an _authentication system configuration_. **User**
objects are the core of the authentication system.today we will implement
Django’s authentication system.  

**Modules required :**

  * django : django install
  * crispy_forms :

    
    
    pip install --upgrade django-crispy-forms

 **Basic setup :**  
Start a project by the following command –

    
    
     django-admin startproject project

Change directory to project –

    
    
     cd project

Start the server- Start the server by typing the following command in terminal
–

  

  

    
    
     python manage.py runserver

To check whether the server is running or not go to a web browser and enter
_http://127.0.0.1:8000/_ as URL.  
Now stop the server by pressing

    
    
    ctrl-c

 **Let’s create an app now called the “user”.**

    
    
    python manage.py startapp user

Goto user/ folder by doing: _cd user_ and create a folder _templates_ with
files _index.html, login.html, Email.html, register.html_ files.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190729100403/Screenshot-from-2019-07-29-10-03-46.png)

Open the project folder using a text editor. The directory structure should
look like this :  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190729094634/Screenshot-from-2019-07-29-09-46-07.png)

Now add the “user” app and “crispy_form” in your todo_site in settings.py, and
add

    
    
    CRISPY_TEMPLATE_PACK = 'bootstrap4'

at last of settings.py  

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190729095107/Screenshot-from-2019-07-29-09-50-27.png)

configure _email settings_ in setting.py:  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190729101406/Screenshot-from-2019-07-29-10-13-38.png)

_place your email and password here._  

**Edit** _ **urls.py**_ **file in project :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

from django.urls import path, include

from user import views as user_view

from django.contrib.auth import views as auth

urlpatterns = [

 path('admin/', admin.site.urls),

 ##### user related path##########################

 path('', include('user.urls')),

 path('login/', user_view.Login, name ='login'),

 path('logout/', auth.LogoutView.as_view(template_name
='user/index.html'), name ='logout'),

 path('register/', user_view.register, name ='register'),

]  
  
---  
  
 __

 __

 **Edit urls.py in user :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.urls import path, include

from django.conf import settings

from . import views

from django.conf.urls.static import static

urlpatterns = [

 path('', views.index, name ='index'),

]  
  
---  
  
 __

 __

 **Edit** _ **views.py**_ **in user :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm

from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives

from django.template.loader import get_template

from django.template import Context

 

 

#################### index#######################################

def index(request):

 return render(request, 'user/index.html',
{'title':'index'})

 

########### register here #####################################

def register(request):

 if request.method == 'POST':

 form = UserRegisterForm(request.POST)

 if form.is_valid():

 form.save()

 username = form.cleaned_data.get('username')

 email = form.cleaned_data.get('email')

 ######################### mail system
####################################

 htmly = get_template('user/Email.html')

 d = { 'username': username }

 subject, from_email, to = 'welcome', 'your_email@gmail.com',
email

 html_content = htmly.render(d)

 msg = EmailMultiAlternatives(subject, html_content, from_email, [to])

 msg.attach_alternative(html_content, "text/html")

 msg.send()

 ##################################################################

 messages.success(request, f'Your account has been created ! You are now
able to log in')

 return redirect('login')

 else:

 form = UserRegisterForm()

 return render(request, 'user/register.html', {'form': form,
'title':'reqister here'})

 

################ login
forms###################################################

def Login(request):

 if request.method == 'POST':

 

 # AuthenticationForm_can_also_be_used__

 

 username = request.POST['username']

 password = request.POST['password']

 user = authenticate(request, username = username, password =
password)

 if user is not None:

 form = login(request, user)

 messages.success(request, f' wecome {username} !!')

 return redirect('index')

 else:

 messages.info(request, f'account done not exit plz sign in')

 form = AuthenticationForm()

 return render(request, 'user/login.html', {'form':form,
'title':'log in'})  
  
---  
  
 __

 __

Configure your email here.  

**Now create a forms.py in user :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

 email = forms.EmailField()

 phone_no = forms.CharField(max_length = 20)

 first_name = forms.CharField(max_length = 20)

 last_name = forms.CharField(max_length = 20)

 class Meta:

 model = User

 fields = ['username', 'email', 'phone_no',
'password1', 'password2']  
  
---  
  
 __

 __

 **Navigate to** _ **templates/user/**_ **and edit files :**

  * link to index.html file
  * link to Email.html
  * link to login.html
  * link to register.html

 **Make migrations and migrate them.**

    
    
    python manage.py makemigrations
    python manage.py migrate

 **Now you can run the server to see your app.**

    
    
    python manage.py runserver

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190729100851/upload26.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

