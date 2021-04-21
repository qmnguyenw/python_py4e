Help function in Python



The python help function is used to display the documentation of modules,
functions, classes, keywords etc.  
The help function has the following syntax:

    
    
    help([object])
    

If the help function is passed without an argument, then the interactive help
utility starts up on the console.

Let us check the documentation of the print function in python console.

 __

 __  
 __

 __

 __  
 __  
 __

help(print)  
  
---  
  
 __

 __

It gives the following output:

    
    
    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    

Help function output can also be defined for user defined functions and
classes. The docstring(documentation string) is used for documentation. It is
nested inside triple quotes and is the first statement within a class or
function or a module.

  

  

Let us define a class with functions:

 __

 __  
 __

 __

 __  
 __  
 __

class Helper:

 def __init__(self):

 '''The helper class is initialized'''

 

 def print_help(self):

 '''Returns the help description'''

 print('helper description')

 

help(Helper)

help(Helper.print_help)  
  
---  
  
 __

 __

On running the above program, we get the output of the first help function as
shown below:

    
    
    Help on class Helper in module __main__:
    
    class Helper(builtins.object)
     |  Methods defined here:
     |  
     |  __init__(self)
     |      The helper class is initialized
     |  
     |  print_help(self)
     |      Returns the help description
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    Help on function print_help in module __main__:
    
    print_help(self)
        Returns the help description
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

