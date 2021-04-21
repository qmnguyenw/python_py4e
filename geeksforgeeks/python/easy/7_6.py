Python – Invoking Functions with and without Parentheses



Functions in Python are the defined blocks of code that perform a specific
task. In this section, we will discuss the difference in invoking functions
with and without Parentheses.

  * When we call a **function with parentheses** , the _function gets execute_ and returns the result to the callable.
  * In another case, when we call a **function without parentheses** , a _function reference is sent to the callable_ rather than executing the function itself.

Let’s discuss 3 important concepts:

  * Invoking functions
  * Return functions
  * Passing functions

## Invoking functions –

The below function performs a simple task, string concatenation. Here we will
invoke the function concatenate_string with and without parentheses and see
the difference.

 __

 __  
 __

 __

 __  
 __  
 __

def concatenate_string(*args):

 string1 = args[0]

 string2 = args[1]

 

 return string1 + string2

 

obj = concatenate_string('Hello, ', 'George')

print('Function call with Parentheses: ')

print(obj)

 

obj = concatenate_string

print('Function call without Parentheses: ')

print(obj)  
  
---  
  
 __

 __

 **Output**

    
    
    Function call with Parentheses: 
    Hello, George
    Function call without Parentheses:
    <function concatenate_string at 0x7f0bb991df28>
    

For the first case, when we call concatenate_string('Hello, ', 'George'),
the function executes and returns the concatenated string.  
And, for the second case, when we call concatenate_string i.e. without
parentheses, a reference is passed to the callable rather than executing the
function itself. Here the callable can decide what to do with the reference.

  

  

## Return Functions –

From the above discussion you can understand that, when the function is called
with parentheses, the code is executed and returns the result. And, when it is
called without parentheses, a function reference is returned to the callable.  
So, what happens when a function is coded along with a return statement with
parentheses and without parentheses. Let’s go through an example.

 **With Parentheses**

 __

 __  
 __

 __

 __  
 __  
 __

def concatenate_string(*args):

 

 string1 = args[0]

 string2 = args[1]

 

 def merge_string(string1, string2):

 return string1 + string2

 

 return merge_string(string1, string2)

 

def func():

 conc_obj = concatenate_string('Hello, ', 'George')

 print(conc_obj)

 

func()  
  
---  
  
 __

 __

 **Output**

    
    
    Hello, George

From the above example, it’s clear that the merge_string is a function
within the function concatenate_string and the main function
(concatenate_string) returns the sub-function (merge_string) to the
caller.

    
    
     return merge_string(string1, string2) 

Here merge_string is invoked with parentheses, hence it executes and
provides the result to the concatenate_string from where the result is
passed to func.

 **Without Parentheses**

 __

 __  
 __

 __

 __  
 __  
 __

def concatenate_string():

 

 def merge_string(string1, string2):

 return string1 + string2

 

 return merge_string

 

def func():

 

 # return the reference of merge_string func

 conc_obj = concatenate_string()

 print(conc_obj) # prints the reference 

 

 # executes the reference 

 print(conc_obj('Hello, ', 'George')) 

 

func()  
  
---  
  
 __

 __

 **Output:**

    
    
    <function concatenate_string..merge_string at 0x7f1e54ebc158>
    Hello, George
    

Since the merge_string is used without parentheses, the concatenate_string
passes the function reference to the callable func rather than executing the
merge_string.

  

  

    
    
    return merge_string

Hence, we can conclude that when we code sub-function with parentheses in a
return statement, the main function executes the sub-function and passes the
result to the callable.  
And, when we code subfunction without parentheses in a return statement, the
main function passes the sub-function reference to the callable rather than
executing it. Here the callable decides what to do with the reference.

## Passing Functions –

You can pass a function as an argument by creating the reference, calling the
function without parentheses, and provide it as an argument. Let’s look into
the code.

 __

 __  
 __

 __

 __  
 __  
 __

def concatenate_string(*args):

 string1 = args[0]

 string2 = args[1]

 

 def merge_string(string1, string2):

 return string1 + string2 # string merge

 

 # executes merge_string and return the result

 return merge_string(string1, string2)

 

def function_call(function):

 string1 = 'Hello, '

 string2 = 'George'

 return function(string1, string2)

 

# passing function as argument

print(function_call(concatenate_string))   
  
---  
  
__

__

**Output:**

    
    
    Hello, George

In this case, the reference of concatenate_string is passed to the
function_call as an argument.

    
    
    function_call(concatenate_string)

Inside function_call, it executes the concatenate_string using the reference
and returns the result to the callable.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

