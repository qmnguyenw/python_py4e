Python – Convert Tuple to Tuple Pair



Sometimes, while working with Python Tuple records, we can have a problem in
which we need to convert Single tuple with 3 elements to pair of dual tuple.
This is quite a peculiar problem but can have problem in day-day programming
and competitive programming. Let’s discuss certain ways in which this task can
be performed.

>  **Input** : test_tuple = (‘A’, ‘B’, ‘C’)  
>  **Output** : [(‘A’, ‘B’), (‘A’, ‘C’)]
>
>  **Input** : test_tuple = (‘X’, ‘Y’, ‘Z’)  
>  **Output** : [(‘X’, ‘Y’), (‘X’, ‘Z’)]

 **Method #1 : Usingproduct() + next()**  
The combination of above functions can be used to solve this problem. In this,
we make pairs using product, the selection of pairing with next element is
done using nex().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple to Tuple Pair

# Using product() + next()

from itertools import product

 

# initializing tuple

test_tuple = ('G', 'F', 'G')

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Convert Tuple to Tuple Pair

# Using product() + next()

test_tuple = iter(test_tuple)

res = list(product(next(test_tuple), test_tuple))

 

# printing result 

print("The paired records : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : ('G', 'F', 'G')
    The paired records : [('G', 'F'), ('G', 'G')]
    

