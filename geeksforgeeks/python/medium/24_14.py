Python | Sort Tuples in Increasing Order by any key



Given a tuple, sort the list of tuples in increasing order by any key in
tuple.

 **Examples:**

    
    
    Input : tuple = [(2, 5), (1, 2), (4, 4), (2, 3)] 
                m = 0
    Output : [(1, 2), (2, 3), (2, 5), (4, 4)]
    Explanation: Sorted using the 0th index key.
    
    Input :  [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
             m = 2
    Output : Sorted: [(23, 45, 20), (89, 40, 23), (25, 44, 39)] 
    Explanation: Sorted using the 2nd index key
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Given tuples, we need to sort them according to any given key. This can be
done using sorted() function where we sort them using **key=last** and store
last as the key index according to which we have to sort the given tuples.

 _Below is the Python implementation of the above approach:_

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort a list of tuples

# according to given key.

 

# get the last key.

def last(n):

 return n[m] 

 

# function to sort the tuple 

def sort(tuples):

 

 # We pass used defined function last

 # as a parameter. 

 return sorted(tuples, key = last)

 

# driver code 

a = [(23, 45, 20), (25, 44, 39), (89, 40,
23)]

m = 2

print("Sorted:"),

print(sort(a))  
  
---  
  
 __

 __

Output:

    
    
    Sorted: [(23, 45, 20), (89, 40, 23), (25, 44, 39)] 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

