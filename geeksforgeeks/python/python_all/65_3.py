Python – Edit objects inside tuple



Sometimes, while working with tuples, being immutable, can offer a lot of
confusion regarding its working. One of the questions that can pop from mind
is, that Are objects inside tuples mutable?. The answer to this is **Yes**.
Let’s discuss certain ways in which this can be achieved.

 **Method #1 : Using Access methods**  
This is one of the way in which edit inside objects of tuples can be
performed. This occurs similar to any other container and inplace using list
access method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Edit objects inside tuple

# Using Access Methods

 

# initializing tuple

test_tuple = (1, [5, 6, 4], 9, 10)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Edit objects inside tuple

# Using Access Methods

test_tuple[1][2] = 14

 

# printing result 

print("The modified tuple : " + str(test_tuple))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple : (1, [5, 6, 4], 9, 10)
    The modified tuple : (1, [5, 6, 14], 9, 10)
    

**Method #2 : Usingpop() + index()**  
The combination of above functionalities can also be used to solve this
problem. In this, we perform task of removak using pop() and add element at
particular index using index().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Edit objects inside tuple

# Using pop() + index()

 

# initializing tuple

test_tuple = (1, [5, 6, 4], 9, 10)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Edit objects inside tuple

# Using pop() + index()

test_tuple[1].pop(2)

test_tuple[1].insert(2, 14) 

 

# printing result 

print("The modified tuple : " + str(test_tuple))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple : (1, [5, 6, 4], 9, 10)
    The modified tuple : (1, [5, 6, 14], 9, 10)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

