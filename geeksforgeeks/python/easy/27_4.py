Log functions in Python



Python offers many inbuild logarithmic functions under the module “ **math** ”
which allows us to compute logs using a single line. There are 4 variants of
logarithmic functions, all of which are discussed in this article.

 **1\. log(a,(Base)) :** This function is used to compute the **natural
logarithm** (Base e) of a. If 2 arguments are passed, it computes the
logarithm of desired base of argument a, numerically value of
**log(a)/log(Base)**.

    
    
    **Syntax :**
    math.log(a,Base)
    **Parameters :**
    **a :** The numeric value
    **Base :**  Base to which the logarithm has to be computed.
    **Return Value :**
    Returns natural log if 1 argument is passed and log with
    specified base if 2 arguments are passed.
    **Exceptions :**
    Raises ValueError is a negative no. is passed as argument.
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate the working of

# log(a,Base)

 

import math

 

# Printing the log base e of 14

print ("Natural logarithm of 14 is : ", end="")

print (math.log(14))

 

# Printing the log base 5 of 14

print ("Logarithm base 5 of 14 is : ", end="")

print (math.log(14,5))  
  
---  
  
 __

 __

Output :

    
    
    Natural logarithm of 14 is : 2.6390573296152584
    Logarithm base 5 of 14 is : 1.6397385131955606
    

**2\. log2(a) :** This function is used to compute the **logarithm base 2** of
a. Displays more accurate result than log(a,2).

    
    
    **Syntax :**
    math.log2(a)
    **Parameters :**
    **a :** The numeric value
    **Return Value :**
    Returns logarithm base 2 of a
    **Exceptions :**
    Raises ValueError is a negative no. is passed as argument.
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate the working of

# log2(a)

 

import math

 

# Printing the log base 2 of 14

print ("Logarithm base 2 of 14 is : ", end="")

print (math.log2(14))  
  
---  
  
 __

 __

Output :

  

  

    
    
    Logarithm base 2 of 14 is : 3.807354922057604
    

**3\. log10(a) :** This function is used to compute the **logarithm base 10**
of a. Displays more accurate result than log(a,10).

    
    
    **Syntax :**
    math.log10(a)
    **Parameters :**
    **a :** The numeric value
    **Return Value :**
    Returns logarithm base 10 of a
    **Exceptions :**
    Raises ValueError is a negative no. is passed as argument.
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate the working of

# log10(a)

 

import math

 

# Printing the log base 10 of 14

print ("Logarithm base 10 of 14 is : ", end="")

print (math.log10(14))  
  
---  
  
 __

 __

Output :

    
    
    Logarithm base 10 of 14 is : 1.146128035678238
    

**3\. log1p(a) :** This function is used to compute **logarithm(1+a)** .

    
    
    **Syntax :**
    math.log1p(a)
    **Parameters :**
    **a :** The numeric value
    **Return Value :**
    Returns log(1+a)
    **Exceptions :**
    Raises ValueError is a negative no. is passed as argument.
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate the working of

# log1p(a)

 

import math

 

# Printing the log(1+a) of 14

print ("Logarithm(1+a) value of 14 is : ", end="")

print (math.log1p(14))  
  
---  
  
 __

 __

Output :

    
    
    Logarithm(1+a) value of 14 is : 2.70805020110221
    

**Exception**

 **1\. ValueError :** This function returns value error if number is
**negative**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the Exception of

# log(a)

 

import math

 

# Printing the log(a) of -14

# Throws Exception

print ("log(a) value of -14 is : ", end="")

print (math.log(-14))  
  
---  
  
 __

 __

Output :

    
    
    log(a) value of -14 is : 
    

Runtime Error :

    
    
    Traceback (most recent call last):
      File "/home/8a74e9d7e5adfdb902ab15712cbaafe2.py", line 9, in 
        print (math.log(-14))
    ValueError: math domain error
    

**Practical Application**

One of the application of log10() function is that it is used to compute the
**no. of digits of a number**. Code below illustrates the same.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the Application of

# log10(a)

 

import math

 

# Printing no. of digits in 73293

print ("The number of digits in 73293 are : ", end="")

print (int(math.log10(73293) + 1))  
  
---  
  
 __

 __

Output :

    
    
    The number of digits in 73293 are : 5
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
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

