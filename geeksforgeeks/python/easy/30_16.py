Operator Functions in Python | Set 2



Operator Functions in Python | Set 1

More functions are discussed in this article.

 **1\. setitem(ob, pos, val)** :- This function is used to **assign** the
value at a **particular position** in the container.  
Operation – **ob[pos] = val**

 **2\. delitem(ob, pos)** :- This function is used to **delete** the value at
a **particular position** in the container.  
Operation – **del ob[pos]**

 **3\. getitem(ob, pos)** :- This function is used to **access** the value at
a **particular position** in the container.  
Operation – **ob[pos]**  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# setitem(), delitem() and getitem()

 

# importing operator module 

import operator

 

# Initializing list

li = [1, 5, 6, 7, 8]

 

# printing original list 

print ("The original list is : ",end="")

for i in range(0,len(li)):

 print (li[i],end=" ")

 

print ("\r")

 

# using setitem() to assign 3 at 4th position

operator.setitem(li,3,3)

 

# printing modified list after setitem()

print ("The modified list after setitem() is : ",end="")

for i in range(0,len(li)):

 print (li[i],end=" ")

 

print ("\r")

 

# using delitem() to delete value at 2nd index

operator.delitem(li,1)

 

# printing modified list after delitem()

print ("The modified list after delitem() is : ",end="")

for i in range(0,len(li)):

 print (li[i],end=" ")

 

print ("\r")

 

# using getitem() to access 4th element

print ("The 4th element of list is : ",end="")

print (operator.getitem(li,3))  
  
---  
  
 __

 __

Output:  

    
    
    The original list is : 1 5 6 7 8 
    The modified list after setitem() is : 1 5 6 3 8 
    The modified list after delitem() is : 1 6 3 8 
    The 4th element of list is : 8

 **4\. setitem(ob, slice(a,b), vals)** :- This function is used to **set the
values in a particular range** in the container.  
Operation – **obj[a:b] = vals**

 **5\. delitem(ob, slice(a,b))** :- This function is used to **delete the
values from a particular range** in the container.  
Operation – **del obj[a:b]**

 **6\. getitem(ob, slice(a,b))** :- This function is used to **access the
values in a particular range** in the container.  
Operation – **obj[a:b]**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# setitem(), delitem() and getitem()

 

# importing operator module 

import operator

 

# Initializing list

li = [1, 5, 6, 7, 8]

 

# printing original list 

print ("The original list is : ",end="")

for i in range(0,len(li)):

 print (li[i],end=" ")

 

print ("\r")

 

# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index

operator.setitem(li,slice(1,4),[2,3,4])

 

# printing modified list after setitem()

print ("The modified list after setitem() is : ",end="")

for i in range(0,len(li)):

 print (li[i],end=" ")

 

print ("\r")

 

# using delitem() to delete value at 3rd and 4th index

operator.delitem(li,slice(2,4))

 

# printing modified list after delitem()

print ("The modified list after delitem() is : ",end="")

for i in range(0,len(li)):

 print (li[i],end=" ")

 

print ("\r")

 

# using getitem() to access 1st and 2nd element

print ("The 1st and 2nd element of list is : ",end="")

print (operator.getitem(li,slice(0,2)))  
  
---  
  
 __

 __

Output:  

    
    
    The original list is : 1 5 6 7 8 
    The modified list after setitem() is : 1 2 3 4 8 
    The modified list after delitem() is : 1 2 8 
    The 1st and 2nd element of list is : [1, 2]

  
**7\. concat(ob1,obj2)** :- This function is used to **concatenate** two
containers.  
Operation – **obj1 + obj2**

 **8\. contains(ob1,obj2)** :- This function is used to **check if obj2 in
present in obj1**.  
Operation – **obj2 in obj1**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# concat() and contains()

 

# importing operator module 

import operator

 

# Initializing string 1

s1 = "geeksfor"

 

# Initializing string 2

s2 = "geeks"

 

# using concat() to concatenate two strings

print ("The concatenated string is : ",end="")

print (operator.concat(s1,s2))

 

# using contains() to check if s1 contains s2

if (operator.contains(s1,s2)):

 print ("geeksfor contains geeks")

else : print ("geeksfor does not contain geeks")  
  
---  
  
 __

 __

Output:  

  

  

    
    
    The concatenated string is : geeksforgeeks
    geeksfor contains geeks

**9\. and_(a,b)** :- This function is used to compute **bitwise and** of the
mentioned arguments.  
Operation – **a & b**

 **10\. or_(a,b)** :- This function is used to compute **bitwise or** of the
mentioned arguments.  
Operation – **a | b**

 **11\. xor(a,b)** :- This function is used to compute **bitwise xor** of the
mentioned arguments.  
Operation – **a ^ b**

 **12\. invert(a)** :- This function is used to compute **bitwise inversion**
of the mentioned argument.  
Operation – **~ a**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# and_(), or_(), xor(), invert()

 

# importing operator module 

import operator

 

# Initializing a and b

 

a = 1

 

b = 0

 

# using and_() to display bitwise and operation

print ("The bitwise and of a and b is : ",end="")

print (operator.and_(a,b))

 

# using or_() to display bitwise or operation

print ("The bitwise or of a and b is : ",end="")

print (operator.or_(a,b))

 

# using xor() to display bitwise exclusive or operation

print ("The bitwise xor of a and b is : ",end="")

print (operator.xor(a,b))

 

# using invert() to invert value of a

operator.invert(a)

 

# printing modified value

print ("The inverted value of a is : ",end="")

print (operator.invert(a))  
  
---  
  
 __

 __

 **Output:**  

    
    
    The bitwise and of a and b is : 0
    The bitwise or of a and b is : 1
    The bitwise xor of a and b is : 1
    The inverted value of a is : -2

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

