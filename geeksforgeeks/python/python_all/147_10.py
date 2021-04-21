Python | Get first index values in tuple of strings



Yet another peculiar problem which might not be common, but can occur in
python programming while playing with tuples. Since tuples are immutable, they
are difficult to manipulate and hence knowledge of possible variation
solutions always helps. This articles solves problem of extracting only the
first index element of each string in tuple. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Using list comprehension**

Almost every problem can be solved using list comprehension as a shorthand to
naive approach and this problem isn’t an exception. In this, we just iterate
through each list picking just the 0th index element to build the resultant
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get first index values in tuple of strings

# using list comprehension

 

# initializing tuple

test_tuple = ('GfG', 'for', 'Geeks')

 

# printing original tuple 

print("The original tuple : " + str(test_tuple))

 

# using list comprehsion

# Get first index values in tuple of strings

res = list(sub[0] for sub in test_tuple)

 

# print result

print("The first index string character list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ('GfG', 'for', 'Geeks')
    The first index string character list : ['G', 'f', 'G']
    

  

  

**Method #2 : Usingnext() + zip()**

This particular task can also be performed using the combination of above two
in more efficient way, using the iterators to do this task. The zip function
can be used bind together the string elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get first index values in tuple of strings

# using next() + zip()

 

# initializing tuple

test_tuple = ('GfG', 'for', 'Geeks')

 

# printing original tuple 

print("The original tuple : " + str(test_tuple))

 

# using next() + zip()

# Get first index values in tuple of strings

res = list(next(zip(*test_tuple)))

 

# print result

print("The first index string character list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ('GfG', 'for', 'Geeks')
    The first index string character list : ['G', 'f', 'G']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

