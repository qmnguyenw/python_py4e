Inplace vs Standard Operators in Python



Inplace Operators – Set 1, Set 2

Normal operators do the simple assigning job. On other hand, Inplace operators
behave similar to normal operators **except** that they act in a different
manner in case of mutable and Immutable targets.

  * The **_add_** method, does simple addition, takes two arguments, returns the sum and stores it in other variable without modifying any of the argument.
  * On the other hand, **_iadd_** method also takes two arguments, but it makes **in-place change** in 1st argument passed by storing the sum in it. As object mutation is needed in this process, immutable targets such as numbers, strings and tuples, **shouldn’t have _iadd_ method**.
  *  **Normal operator’s “add()”** method, implements “ **a+b** ” and stores the result in the mentioned variable.
  *  **Inplace operator’s “iadd()”** method, implements “ **a+=b** ” if it exists (i.e in case of immutable targets, it doesn’t exist) and changes the value of passed argument. But **if not, “a+b” is implemented**.

In both the cases assignment is required to do to store the value.

 **Case 1** : **Immutable Targets.**  
In Immutable targets, such as numbers, strings and tuples. Inplace operator
behave same as normal operators, i.e only assignment takes place, no
modification is taken place in the passed arguments.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate difference between

# Inplace and Normal operators in Immutable Targets

 

# importing operator to handle operator operations

import operator

 

# Initializing values

x = 5

y = 6

a = 5

b = 6

 

# using add() to add the arguments passed 

z = operator.add(a,b)

 

# using iadd() to add the arguments passed 

p = operator.iadd(x,y)

 

# printing the modified value

print ("Value after adding using normal operator : ",end="")

print (z)

 

# printing the modified value

print ("Value after adding using Inplace operator : ",end="")

print (p)

 

# printing value of first argument

# value is unchanged

print ("Value of first argument using normal operator : ",end="")

print (a)

 

# printing value of first argument

# value is unchanged

print ("Value of first argument using Inplace operator : ",end="")

print (x)  
  
---  
  
 __

 __

Output:

    
    
    Value after adding using normal operator : 11
    Value after adding using Inplace operator : 11
    Value of first argument using normal operator : 5
    Value of first argument using Inplace operator : 5
    

**Case 2** : **Mutable Targets**  
The behaviour of Inplace operators in mutable targets, such as list and
dictionaries, is different from normal operators.The **updation and assignment
both are carried out** in case of mutable targets.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate difference between

# Inplace and Normal operators in mutable Targets

 

# importing operator to handle operator operations

import operator

 

# Initializing list

a = [1, 2, 4, 5]

 

# using add() to add the arguments passed 

z = operator.add(a,[1, 2, 3])

 

# printing the modified value

print ("Value after adding using normal operator : ",end="")

print (z)

 

# printing value of first argument

# value is unchanged

print ("Value of first argument using normal operator : ",end="")

print (a)

 

# using iadd() to add the arguments passed 

# performs a+=[1, 2, 3]

p = operator.iadd(a,[1, 2, 3])

 

# printing the modified value

print ("Value after adding using Inplace operator : ",end="")

print (p)

 

# printing value of first argument

# value is changed

print ("Value of first argument using Inplace operator : ",end="")

print (a)  
  
---  
  
 __

 __

Output:

    
    
    Value after adding using normal operator : [1, 2, 4, 5, 1, 2, 3]
    Value of first argument using normal operator : [1, 2, 4, 5]
    Value after adding using Inplace operator : [1, 2, 4, 5, 1, 2, 3]
    Value of first argument using Inplace operator : [1, 2, 4, 5, 1, 2, 3]
    

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

