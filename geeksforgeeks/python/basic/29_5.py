Division Operators in Python



Consider the below statements in Python.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate the use of

# "//" for integers

print (5//2)

print (-5//2)  
  
---  
  
 __

 __

Output:

    
    
    2
    -3

The first output is fine, but the second one may be surprised if we are coming
Java/C++ world. In Python, the “//” operator works as a floor division for
integer and float arguments. However, the operator / returns a float value if
one of the arguments is a float (this is similar to C++)  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate use of

# "/" for floating point numbers

print (5.0/2)

print (-5.0/2)  
  
---  
  
 __

 __

Output:

    
    
    2.5
    -2.5

 **The real floor division operator is “//”. It returns floor value for both
integer and floating point arguments.**  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate use of

# "//" for both integers and floating points

print (5//2)

print (-5//2)

print (5.0//2)

print (-5.0//2)  
  
---  
  
 __

 __

Output:

    
    
    2
    -3
    2.0
    -3.0

See this for example.  

This article is contributed by **Arpit Agrawal**. Please write comments if you
find anything incorrect, or you want to share more information about the topic
discussed above  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

