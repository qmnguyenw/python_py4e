Integrating TinyMCE with Django



TinyMCE is a online rich text editor which is fully flexible and provides
customisation. mostly used to get dynamic data such as articles in GFG and
much more, their is no static database for posts

 **Installation –**

To integrate it with Django web app or website you need to first install its
pip library

    
    
    pip install django-tinymce
    

**Integrate with Django Project –**

add tinyMCE as individual app in setting.py

  

  

    
    
    INSTALLED_APPS = [
         ...
        'tinymce',
         ... 
    ]
    

Also add default configuration for tinyMCE editor in settings.py

    
    
    TINYMCE_DEFAULT_CONFIG = {
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 20,
        'selector': 'textarea',
        'theme': 'silver',
        'plugins': '''
                textcolor save link image media preview codesample contextmenu
                table code lists fullscreen  insertdatetime  nonbreaking
                contextmenu directionality searchreplace wordcount visualblocks
                visualchars code fullscreen autolink lists  charmap print  hr
                anchor pagebreak
                ''',
        'toolbar1': '''
                fullscreen preview bold italic underline | fontselect,
                fontsizeselect  | forecolor backcolor | alignleft alignright |
                aligncenter alignjustify | indent outdent | bullist numlist table |
                | link image media | codesample |
                ''',
        'toolbar2': '''
                visualblocks visualchars |
                charmap hr pagebreak nonbreaking anchor |  code |
                ''',
        'contextmenu': 'formats | link image',
        'menubar': True,
        'statusbar': True,
    }
    
    
    

here in configuration dictionary you can customise editor by changing values
like theme and many more.

setting TinyMCE is done now to bring it into actions we need forms.py file
with some required values like needed size of input field it is used by
displaying content on html page

 __

 __  
 __

 __

 __  
 __  
 __

from django import forms

from tinymce import TinyMCE

from .models import _your_model_

 

 

class TinyMCEWidget(TinyMCE):

 def use_required_attribute(self, *args):

 return False

 

 

class PostForm(forms.ModelForm):

 content = forms.CharField(

 widget=TinyMCEWidget(

 attrs={'required': False, 'cols': 30, 'rows':
10}

 )

 )

 class Meta:

 model = _your_model_

 fields = '__all__'  
  
---  
  
 __

 __

Last step is to add htmlfield to your model you can also use different field
check out them on their official website

__

__  
__

__

__  
__  
__

...

from tinymce.models import HTMLField 

 

 

class article(models.Model):

 ...

 content = HTMLField()  
  
---  
  
 __

 __

And its all set just make migrations for see changes in admin page by running
following commands

    
    
    python manage.py makemigrations
    
    
    
    python manage.py migrate

Now check it in admin area by running server

    
    
    python manage.py runserver
    

**Output –**

here how it will look like it may have different appearance

![html field](https://media.geeksforgeeks.org/wp-
content/uploads/20200711202334/Screenshotfrom20200711201950.png)

Editor in admin area

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

