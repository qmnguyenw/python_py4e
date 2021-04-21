Inplace Operators in Python | Set 2 (ixor(), iand(), ipow(),…)



Inplace Operators in Python | Set 1(iadd(), isub(), iconcat()…)

More functions are discussed in this articles.

 **1\. ixor()** :- This function is used to **assign and xor the current
value**. This operation does “ **a^ = b** ” operation. Assigning is **not**
performed in case of immutable containers, such as strings, numbers and
tuples.

 **2\. ipow()** :- This function is used to **assign and exponentiate the
current value**. This operation does “ **a ** = b** ” operation. Assigning is
**not** performed in case of immutable containers, such as strings, numbers
and tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# ixor() and ipow()

 

# importing operator to handle operator operations

import operator

 

# using ixor() to exclusive or and assign value

x = operator.ixor(10,5);

 

# printing the modified value

print ("The value after xoring and assigning : ",end="")

print (x)

 

# using ipow() to exponentiate and assign value

x = operator.ipow(5,4);

 

# printing the modified value

print ("The value after exponentiating and assigning : ",end="")

print (x)  
  
---  
  
 __

 __

Output:

  

  

    
    
    The value after xoring and assigning : 15
    The value after exponentiating and assigning : 625
    

**3\. iand()** :- This function is used to **assign and bitwise and the
current value**. This operation does “ **a &= b**” operation. Assigning is
**not** performed in case of immutable containers, such as strings, numbers
and tuples.

 **4\. ior()** :- This function is used to **assign and bitwise or the current
value**. This operation does “ **a |=b** ” operation. Assigning is **not**
performed in case of immutable containers, such as strings, numbers and
tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# ior() and iand()

 

# importing operator to handle operator operations

import operator

 

# using ior() to or, and assign value

x = operator.ior(10,5);

 

# printing the modified value

print ("The value after bitwise or, and assigning : ",end="")

print (x)

 

# using iand() to and, and assign value

x = operator.iand(5,4);

 

# printing the modified value

print ("The value after bitwise and, and assigning : ",end="")

print (x)  
  
---  
  
 __

 __

Output:

    
    
    The value after bitwise or, and assigning : 15
    The value after bitwise and, and assigning : 4
    

**5\. ilshift()** :- This function is used to **assign and bitwise leftshift
the current value by second argument**. This operation does “ **a <<=b **”
operation. Assigning is **not** performed in case of immutable containers,
such as strings, numbers and tuples.

 **6\. irshift()** :- This function is used to **assign and bitwise rightshift
the current value by second argument**. This operation does “ **a >>=b **”
operation. Assigning is **not** performed in case of immutable containers,
such as strings, numbers and tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# ilshift() and irshift()

 

# importing operator to handle operator operations

import operator

 

# using ilshift() to bitwise left shift and assign value

x = operator.ilshift(8,2);

 

# printing the modified value

print ("The value after bitwise left shift and assigning :
",end="")

print (x)

 

# using irshift() to bitwise right shift and assign value

x = operator.irshift(8,2);

 

# printing the modified value

print ("The value after bitwise right shift and assigning :
",end="")

print (x)  
  
---  
  
 __

 __

Output:

    
    
    The value after bitwise left shift and assigning : 32
    The value after bitwise right shift and assigning : 2
    

Next Article – Inplace vs Standard Operators

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

