eval in Python



This article discusses a built-in function in Python, **eval**.

It is an interesting hack/utility in Python which lets a Python program run
Python code within itself.

The **eval()** method parses the expression passed to it and runs python
expression(code) within the program.

The syntax of **eval** is:

    
    
    eval(expression, globals=None, locals=None)
    

  * **expression:** this string is parsed and evaluated as a Python expression
  *  **globals (optional):** a dictionary to specify the available global methods and variables.
  *  **locals (optional):** another dictionary to specify the available local methods and variables.

Let us explore it with the help of a simple Python program:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from math import *

 

def secret_function():

 return "Secret key is 1234"

 

def function_creator():

 

 # expression to be evaluated

 expr = input("Enter the function(in terms of x):")

 

 # variable used in expression

 x = int(input("Enter the value of x:"))

 

 # evaluating expression

 y = eval(expr)

 

 # printing evaluated result

 print("y = {}".format(y))

 

if __name__ == "__main__":

 function_creator()  
  
---  
  
 __

 __

 **function_creator** is a function which evaluates the mathematical functions
created by user.

Consider an output:

    
    
    Enter the function(in terms of x):x*(x+1)*(x+2)
    Enter the value of x:3
    y = 60

Let us analyze the code a bit:

  * The above function takes any expression in variable **x** as input.
  * Then user has to enter a value of **x**.
  * Finally, we evaluate the python expression using **eval()** built-in function by passing the **expr** as argument.

###

 **Vulnerability issues with eval**

Our current version of **function_creator** has a few vulnerabilities.

The user can easily expose hidden values in the program, or call a dangerous
function as eval will execute anything passed to it.

For example, if you input like this:

    
    
    Enter the function(in terms of x):secret_function()
    Enter the value of x:0
    

You will get output:

  

  

    
    
    y = Secret key is 1234
    

Also, consider the situation when you have imported **os** module in your
python program. The os module provides portable way to use operating system
functionalities like: read or write a file. A single command can delete all
files in your system!

Of course in most cases (like desktop programs) the user can’t do any more
than they could do by writing their own python script, but in some
applications (like web apps, kiosk computers), this could be a risk!

The solution is to restrict **eval** to only the functions and variables we
want to make available.

 **Making eval safe**

 **eval** function comes with the facility of explicitly passing a list of
functions or variables that it can access. We need to pass it as argument in
the form of a dictionary.

Consider the example below:

 __

 __  
 __

 __

 __  
 __  
 __

from math import *

 

def secret_function():

 return "Secret key is 1234"

 

def function_creator():

 

 # expression to be evaluated

 expr = input("Enter the function(in terms of x):")

 

 # variable used in expression

 x = int(input("Enter the value of x:"))

 

 # passing variable x in safe dictionary

 safe_dict['x'] = x

 

 # evaluating expression

 y = eval(expr, {"__builtins__":None}, safe_dict)

 

 # printing evaluated result

 print("y = {}".format(y))

 

if __name__ == "__main__":

 

 # list of safe methods

 safe_list = ['acos', 'asin', 'atan', 'atan2',
'ceil', 'cos',

 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',

 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',

 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh',
'sqrt',

 'tan', 'tanh']

 

 # creating a dictionary of safe methods

 safe_dict = dict([(k, locals().get(k, None)) for k in
safe_list])

 

 function_creator()  
  
---  
  
 __

 __

Now if we try to run above program like:

    
    
    Enter the function(in terms of x):secret_function()
    Enter the value of x:0
    

We get output:

    
    
    NameError: name 'secret_function' is not defined
    

Let us analyze above code step by step:

  * First of all, we create a list of methods we want to allow as **safe_list**.
  * Next, we create a dictionary of safe methods. In this dictionary, **keys** are the method names and **values** are their local namespaces.
    
        safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
    

**locals()** is a built-in method which returns a dictionary which maps all
the methods and variables in local scope with their namespaces.

  *     safe_dict['x'] = x
    

Here, we add local variable **x** to the safe_dict too. No local variable
other than **x** will get identified by **eval** function.

  *  **eval** accepts dictionaries of **local** as well as **global** variables as arguments. So, in order to ensure that none of the built-in methods is available to **eval** expression, we pass another dictionary along with **safe_dict** as well, as shown below:
    
        y = eval(expr, {"__builtins__":None}, safe_dict)
    

So, in this way, we have made our **eval** function safe from any possible
hacks!

 **Uses of eval**

 **eval** is not much used due to security reasons as we explored above.

Still, it comes handy in some situations like:

  * You may want to use it to allow users to enter their own “scriptlets”: small expressions (or even small functions), that can be used to customize the behavior of a complex system.
  * eval is also sometimes used in applications needing to evaluate math expressions. This is much easier than writing an expression parser.

This blog is contributed by Nikhil Kumar. If you like GeeksforGeeks and would
like to contribute, you can also write an article using
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

