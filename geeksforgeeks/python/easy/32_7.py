Mathematical Functions in Python | Set 4 (Special Functions and Constants)



Some of the mathematical functions are discussed in below set 1, set 2 and set
3  
Mathematical Functions in Python | Set 1 (Numeric Functions)  
Mathematical Functions in Python | Set 2 (Logarithmic and Power Functions)  
Mathematical Functions in Python | Set 3 (Trigonometric and Angular Functions)

Special Functions and constants are discussed in this article.

 **1\. gamma()** :- This function is used to return the **gamma function** of
the argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# gamma()

 

# importing "math" for mathematical operations

import math

 

a = 4

 

# returning the gamma() of 4

print ("The gamma() of 4 is : ", end="")

print (math.gamma(a))  
  
---  
  
 __

 __

Output:

    
    
    The gamma() of 4 is : 6.0
    

**2\. pi** :- This is an inbuilt constant that outputs the **value of
pi(3.141592)**.

  

  

 **3\. e** :- This is an inbuilt constant that outputs the **value of
e(2.718281)**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# const. pi and e

 

# importing "math" for mathematical operations

import math

 

# returning the value of const. pi

print ("The value of const. pi is : ", end="")

print (math.pi)

 

# returning the value of const. e

print ("The value of const. e is : ", end="")

print (math.e)  
  
---  
  
 __

 __

Output:

    
    
    The value of const. pi is : 3.141592653589793
    The value of const. e is : 2.718281828459045
    

**4\. inf** :- This is a **positive floating point infinity constant**. -inf
is used to denote the negative floating point infinity. This constant is
defined in python 3.5 and above.

 **5\. isinf()** :- This function is used to **check** whether the value is an
**infinity or not.**

 **6\. nan** :- This constant denotes “Not a number” in python. This constant
is defined in python 3.5 and above.

 **7\. isnan()** :- This function returns **true if the number is “nan”** else
returns false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# inf, nan, isinf(), isnan()

 

# importing "math" for mathematical operations

import math

 

# checking if number is nan

if (math.isnan(math.nan)):

 print ("The number is nan")

else : print ("The number is not nan")

 

# checking if number is positive infinity

if (math.isinf(math.inf)):

 print ("The number is positive infinity")

else : print ("The number is not positive infinity")  
  
---  
  
 __

 __

Output:

    
    
    The number is nan
    The number is positive infinity
    

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

