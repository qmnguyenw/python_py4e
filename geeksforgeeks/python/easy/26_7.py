exec() in Python



 **exec()** function is used for the dynamic execution of Python program which
can either be a string or object code. If it is a string, the string is parsed
as a suite of Python statements which is then executed unless a syntax error
occurs and if it is an object code, it is simply executed. We must be careful
that the return statements may not be used outside of function definitions not
even within the context of code passed to the exec() function. It doesn;t
returnn any value, hence returns _None_.  
 **Syntax:**

    
    
    exec(object[, globals[, locals]])
    

It can take three parameters:

  *  **object:** As already said this can be a string or object code
  *  **globals:** This can be a dictionary and the parameter is optional
  *  **locals:** This can be a mapping object and is also optional

Now let’s see how this function works. In the following code, we have used an
object code and executed it using exec() function. We have just taken the
object parameter and omitted the other two fields.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

prog= 'print("The sum of 5 and 10 is", (5+10))'

exec(prog)  
  
---  
  
 __

 __

Output:  
The sum of 5 and 10 is 15

 **Warning or Limitations**

  

  

Before using any methods inside the exec() function one must keep in mind
about what all functions do exec() support. To view this we may use dir()
function.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# The math class is used to include all the

# math functions

from math import *

exec("print(dir())")  
  
---  
  
 __

 __

Output:

    
    
    ['__builtins__', '__cached__', '__doc__', '__file__',
     '__loader__', '__name__', '__package__', '__spec__', 
    'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 
    'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 
    'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
     'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 
    'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
    'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
    'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin',
     'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
    

**Global and Local Parameters**

Python allows us to restrict the use of various variables and methods by the
use of global and local parameters, which might not be needed. These local and
global parameters are used for local or global variables mainly dictionaries.
The global parameter overtakes if the local is missing which means global can
be used for both the fields. Let’s see how the code works on passing only the
global parameter.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# Here we have passed an empty dictionary

from math import *

exec("print(dir())", {})  
  
---  
  
 __

 __

Output:

    
    
    ['__builtins__']
    

So we see that on passing an empty dictionary as a global parameter, only the
__builtins__ is displayed and no other math functions are displayed as in the
previous example. This means that only the __builtins__ will be supported for
the object parameter. This suggests that all other functions are restricted on
the object. To prove it let’s try to work with a math function and see what
happens.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# An exception will be raised

from math import *

exec("print(factorial(5))", {})  
  
---  
  
 __

 __

Output:

    
    
    No Output
    

This example should have printed 120 as output but instead, it displays No
Output and raises an exception. Although, we have imported the math module the
factorial() method failed to work because of restrictions we have set by
passing the global parameter.  
We can also allow few of the many functions to execute. Suppose we want all
other math modules to be restricted except the factorial() function.  
Example:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# factorial() will be executed

from math import *

exec("print(factorial(5))", {"factorial":factorial})  
  
---  
  
 __

 __

Output:

    
    
    120
    

We can also change the name of these predefined methods and give them user-
defined name during execution. We can change the name of the function from
**factorial()** to **fact()** , which is user-defined.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# factorial() renamed as fact

from math import *

exec('print(fact(5))', {'fact': factorial})  
  
---  
  
 __

 __

Output:

    
    
    120
    

Now let’s see what else can we do on passing both the global and local
parameters. Using local parameters we can implement the funtions according to
our need.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

from math import *

exec("print(dir())", {"built" : __builtins__}, {"sum": sum,
"iter": iter})  
  
---  
  
 __

 __

Output:

    
    
    ['dir', 'print', 'sum']
    

Through this only the sum,and iter methods along with all the built-in methods
can be executed inside exec() function.  
We can also restrict the use of __builtins__ like this:

 __

 __  
 __

 __

 __  
 __  
 __

#__builtins__ has been restricted using None

from math import *

exec("print(dir())", {"__builtins__" : None}, {"sum":
sum, "print": print, "dir": dir})  
  
---  
  
 __

 __

Output:

    
    
    ['dir', 'print', 'sum']
    

Here only the sum, print and dir methods will be executed inside exec()
function and not all built-in methods.

This article is contributed by **Chinmoy Lenka**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
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

