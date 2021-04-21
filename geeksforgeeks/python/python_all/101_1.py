Python | Rear elements from Tuple Strings



Yet another peculiar problem which might not be common, but can occur in
python programming while playing with tuples. Since tuples are immutable, they
are difficult to manipulate and hence knowledge of possible variation
solutions always helps. This articles solves problem of extracting only the
rear index element of each string in tuple. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Using list comprehension**  
Almost every problem can be solved using list comprehension as a shorthand to
naive approach and this problem isn’t an exception. In this, we just iterate
through each list picking just the n -1th index element to build the resultant
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Rear elements from Tuple Strings

# using list comprehension

 

# initializing tuple

test_tuple = ('GfG', 'for', 'Geeks')

 

# printing original tuple 

print("The original tuple : " + str(test_tuple))

 

# using list comprehsion

# Rear elements from Tuple Strings

res = list(sub[len(sub) - 1] for sub in test_tuple)

 

# print result

print("The rear index string character list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ('GfG', 'for', 'Geeks')
    The rear index string character list : ['G', 'r', 's']
    

**Method #2 : Using loop**  
This task can also be performed using brute force manner. In this, we just
iterate the each string element and extract the rear element when the index
reaches size – 1th element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Rear elements from Tuple Strings

# using list comprehension

 

# initializing tuple

test_tuple = ('GfG', 'for', 'Geeks')

 

# printing original tuple 

print("The original tuple : " + str(test_tuple))

 

# using list comprehsion

# Rear elements from Tuple Strings

res = []

for sub in test_tuple :

 N = len(sub) - 1

 res.append(sub[N])

 

# print result

print("The rear index string character list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ('GfG', 'for', 'Geeks')
    The rear index string character list : ['G', 'r', 's']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

