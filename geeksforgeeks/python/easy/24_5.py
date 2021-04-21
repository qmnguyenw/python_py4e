filter() in python



The filter() method filters the given sequence with the help of a function
that tests each element in the sequence to be true or not.

 **syntax:**

    
    
    filter(function, sequence)
    **Parameters:**
    function: function that tests if each element of a 
    sequence true or not.
    sequence: sequence which needs to be filtered, it can 
    be sets, lists, tuples, or containers of any iterators.
    **Returns:**
    returns an iterator that is already filtered.
    

__

__  
__

__

__  
__  
__

# function that filters vowels

def fun(variable):

 letters = ['a', 'e', 'i', 'o', 'u']

 if (variable in letters):

 return True

 else:

 return False

 

 

# sequence

sequence = ['g', 'e', 'e', 'j', 'k', 's',
'p', 'r']

 

# using filter function

filtered = filter(fun, sequence)

 

print('The filtered letters are:')

for s in filtered:

 print(s)  
  
---  
  
 __

 __

 **Output:**

    
    
    The filtered letters are:
    e
    e
    

**Application:**  
It is normally used with Lambda functions to separate list, tuple, or sets.

 __

 __  
 __

 __

 __  
 __  
 __

# a list contains both even and odd numbers.

seq = [0, 1, 2, 3, 5, 8, 13]

 

# result contains odd numbers of the list

result = filter(lambda x: x % 2 != 0, seq)

print(list(result))

 

# result contains even numbers of the list

result = filter(lambda x: x % 2 == 0, seq)

print(list(result))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [1, 3, 5, 13]
    [0, 2, 8]
    

Please refer Python Lambda functions for more details.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

