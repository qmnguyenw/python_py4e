Random.Choices() method in Python



The **choices()** method returns multiple random elements from the list with
replacement. You can weigh the possibility of each result with the weights
parameter or the cum_weights parameter. The elements can be a string, a
range, a list, a tuple or any other kind of sequence.

>  **Syntax :** random.choices(sequence, weights=None, cum_weights=None, k=1)
>
>  **Parameters :**  
>  1\. **sequence** is a mandatory parameter that can be a list, tuple, or
> string.  
> 2\. **weights** is an optional parameter which is used to weigh the
> possibility for each value.  
> 3\. **cum_weights** is an optional parameter which is used to weigh the
> possibility for each value but in this the possibility is accumulated  
> 4\. **k** is an optional parameter that is used to define the length of the
> returned list.

 **Note:** This method is different from random.choice().

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

mylist = ["geeks", "for", "python"]

 

print(random.choices(mylist, weights = [10, 1, 1], k =
5))  
  
---  
  
 __

 __

 **Note:** Every time output will be different as the system returns random
elements.  
 **Output:**

    
    
    ['geeks', 'geeks', 'geeks', 'for', 'for']
    

**Practical application:** Print a random list with 6 items.

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

mylist = ["apple", "banana", "mango"]

 

print(random.choices(mylist, weights = [10, 1, 1], k =
6))  
  
---  
  
 __

 __

 **Note:** The output changes every time as choices() function is used.  
 **Output:**

    
    
    ['apple', 'banana', 'apple', 'apple', 'apple', 'banana']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

