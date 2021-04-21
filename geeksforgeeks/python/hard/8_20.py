Private Variables in Python



 **Prerequisite:**Underscore in Python  
In Python, there is no existence of “Private” instance variables that cannot
be accessed except inside an object. However, a convention is being followed
by most Python code and coders i.e., a name prefixed with an underscore, For
e.g. **_geek** should be treated as a non-public part of the API or any Python
code, whether it is a function, a method, or a data member. While going
through this we would also try to understand the concept of various forms of
trailing underscores, for e.g., for _ in range(10), __init__(self).  

**Mangling and how it works**

In Python, there is something called name mangling, which means that there is
a limited support for a valid use-case for class-private members basically to
avoid name clashes of names with names defined by subclasses. Any identifier
of the form __geek (at least two leading underscores or at most one trailing
underscore) is replaced with _classname__geek, where classname is the current
class name with a leading underscore(s) stripped. As long as it occurs within
the definition of the class, this mangling is done. This is helpful for
letting subclasses override methods without breaking intraclass method calls.  
Let’s look at this example and try to find out how this underscore works:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate how mangling works

class Map:

 def __init__(self, iterate):

 self.list = []

 self.__geek(iterate)

 def geek(self, iterate):

 for item in iterate:

 self.list.append(item)

 # private copy of original geek() method

 __geek = geek 

class MapSubclass(Map):

 

 # provides new signature for geek() but

 # does not break __init__()

 def geek(self, key, value): 

 for i in zip(keys, value):

 self.list.append(i)  
  
---  
  
 __

 __

The mangling rules are designed mostly to avoid accidents but it is still
possible to access or modify a variable that is considered private. This can
even be useful in special circumstances, such as in the debugger.  

**_Single Leading Underscores**

  

  

So basically one underline in the beginning of a method, function, or data
member means you shouldn’t access this method because it’s not part of the
API. Let’s look at this snippet of code:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# how single underscore works

def _get_errors(self):

 if self._errors is None:

 self.full_clean()

 return self._errors

errors = property(_get_errors)  
  
---  
  
 __

 __

The snippet is taken from the Django source code (django/forms/forms.py). This
suggests that errors is a property, and it’s also a part of the API, but the
method, _get_errors, is “private”, so one shouldn’t access it.  

**__Double Leading Underscores**

Two underlines, in the beginning, cause a lot of confusion. This is about
syntax rather than a convention. double underscore will mangle the attribute
names of a class to avoid conflicts of attribute names between classes. For
example:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate how double

# underscore at the beginning works

class Geek:

 def _single_method(self):

 pass

 def __double_method(self): # for mangling

 pass

class Pyth(Geek):

 def __double_method(self): # for mangling

 pass  
  
---  
  
 __

 __

 **__Double leading and Double trailing underscores__**

There’s another case of double leading and trailing underscores. We follow
this while using special variables or methods (called “magic method”) such
as__len__, __init__. These methods provide special syntactic features to the
names. For example, __file__ indicates the location of the Python file, __eq__
is executed when a == b expression is executed.  
**Example:**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate double leading and

# double trailing underscore works

class Geek:

 # '__init__' for initializing, this is a

 # special method 

 def __init__(self, ab):

 self.ab = ab

 # custom special method. try not to use it

 def __custom__(self):

 pass  
  
---  
  
 __

 __

This article is contributed by **Chinmoy Lenka**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
I have referred Python Docs, hackernoon.com and igorsobreira.com  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

