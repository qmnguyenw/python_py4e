Python | Insert value after each k letters in given list of string



Given a list of string, write a Python program to Insert some letter after
each k letters in given list of strings.

As we know inserting element in a list is quite common, but sometimes we need
to operate on list of strings by considering each letter and insert some
repeated elements some fixed frequency. Let’s see how to achieve this task
using Python.

 **Method #1:** Using enumerate() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to insert value after

# each k letters in given list of string

list1 = ['p', 'y', 't', 'h', 'o', 'n'] 

 

# printing original list 

print ("Original list : " + str(list1)) 

 

# initializing k 

k = 'G'

 

# initializing N 

N = 2

 

# using join() + enumerate() 

# inserting K after every Nth number 

output = list(''.join(i + k * (N % 2 == 1) 

 for N, i in enumerate(list1))) 

 

# printing result 

print ("The lists after insertion : " + str(output))   
  
---  
  
__

__

**Output:**

    
    
    Original list : ['p', 'y', 't', 'h', 'o', 'n']
    The lists after insertion : ['p', 'y', 'G', 't', 'h', 'G', 'o', 'n', 'G']
    

  

  

**Method #2:** Using itertools

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to insert value after

# each k letters in given list of string

from itertools import chain 

 

list1 = ['p', 'y', 't', 'h', 'o', 'n'] 

 

# printing original list 

print ("Original list : " + str(list1)) 

 

# initializing k 

k = 'x'

 

# initializing N 

N = 3

 

 

# inserting K after every Nth number 

output = list(chain(*[list1[i : i + N] + [k] 

 if len(list1[i : i + N]) == N else list1[i : i + N]


 for i in range(0, len(list1), N)])) 

 

# printing result 

print ("The lists after insertion : " + str(output))   
  
---  
  
__

__

**Output:**

    
    
    Original list : ['p', 'y', 't', 'h', 'o', 'n']
    The lists after insertion : ['p', 'y', 't', 'x', 'h', 'o', 'n', 'x']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

