HyperlinkedModelSerializer in serializers – Django REST Framework



HyperlinkedModelSerializer is a layer of abstraction over the default
serializer that allows to quickly create a serializer for a model in Django.
Django REST Framework is a wrapper over default Django Framework, basically
used to create APIs of various kinds. There are three stages before creating a
API through REST framework, Converting a Model’s data to JSON/XML format
(Serialization), Rendering this data to the view, Creating a URL for mapping
to the viewset. This article revolves around HyperlinkedModelSerializer in
serializers of Django REST Framework.

#### HyperlinkedModelSerializer

The HyperlinkedModelSerializer class is similar to the ModelSerializer class
except that it uses hyperlinks to represent relationships, rather than primary
keys. By default the serializer will include a url field instead of a primary
key field. The url field will be represented using a HyperlinkedIdentityField
serializer field, and any relationships on the model will be represented using
a HyperlinkedRelatedField serializer field.

 **Syntax –**

 __

 __  
 __

 __

 __  
 __  
 __

class SerializerName(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = ModelName

 fields = List of Fields  
  
---  
  
 __

 __

 **Example –**

 __

 __  
 __

 __

 __  
 __  
 __

class AccountSerializer(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = Account

 fields = ['id', 'account_name', 'users', 'created']  
  
---  
  
 __

 __

By default, all the model fields on the class will be mapped to a
corresponding serializer fields.

  

  

### How to create a HyperlinkedModelSerializer using Django REST Framework ?

>   * Add rest_framework to INSTALLED_APPS
>   * Create a app and model
>   * Serialization
>   * Creating a viewset
>   * Define URLs of API
>   * Run server and check API
>

#### Add rest_framework to INSTALLED_APPS

To initialize REST Framework in your project, go to settings.py, and in
INSTALLED_APPS add **‘rest_framework’** at the bottom.

 __

 __  
 __

 __

 __  
 __  
 __

# Application definition

 

INSTALLED_APPS = [

 'django.contrib.admin',

 'django.contrib.auth',

 'django.contrib.contenttypes',

 'django.contrib.sessions',

 'django.contrib.messages',

 'django.contrib.staticfiles',

 'rest_framework',

]  
  
---  
  
 __

 __

#### Create a app and model

Now, let’s create a app using command,

    
    
    python manage.py startapp apis

A folder with name apis would have been registered by now. let’s add this app
to **INSTALLED_APPS** and urls.py also.  
In, settings.py,

 __

 __  
 __

 __

 __  
 __  
 __

# Application definition

 

INSTALLED_APPS = [

 'django.contrib.admin',

 'django.contrib.auth',

 'django.contrib.contenttypes',

 'django.contrib.sessions',

 'django.contrib.messages',

 'django.contrib.staticfiles',

 'rest_framework',

 'apis',

]  
  
---  
  
 __

 __

Now, add apis urls in urls.py. In **geeksforgeeks.urls.py** ,

 __

 __  
 __

 __

 __  
 __  
 __

from django.contrib import admin

# include necessary libraries

from django.urls import path, include

 

urlpatterns = [

 path('admin/', admin.site.urls),

 # add apis urls

 path('', include("apis.urls"))

]  
  
---  
  
 __

 __

 **Create a model**  
To demonstrate, creating and using an API, let’s create a model named
“GeeksModel”. In apis/models.py

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

 

class GeeksModel(models.Model):

 title = models.CharField(max_length = 200)

 description = models.TextField()

 

 def __str__(self):

 return self.title  
  
---  
  
 __

 __

now our app is ready, let’s serialize the data and create views from the same.

#### Serialization

Serializers allow complex data such as querysets and model instances to be
converted to native Python datatypes that can then be easily rendered into
JSON, XML or other content types. Serializers also provide deserialization,
allowing parsed data to be converted back into complex types, after first
validating the incoming data. Let’s start creating a serializer, in file
apis/serializers.py,

 __

 __  
 __

 __

 __  
 __  
 __

# import serializer from rest_framework

from rest_framework import serializers

 

# import model from models.py

from .models import GeeksModel

 

# Create a model serializer 

class GeeksSerializer(serializers.HyperlinkedModelSerializer):

 # specify model and fields

 class Meta:

 model = GeeksModel

 fields = ('url', 'id', 'title', 'description')  
  
---  
  
 __

 __

#### Creating a viewset

To render data into frontend, and handle requests from user, we need to create
a view. In Django REST Framework, we call these as viewsets, so let’s create a
view in apis/views.py,

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import viewsets

from rest_framework import viewsets

 

# import local data

from .serializers import GeeksSerializer

from .models import GeeksModel

 

# create a viewset

class GeeksViewSet(viewsets.ModelViewSet):

 # define queryset

 queryset = GeeksModel.objects.all()

 

 # specify serializer to be used

 serializer_class = GeeksSerializer  
  
---  
  
 __

 __

#### Define URLs of API

Specify the url path of APIs to be accessed, In apis/urls.py,

 __

 __  
 __

 __

 __  
 __  
 __

# basic URL Configurations

from django.urls import include, path

# import routers

from rest_framework import routers

 

# import everything from views

from .views import *

 

# define the router

router = routers.DefaultRouter()

 

# define the router path and viewset to be used

router.register(r'geeks', GeeksViewSet)

 

# specify URL Path for rest_framework

urlpatterns = [

 path('', include(router.urls)),

 path('api-auth/', include('rest_framework.urls'))

]  
  
---  
  
 __

 __

After everything is successfully ready, let’s run some commands to activate
the server.

#### Run server and check API

Run following commands to create the database, and run server,

    
    
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    

Now visit http://127.0.0.1:8000/geeks/,

![hyperlinkedmodelserializer-Django-REST-
Framework](https://media.geeksforgeeks.org/wp-
content/uploads/20200325061436/hyperlinkedmodelserializer-Django-REST-
Framework.png)

One can check that HyperlinkedModelSerializer has created a endpoint with
overall CRUD functionality.

To check the code for the project, click here

### Advanced Usage

 **Specifying which fields to include**  
If you only want a subset of the default fields to be used in a model
serializer, you can do so using fields or exclude options, just as you would
with a ModelForm.  
For example:

 __

 __  
 __

 __

 __  
 __  
 __

class AccountSerializer(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = Account

 # specify field names

 fields = ['id', 'account_name', 'users', 'created']  
  
---  
  
 __

 __

or exclude Example :

 __

 __  
 __

 __

 __  
 __  
 __

class AccountSerializer(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = Account

 # specify field names

 exclude = ['id']  
  
---  
  
 __

 __

 **Specifying read only fields**  
One may wish to specify multiple fields as read-only. Instead of adding each
field explicitly with the read_only=True attribute, you can use the shortcut
Meta option, read_only_fields.  
This option should be a list or tuple of field names, and is declared as
follows:

 __

 __  
 __

 __

 __  
 __  
 __

class AccountSerializer(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = Account

 fields = ['id', 'account_name', 'users', 'created']

 # specify read only fields

 read_only_fields = ['account_name']  
  
---  
  
 __

 __

 **Changing the URL field name**  
The name of the URL field defaults to ‘url’. You can override this globally,
by using the URL_FIELD_NAME setting.

 __

 __  
 __

 __

 __  
 __  
 __

class AccountSerializer(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = Account

 fields = ['id', 'newurl', 'account_name', 'users',
'created']

 # specify read only fields

 read_only_fields = ['account_name']

 URL_FIELD_NAME = 'newurl'  
  
---  
  
 __

 __

To check more about HyperlinkedModelSerializer,
visitHyperlinkedModelSerializer Documentation

## Core arguments in serializer fields

Argument| Description| read_only| Set this to True to ensure that the field is
used when serializing a representation, but is not used when creating or
updating an instance during deserialization| write_only| Set this to True to
ensure that the field may be used when updating or creating an instance, but
is not included when serializing the representation.| required| Setting this
to False also allows the object attribute or dictionary key to be omitted from
output when serializing the instance.| default| If set, this gives the default
value that will be used for the field if no input value is supplied.|
allow_null| Normally an error will be raised if None is passed to a serializer
field. Set this keyword argument to True if None should be considered a valid
value.| source| The name of the attribute that will be used to populate the
field.| validators| A list of validator functions which should be applied to
the incoming field input, and which either raise a validation error or simply
return.| error_messages| A dictionary of error codes to error messages.|
label| A short text string that may be used as the name of the field in HTML
form fields or other descriptive elements.| help_text| A text string that may
be used as a description of the field in HTML form fields or other descriptive
elements.| initial| A value that should be used for pre-populating the value
of HTML form fields.  
---|---  
  
Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

