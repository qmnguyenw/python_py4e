Precision Handling in Python



Python in its definition allows to handle precision of floating point numbers
in several ways using different functions. Most of them are defined under the
“ **math** ” module. Some of the most used operations are discussed in this
article.

 **1\. trunc() :-** This function is used to **eliminate all decimal part** of
the floating point number and return the integer without the decimal part.

 **2\. ceil() :-** This function is used to print the **least integer greater
than the given number**.

 **3\. floor() :-** This function is used to print the **greatest integer
smaller than the given integer**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate ceil(), trunc()

# and floor()

 

# importing "math" for precision function

import math

 

# initializing value

a = 3.4536

 

# using trunc() to print integer after truncating 

print ("The integral value of number is : ",end="")

print (math.trunc(a))

 

# using ceil() to print number after ceiling 

print ("The smallest integer greater than number is : ",end="")

print (math.ceil(a))

 

# using floor() to print number after flooring 

print ("The greatest integer smaller than number is : ",end="")

print (math.floor(a))  
  
---  
  
 __

 __

Output :

  

  

    
    
    The integral value of number is : 3
    The smallest integer greater than number is : 4
    The greatest integer smaller than number is : 3
    

**

Setting Precision

**

There are many ways to set precision of floating point value. Some of them is
discussed below.  
  
 **1\. Using “%”** :- “%” operator is used to format as well as set precision
in python. This is similar to “printf” statement in C programming.

 **2\. Using format() :-** This is yet another way to format the string for
setting precision.

 **3\. Using round(x,n) :-** This function takes 2 arguments, **number and the
number till which we want decimal part rounded.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate precision

# and round()

 

# initializing value

a = 3.4536

 

# using "%" to print value till 2 decimal places 

print ("The value of number till 2 decimal place(using %) is :
",end="")

print ('%.2f'%a)

 

# using format() to print value till 2 decimal places 

print ("The value of number till 2 decimal place(using format()) is :
",end="")

print ("{0:.2f}".format(a))

 

# using round() to print value till 2 decimal places 

print ("The value of number till 2 decimal place(using round()) is :
",end="")

print (round(a,2))  
  
---  
  
 __

 __

Output :

    
    
    The value of number till 2 decimal place(using %) is : 3.45
    The value of number till 2 decimal place(using format()) is : 3.45
    The value of number till 2 decimal place(using round()) is : 3.45
    

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

