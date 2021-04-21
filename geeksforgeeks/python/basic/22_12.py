join() function in Python



  
The join() method is a string method and returns a string in which the
elements of sequence have been joined by str separator.

 **Syntax:**

    
    
    _string_name_.join(iterable) 
    
    **string_name** : It is the name of string in which
                 joined elements of iterable will be
                 stored.
    

**Parameters:** The join() method takes iterable – objects capable of
returning its members one at a time. Some examples are **List, Tuple, String,
Dictionary and Set**

 **Return Value:** The join() method returns a string concatenated with the
elements of _iterable_.

 **Type Error** : If the iterable contains any non-string values, it raises a
TypeError exception.

  

  

Below program illustrates the working of join() method:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# use of join function to join list

# elements with a character.

 

list1 = ['1','2','3','4'] 

 

s = "-"

 

# joins elements of list1 by '-'

# and stores in sting s

s = s.join(list1)

 

# join use to join a list of

# strings to a separator s

print(s)  
  
---  
  
 __

 __

Output:

    
    
    1-2-3-4
    

**Joining with empty string.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# use of join function to join list

# elements without any separator.

 

# Joining with empty separator

list1 = ['g','e','e','k', 's'] 

print("".join(list1))  
  
---  
  
 __

 __

Output:

    
    
    geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

