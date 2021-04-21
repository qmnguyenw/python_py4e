Mathematical Functions in Python | Set 2 (Logarithmic and Power Functions)



Numeric functions are discussed in set 1 below

Mathematical Functions in Python | Set 1 ( Numeric Functions)

Logarithmic and power functions are discussed in this set.

 **1\. exp(a)** :- This function returns the value of **e raised to the power
a (e**a)**.

 **2\. log(a, b)** :- This function returns the logarithmic **value of a with
base b**. If base is not mentioned, the computed value is of natural log.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# exp() and log()

 

# importing "math" for mathematical operations

import math

 

# returning the exp of 4

print ("The e**4 value is : ", end="")

print (math.exp(4))

 

# returning the log of 2,3

print ("The value of log 2 with base 3 is : ", end="")

print (math.log(2,3))  
  
---  
  
 __

 __

Output:

    
    
    The e**4 value is : 54.598150033144236
    The value of log 2 with base 3 is : 0.6309297535714574
    

**3\. log2(a)** :- This function computes value of **log a with base 2**. This
value is **more accurate** than the value of the function discussed above.

 **4\. log10(a)** :- This function computes value of **log a with base 10**.
This value is **more accurate** than the value of the function discussed
above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# log2() and log10()

 

# importing "math" for mathematical operations

import math

 

# returning the log2 of 16

print ("The value of log2 of 16 is : ", end="")

print (math.log2(16))

 

# returning the log10 of 10000

print ("The value of log10 of 10000 is : ", end="")

print (math.log10(10000))  
  
---  
  
 __

 __

Output:

    
    
    The value of log2 of 16 is : 4.0
    The value of log10 of 10000 is : 4.0
    

**5\. pow(a, b)** :- This function is used to compute value of **a raised to
the power b (a**b)**.

 **6\. sqrt()** :- This function returns the **square root** of the number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# pow() and sqrt()

 

# importing "math" for mathematical operations

import math

 

# returning the value of 3**2

print ("The value of 3 to the power 2 is : ", end="")

print (math.pow(3,2))

 

# returning the square root of 25

print ("The value of square root of 25 : ", end="")

print (math.sqrt(25))  
  
---  
  
 __

 __

Output:

    
    
    The value of 3 to the power 2 is : 9.0
    The value of square root of 25 : 5.0
    

This article is contributed by **Manjeet Singh** .If you like GeeksforGeeks
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

