How to check if a string is a valid keyword in Python?



 **Defining a Keyword**

In programming, a keyword is a “ **reserved word** ” by the language which
**convey a special meaning to the interpreter**. It may be a command or a
parameter. Keywords **cannot be used as a variable name** in the program
snippet.

 **Keywords in Python:** Python language also reserves some of keywords that
convey special meaning. Knowledge of these is necessary part of learning this
language. Below is list of keywords registered by python .  
 **  
False, elif, lambda,  
None, else, nonlocal,  
True, except, not,  
and, finally, or,  
as, for, pass,  
assert, from, raise,  
break, global, return,  
class, if, try,  
continue, import, while,  
def, in, with,  
del, is, yield,  
**

 **How to check if a string is keyword?**

Python in its language defines an inbuilt module “ **keyword** ” which handles
certain operations related to keywords. A function “ **iskeyword()** ” checks
if a string is keyword or not. Returns **true if a string is keyword, else
returns false**.

 __

 __  
 __

 __

 __  
 __  
 __

#Instead of writing this massive Python code

#we can also code this in a different way

 

#Python code to demonstrate working of iskeyword()

 

# importing "keyword" for keyword operations

import keyword

import keyword

# initializing strings for testing while putting them in an array

keys = ["for", "while", "tanisha", "break", "sky",

"elif", "assert", "pulkit", "lambda", "else",
"sakshar"]

 

for i in range(len(keys)):

 # checking which are keywords

 if keyword.iskeyword(keys[i]):

 print(keys[i] + " is python keyword")

 else:

 print(keys[i] + " is not a python keyword")  
  
---  
  
 __

 __

Output:

  

  

    
    
    for is a python keyword
    geeksforgeeks is not a python keyword
    elif is a python keyword
    elseif is not a python keyword
    nikhil is not a python keyword
    assert is a python keyword
    shambhavi is not a python keyword
    True is a python keyword
    False is a python keyword
    akshat is not a python keyword
    akash is not a python keyword
    break is a python keyword
    ashty is not a python keyword
    lambda is a python keyword
    suman is not a python keyword
    try is a python keyword
    vaishnavi is not a python keyword
    

**How to print list of all keywords**

Sometimes, remembering all the keywords can be a difficult task while
assigning variable names. Hence a function “ **kwlist()** ” is provided in
“keyword” module which **prints all the 33 python keywords**.

 __

 __  
 __

 __

 __  
 __  
 __

#Python code to demonstrate working of iskeyword()

 

# importing "keyword" for keyword operations

import keyword

 

# printing all keywords at once using "kwlist()"

print ("The list of keywords is : ")

print (keyword.kwlist)  
  
---  
  
 __

 __

Output:

    
    
    The list of keywords is : 
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
    'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
    'try', 'while', 'with', 'yield']
    

  
  
**Next Articles:**

  * Keywords in Python | Set 1
  * Keywords in Python | Set 2

This article is contributed by **Manjeet Singh(S.Nandini)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

