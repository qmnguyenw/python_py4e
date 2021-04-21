Underscore (_) in Python



Following are different places where _ is used in Python:

  1. Single Underscore:
    * In Interpreter
    * After a name
    * Before a name
  2. Double Underscore:
    1. __leading_double_underscore
    2. __before_after__

 **Single Underscore**

 **In Interpreter:**  
_ returns the value of last executed expression value in Python
Prompt/Interpreter

 __

 __  
 __

 __

 __  
 __  
 __

>>> a = 10

>>> b = 10

>>> _

Traceback (most recent call last):

File "<stdin>", line 1, in <module>

NameError: name '_' is not defined

>>> a+b

20

>>> _

20

>>> _ * 2

40

>>> _

40

>>> _ / 2

20  
  
---  
  
 __

 __

 **For ignoring values:**  
Multiple time we do not want return values at that time assign those values to
Underscore. It used as throwaway variable.

 __

 __  
 __

 __

 __  
 __  
 __

# Ignore a value of specific location/index

for _ in range(10)

 print ("Test")

 

# Ignore a value when unpacking

a,b,_,_ = my_method(var1)  
  
---  
  
 __

 __

 **After a name**  
Python has their by default keywords which we can not use as the variable
name. To avoid such conflict between python keyword and variable we use
underscore after name

  

  

Example:

 __

 __  
 __

 __

 __  
 __  
 __

>>> class MyClass():

... def __init__(self):

... print ("OWK")

 

>>> def my_defination(var1 = 1, class_ = MyClass):

... print (var1)

... print (class_)

 

>>> my_defination()

1

__main__.MyClass

>>>  
  
---  
  
 __

 __

 **Before a name**  
Leading Underscore before variable/function/method name indicates to
programmer that It is for internal use only, that can be modified whenever
class want.

Here name prefix by underscore is treated as non-public. If specify **from
Import *** all the name starts with _ will not import. Python does not specify
truly private so this ones can be call directly from other modules if it is
specified in __all__, We also call it **weak Private**

 __

 __  
 __

 __

 __  
 __  
 __

class Prefix:

... def __init__(self):

... self.public = 10

... self._private = 12

>>> test = Prefix()

>>> test.public

10

>>> test._private

12  
  
---  
  
 __

 __

Python class_file.py

 __

 __  
 __

 __

 __  
 __  
 __

def public_api():

 print ("public api")

 

def _private_api():

 print ("private api")  
  
---  
  
 __

 __

Calling file from Prompt

 __

 __  
 __

 __

 __  
 __  
 __

>>> from class_file import *

>>> public_api()

public api

 

>>> _private_api()

Traceback (most recent call last):

File "<stdin>", line 1, in <module>

NameError: name '_private_api' is not defined

 

>>> import class_file

>>> class_file.public_api()

public api

>>> class_file._private_api()

private api  
  
---  
  
 __

 __

 **Double Underscore(__)**

 **__leading_double_underscore**  
Leading double underscore tell python interpreter to rewrite name in order to
avoid conflict in subclass.Interpreter changes variable name with class
extension and that feature known as the Mangling.  
testFile.py

 __

 __  
 __

 __

 __  
 __  
 __

class Myclass():

 def __init__(self):

 self.__variable = 10  
  
---  
  
 __

 __

Calling from Interpreter

  

  

 __

 __  
 __

 __

 __  
 __  
 __

>>> import testFile

>>> obj = testFile.Myclass()

>>> obj.__variable

Traceback (most recent call last):

File "", line 1, in

AttributeError: Myclass instance has no attribute '__variable'

nce has no attribute 'Myclass'

>>> obj._Myclass__variable

10  
  
---  
  
 __

 __

In Mangling python interpreter modify variable name with ___. So Multiple time
It use as the Private member because another class can not access that
variable directly. Main purpose for __ is to use variable/method in class only
If you want to use it outside of the class you can make public api

 __

 __  
 __

 __

 __  
 __  
 __

class Myclass():

 def __init__(self):

 self.__variable = 10

 def func(self)

 print (self.__variable)  
  
---  
  
 __

 __

Calling from Interpreter

 __

 __  
 __

 __

 __  
 __  
 __

>>> import testFile

>>> obj = testFile.Myclass()

>>> obj.func()

10  
  
---  
  
 __

 __

 **__BEFORE_AFTER__**  
Name with start with __ and ends with same considers special methods in
Python. Python provide this methods to use it as the operator overloading
depending on the user.

Python provides this convention to differentiate between the user defined
function with the module’s function

 __

 __  
 __

 __

 __  
 __  
 __

class Myclass():

 def __add__(self,a,b):

 print (a*b)  
  
---  
  
 __

 __

Calling from Interpreter

 __

 __  
 __

 __

 __  
 __  
 __

>>> import testFile

>>> obj = testFile.Myclass()

>>> obj.__add__(1,2)

2

>>> obj.__add__(5,2)

10  
  
---  
  
 __

 __

This article is contributed by **Nirmi Shah**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

