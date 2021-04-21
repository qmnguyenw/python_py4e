What does the Double Star operator mean in Python?



Double Star or (**) is one of the Arithmetic Operator (Like +, -, *, **, /,
//, %) in Python Language. It is also known as Power Operator.

###  **What is the Precedence of Arithmetic Operators?**

Arithmetic operators follow the same precedence rules as in mathematics, and
they are: exponential is performed first, multiplication and division are
performed next ,followed by addition and subtraction.

 **Arithmetic operators priorities order in Decreasing Mode:**

    
    
    ()   >>   **   >>   *  >>  /  >>  //  >>  %   >>   +   >>   -
    

### Uses of Double Star operator:

 **As Exponentiation Operator**

For numeric data types, double-asterisk (**) is defined as an Exponentiation
Operator:

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to Demonstrate the Exponential Operactor

 

a = 2

b = 5

 

# using double asterisk operator

c = a**b

print(c)

 

 

# using double asterisk operator

z = 2 * (4 ** 2) + 3 * (4 ** 2 - 10)

print(z)  
  
---  
  
 __

 __

 **Output:**

    
    
    32
    50

###

**As arguments in functions and methods**

In a function definition, the double asterisk is also known _**kwargs_. They
used to pass a keyword, variable-length argument dictionary to a function. The
two asterisks (**) are the important element here, as the word _kwargs_ is
conventionally used, though not enforced by the language.

First, let’s simply print out the _**kwargs_ arguments that we pass to a
function. We’ll create a short function to do this:

#### Example:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to create a function to get a dictionary of names.

# Here, we will start with a dictionary of three names

 

 

def function(**kwargs):

 for key, value in kwargs.items():

 print("The value of {} is {}".format(key, value))

 

 

function(name_1="Shrey", name_2="Rohan", name_3="Ayush")  
  
---  
  
 __

 __

 **Output:**

    
    
    The value of name_1 is Shrey
    The value of name_2 is Rohan
    The value of name_3 is Ayush

Now here is another example where we will pass additional arguments to the
function to show that _**kwargs_ will accept any number of arguments:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to create a function to get a dictionary of as many names

# you want to include in your Dictionary

 

 

def function(**kwargs):

 for key, value in kwargs.items():

 print("The value of {} is {}".format(key, value))

 

 

function(

 name_1="Ayush",

 name_2="Aman",

 name_3="Harman",

 name_4="Babber",

 name_5="Striver",

)  
  
---  
  
 __

 __

 **Output:**

    
    
    The value of name_1 is Ayush
    The value of name_2 is Aman
    The value of name_3 is Harman
    The value of name_4 is Babber
    The value of name_5 is Striver

### Conclusion:

Using _**kwargs_ provides us with the flexibility to use keyword arguments in
our program. When we use _**kwargs_ as a parameter, we don’t need to know how
many arguments we would eventually like to pass to a function. Creating
functions that accept _**kwargs_ are best used in situations where you expect
that the number of inputs within the argument list will remain relatively
small.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

