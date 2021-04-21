Python | Interleaving two strings



Sometimes, while working with strings, we have the task of combining two
strings, i.e interleaving them according to utility. This type of utility is
mostly useful while writing codes for games. Let’s discuss certain ways in
which this can be performed.

 **Method #1 : Usingjoin() + zip()**  
This task can be performed using the above functions. In this join function
performs the task of joining of each element pair two strings at an index and
zip performs the task of interleaving character at each string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Interleaving two strings

# using join() + zip()

 

# initializing strings 

test_string1 = 'geeksforgeeks'

test_string2 = 'computerfreak'

 

# printing original strings 

print("The original string 1 : " + test_string1)

print("The original string 2 : " + test_string2)

 

# using join() + zip()

# Interleaving two strings

res = "".join(i + j for i, j in zip(test_string1,
test_string2))

 

# print result

print("The Interleaved string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original string 1 : geeksforgeeks
    The original string 2 : computerfreak
    The Interleaved string : gceoemkpsuftoerrgfereekask
    

**Method #2 : Usingzip() + join() + chain.from_iterable()**  
This task can also be performed using the chain.from_iterable function. The
major advantage to use this particular function is that it offers more speed
than the above method, about 3 times faster than above method as it converts
the string to iterable.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Interleaving two strings

# using join() + zip() + chain.from_iterable()

from itertools import chain

 

# initializing strings 

test_string1 = 'geeksforgeeks'

test_string2 = 'computerfreak'

 

# printing original strings 

print("The original string 1 : " + test_string1)

print("The original string 2 : " + test_string2)

 

# using join() + zip() + chain.from_iterable()

# Interleaving two strings

res = "".join(list(chain.from_iterable(zip(test_string1,
test_string2))))

 

# print result

print("The Interleaved string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original string 1 : geeksforgeeks
    The original string 2 : computerfreak
    The Interleaved string : gceoemkpsuftoerrgfereekask
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

