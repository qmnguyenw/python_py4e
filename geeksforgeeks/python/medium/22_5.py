Why Python is called Dynamically Typed?



Python variable assignment is different from some of the popular languages
like c, c++ and java. There is no declaration of a variable, just an
assignment statement.

Let us see why?  
When we **declare a variable** in C or alike languages, this sets aside an
area of memory for holding values allowed by the **data type** of the
variable. The memory allocated will be interpreted as the data type suggests.
If it’s an integer variable the memory allocated will be read as an integer
and so on. When we assign or initialize it with some value, that value will
get stored at that memory location. At compile time, initial value or assigned
value will be checked. So we cannot mix types. Example: initializing a string
value to an int variable is not allowed and the program will not compile.

But Python is a **dynamically typed** language. It doesn’t know about the type
of the variable until the code is run. So declaration is of no use. What it
does is, It stores that value at some memory location and then binds that
variable name to that memory container. And makes the contents of the
container accessible through that variable name. So the data type does not
matter. As it will get to know the type of the value at run-time.

 __

 __  
 __

 __

 __  
 __  
 __

# This will store 6 in the memory and binds the

# name x to it. After it runs, type of x will

# be int.

x = 6

 

print(type(x))

 

# This will store 'hello' at some location int 

# the memory and binds name x to it. After it

# runs type of x will be str.

x = 'hello'

 

print(type(x))  
  
---  
  
 __

 __

 **Output:**

    
    
    <class 'int'>
    <class 'str'>
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

