Python | Ways to sort letters of string alphabetically



Given a string of letters, write a python program to sort the given string in
an alphabetical order.

 **Examples:**

    
    
    **Input :** PYTHON
    **Output :** HNOPTY
    
    **Input :** Geeks
    **Output :** eeGks
    

#### When string is in same case –

 **Method #1 :** Using sorted() with join()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to sort letters

# of string alphabetically

 

def sortString(str):

 return ''.join(sorted(str))

 

# Driver code

str = 'PYTHON'

print(sortString(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    HNOPTY
    

  
**Method #2 :** Using sorted() with accumulate()

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to sort letters

# of string alphabetically

from itertools import accumulate

 

def sortString(str):

 return tuple(accumulate(sorted(str)))[-1]

 

# Driver code

str = 'PYTHON'

print(sortString(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    HNOPTY
    

  
**Method #3 :** Using sorted() with reduce()

Another alternative is to use _reduce()_ method. It applies a join function on
the sorted list using ‘+’ operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to sort letters

# of string alphabetically

from functools import reduce

 

def sortString(str):

 return reduce(lambda a, b : a + b, sorted(str))

 

# Driver code

str = 'PYTHON'

print(sortString(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    HNOPTY
    

#### When string is in different cases –

Using sorted() with join()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to sort letters

# of string alphabetically

from itertools import accumulate

 

def sortString(str):

 return "".join(sorted(str, key = lambda x:x.lower()))

 

# Driver code

str = 'Geeks'

print(sortString(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    eeGks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

