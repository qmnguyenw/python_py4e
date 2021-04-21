Access front and rear element of Python tuple



Sometimes, while working with records, we can have a problem in which we need
to access the initial and last data of a particular record. This kind of
problem can have application in many domains. Let’s discuss some ways in which
this problem can be solved.

 **Method #1 : Using Access Brackets**  
We can perform the possible get of front and rear element in tuple using the
access brackets in similar way in which elements can be accessed in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accessing front and rear element of tuple

# using access brackets

 

# initialize tuple

test_tup = (10, 4, 5, 6, 7)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Accessing front and rear element of tuple

# using access brackets

res = (test_tup[0], test_tup[-1])

 

# printing result

print("The front and rear element of tuple are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 7)
    The front and rear element of tuple are : (10, 7)
    

**Method #2 : Usingitemegetter()**  
This is yet another way in which this task can be performed. In this, we
access the elements using inbuilt function of itemgetter().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accessing front and rear element of tuple

# using itemgetter()

from operator import itemgetter

 

# initialize tuple

test_tup = (10, 4, 5, 6, 7)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Accessing front and rear element of tuple

# using itemgetter()

res = itemgetter(0, -1)(test_tup)

 

# printing result

print("The front and rear element of tuple are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 7)
    The front and rear element of tuple are : (10, 7)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

