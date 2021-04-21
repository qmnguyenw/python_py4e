Inplace Operators in Python | Set 1 (iadd(), isub(), iconcat()…)



Python in its definition provides methods to perform inplace operations, i.e
**doing assignment and computation in a single statement** using “
**operator** ” module. For example,

    
    
    x += y is equivalent to x = operator.iadd(x, y) 

**Some Important Inplace operations** :

 **1\. iadd()** :- This function is used to **assign and add the current
value**. This operation does “ **a+=b** ” operation. Assigning is **not**
performed in case of immutable containers, such as strings, numbers and
tuples.

 **2\. iconcat()** :- This function is used to **concat** one string at end of
second.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# iadd() and iconcat()

 

# importing operator to handle operator operations

import operator

 

# using iadd() to add and assign value

x = operator.iadd(2, 3);

 

# printing the modified value

print ("The value after adding and assigning : ", end="")

print (x)

 

# initializing values

y = "geeks"

 

z = "forgeeks"

 

# using iconcat() to concat the sequences

y = operator.iconcat(y, z)

 

# using iconcat() to concat sequences 

print ("The string after concatenation is : ", end="")

print (y)  
  
---  
  
 __

 __

Output:

  

  

    
    
    The value after adding and assigning : 5
    The string after concatenation is : geeksforgeeks
    

**3\. isub()** :- This function is used to **assign and subtract the current
value**. This operation does “ **a-=b** ” operation. Assigning is **not**
performed in case of immutable containers, such as strings, numbers and
tuples.

 **4\. imul()** :- This function is used to **assign and multiply the current
value**. This operation does “ **a*=b** ” operation. Assigning is **not**
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

# isub() and imul()

 

# importing operator to handle operator operations

import operator

 

# using isub() to subtract and assign value

x = operator.isub(2, 3);

 

# printing the modified value

print ("The value after subtracting and assigning : ", end="")

print (x)

 

# using imul() to multiply and assign value

x = operator.imul(2, 3);

 

# printing the modified value

print ("The value after multiplying and assigning : ", end="")

print (x)  
  
---  
  
 __

 __

Output:

    
    
    The value after subtracting and assigning : -1
    The value after multiplying and assigning : 6
    

**5\. itruediv()** :- This function is used to **assign and divide the current
value**. This operation does “ **a/=b** ” operation. Assigning is **not**
performed in case of immutable containers, such as strings, numbers and
tuples.

 **6\. imod()** :- This function is used to **assign and return remainder**.
This operation does “ **a%=b** ” operation. Assigning is **not** performed in
case of immutable containers, such as strings, numbers and tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# itruediv() and imod()

 

# importing operator to handle operator operations

import operator

 

# using itruediv() to divide and assign value

x = operator.itruediv(10, 5);

 

# printing the modified value

print ("The value after dividing and assigning : ", end="")

print (x)

 

# using imod() to modulus and assign value

x = operator.imod(10, 6);

 

# printing the modified value

print ("The value after modulus and assigning : ", end="")

print (x)  
  
---  
  
 __

 __

Output:

    
    
    The value after dividing and assigning : 2.0
    The value after modulus and assigning : 4
    

Next Articles

  * Inplace Operators in Python | Set 2
  * Inplace vs Standard Operators

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

