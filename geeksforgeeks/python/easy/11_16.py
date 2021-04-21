Django model data types and fields list



The most important part of a model and the only required part of a model is
the list of database fields it defines. Fields are specified by class
attributes. Be careful not to choose field names that conflict with the models
API like clean, save, or delete.

**Example:**

    
    
    from django.db import models
    
    class Musician(models.Model):
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        instrument = models.CharField(max_length=200)
    
    class Album(models.Model):
        artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        num_stars = models.IntegerField()

Setting a field for storing any type of data is like deciding a data type in
C/C++ for storing a particular integer, char etc. Fields in Django are the
data types to store a particular type of data. For example, to store an
integer, IntegerField would be used. These fields have in-built validation for
a particular data type, that is you can not store “abc” in an IntegerField.
Similarly, for other fields. This post revolves about major fields one can use
in Django Models.  
Here are some key attributes one should be aware of before starting to use
Django Fields.

### Field types

Each field in the model should be an instance of the appropriate Field class.
Django uses field class types to determine a few things:

  

  

  * The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).
  * The default HTML widget to use when rendering a form field (e.g. <input type=”text”>, <select>).
  * The minimal validation requirements, used in Django’s admin and in automatically-generated forms.

Django ships with dozens of built-in field types which can be used to save any
type of data from number to entire HTML file too. Here is a list of all Field
types used in Django.  

### Basic model data types and fields list

Field Name| Description| AutoField| It An IntegerField that automatically
increments.| BigAutoField| It is a 64-bit integer, much like an AutoField
except that it is guaranteed to fit numbers from 1 to 9223372036854775807.|
BigIntegerField| It is a 64-bit integer, much like an IntegerField except that
it is guaranteed to fit numbers from -9223372036854775808 to
9223372036854775807.| BinaryField| A field to store raw binary data. |
BooleanField| A true/false field.  
The default form widget for this field is a CheckboxInput.| CharField| A field
to store text based values.| DateField| A date, represented in Python by a
datetime.date instance|  | It is used for date and time, represented in Python
by a datetime.datetime instance.| DecimalField| It is a fixed-precision
decimal number, represented in Python by a Decimal instance.| DurationField| A
field for storing periods of time.| EmailField| It is a CharField that checks
that the value is a valid email address.| FileField| It is a file-upload
field.| FloatField| It is a floating-point number represented in Python by a
float instance.| ImageField| It inherits all attributes and methods from
FileField, but also validates that the uploaded object is a valid image.|
IntegerField| It is an integer field. Values from -2147483648 to 2147483647
are safe in all databases supported by Django.| GenericIPAddressField| An IPv4
or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).|
NullBooleanField| Like a BooleanField, but allows NULL as one of the options.|
PositiveIntegerField| Like an IntegerField, but must be either positive or
zero (0).| PositiveSmallIntegerField| Like a PositiveIntegerField, but only
allows values under a certain (database-dependent) point.| SlugField| Slug is
a newspaper term. A slug is a short label for something, containing only
letters, numbers, underscores or hyphens. They’re generally used in URLs.|
SmallIntegerField| It is like an IntegerField, but only allows values under a
certain (database-dependent) point.| TextField| A large text field. The
default form widget for this field is a Textarea.| TimeField| A time,
represented in Python by a datetime.time instance.| URLField| A CharField for
a URL, validated by URLValidator.| UUIDField| A field for storing universally
unique identifiers. Uses Python’s UUID class. When used on PostgreSQL, this
stores in a uuid datatype, otherwise in a char(32).  
---|---  
  
### Relationship Fields

Django also defines a set of fields that represent relations. Field Name|
Description| ForeignKey| A many-to-one relationship. Requires two positional
arguments: the class to which the model is related and the on_delete option.|
ManyToManyField| A many-to-many relationship. Requires a positional argument:
the class to which the model is related, which works exactly the same as it
does for ForeignKey, including recursive and lazy relationships.|
OneToOneField| A one-to-one relationship. Conceptually, this is similar to a
ForeignKey with unique=True, but the “reverse” side of the relation will
directly return a single object.  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

