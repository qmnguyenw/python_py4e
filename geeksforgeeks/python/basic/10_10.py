verbose_name – Django Built-in Field Validation



Built-in Field Validations in Django models are the validations that come
predefined to all Django fields. Every field comes in with built-in
validations from Django validators. One can also add more built-in field
validations for applying or removing certain constraints on a particular
field. verbose_name is a human-readable name for the field. If the verbose
name isn’t given, Django will automatically create it using the field’s
attribute name, converting underscores to spaces. This attribute in general
changes the field name in admin interface.

 **Syntax –**

    
    
    field_name = models.Field(verbose_name = "name")

## Django Built-in Field Validation verbose_name Explanation

Illustration of **verbose_name** using an Example. Consider a project named
geeksforgeeks having an app named geeks.

> Refer to the following articles to check how to create a project and an app
> in Django.
>
>   * How to Create a Basic Project using MVT in Django?
>   * How to Create an App in Django ?
>

Enter the following code into models.py file of **geeks** app. We will be
using CharField for experimenting for all field options.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.db.models import Model

# Create your models here.

 

class GeeksModel(Model):

 geeks_field = models.CharField(

 max_length = 200, 

 )  
  
---  
  
 __

 __

After runningmakemigrations and migrate on Django and rendering the above
model, let us check the display name for geeks_field.

![django-verbose_name-](https://media.geeksforgeeks.org/wp-
content/uploads/20191104161659/django-verbose_name-.png)  
Now let us modify this using verbose_name attribute. change models.py to

 __

 __  
 __

 __

 __  
 __  
 __

from django.db import models

from django.db.models import Model

# Create your models here.

 

class GeeksModel(Model):

 geeks_field = models.CharField(

 max_length = 200, 

 verbose_name = "Geeksforgeeks"

 )  
  
---  
  
 __

 __

Since models.py is modified run makemigrations and migrate again on the
project. Open admin interface and check the name of that field again, it is
changes to “Geeksforgeeks”.  
![](https://media.geeksforgeeks.org/wp-content/uploads/20191104161658/django-
verbose-name.png)  
You can see the modified image. Therefore, verbose_name modifies the field
name.

#### More Built-in Field Validations

Field Options| Description| Null| If **True** , Django will store empty values
as **NULL** in the database. Default is **False**.| Blank| If **True** , the
field is allowed to be blank. Default is **False**.| db_column| The name of
the database column to use for this field. If this isn’t given, Django will
use the field’s name.| Default| The default value for the field. This can be a
value or a callable object. If callable it will be called every time a new
object is created.| help_text| Extra “help” text to be displayed with the form
widget. It’s useful for documentation even if your field isn’t used on a
form.| primary_key| If True, this field is the primary key for the model.|
editable| If **False** , the field will not be displayed in the admin or any
other ModelForm. They are also skipped during model validation. Default is
**True**.| error_messages| The error_messages argument lets you override the
default messages that the field will raise. Pass in a dictionary with keys
matching the error messages you want to override.| help_text| Extra “help”
text to be displayed with the form widget. It’s useful for documentation even
if your field isn’t used on a form.| verbose_name| A human-readable name for
the field. If the verbose name isn’t given, Django will automatically create
it using the field’s attribute name, converting underscores to spaces.|
validators| A list of validators to run for this field. See the validators
documentation for more information.| Unique| If True, this field must be
unique throughout the table.  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

