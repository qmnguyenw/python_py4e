What is the maximum possible value of an integer in Python ?



Consider below Python program.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate that we can store

# large numbers in Python

 

x = 10000000000000000000000000000000000000000000;

x = x + 1

print (x)  
  
---  
  
 __

 __

Output :

    
    
    10000000000000000000000000000000000000000001

 _ **In Python, value of an integer is not restricted by the number of bits
and can expand to the limit of the available memory (Sources :this and
this)**_. Thus we never need any special arrangement for storing large numbers
(Imagine doing above arithmetic in C/C++).

As a side note, in Python 3, there is only one type “int” for all type of
integers. In Python 2.7. there are two separate types “int” (which is 32 bit)
and “long int” that is same as “int” of Python 3.x, i.e., can store
arbitrarily large numbers.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to show that there are two types in

# Python 2.7 : int and long int

# And in Python 3 there is only one type : int

 

x = 10

print(type(x))

 

x = 10000000000000000000000000000000000000000000

print(type(x))  
  
---  
  
 __

 __

 **Output in Python 2.7 :**

  

  

    
    
    <type 'int'>
    <type 'long'>

 **Output in Python 3 :**

    
    
    <type 'int'>
    <type 'int'>

We may want to try more interesting programs like below :

 __

 __  
 __

 __

 __  
 __  
 __

# Printing 100 raise to power 100

print(100**100)  
  
---  
  
 __

 __

This article is contributed by **Abhay Rathi**. Please write comments if you
find anything incorrect, or you want to share more information about the topic
discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

