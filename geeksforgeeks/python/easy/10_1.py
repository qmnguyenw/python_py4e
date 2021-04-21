Internal Working of the len() Function in Python



The len() function in Python has a very peculiar characteristic that one had
often wondered about. It takes absolutely no time, and equal time, in
calculating the lengths of iterable data structures(string, array, tuple,
etc.), irrespective of the size or type of data. This obviously implies O(1)
time complexity. **But have you wondered How?**

Python follows the idea that keeping the length as an attribute is cheap and
easy to maintain. len() is actually a function that calls the method
‘__len__()’. This method is defined in the predefined classes of iterable data
structures. This method actually acts as a counter, that is automatically
incremented as the data is defined and stored. Thus when you call the len()
function, you do not give the interpreter the command to find the length by
traversing, but rather you ask the interpreter to print a value that is
already stored. Hence, len() function in Python runs in O(1) complexity.

Thus it can also be defined as:

 __

 __  
 __

 __

 __  
 __  
 __

def length(ar):

 

 # calling the internally 

 # defined __len__() method

 return ar.__len__() 

 

# Driver code

a = [1, 2, 3, 4]

print(length(a))  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Note:** This might seem very beneficial, but remember that it puts a
remarkable burden on the interpreter during the data definition phase. This is
one of the many reasons why Python is slower during competitive programming,
especially with big inputs.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

