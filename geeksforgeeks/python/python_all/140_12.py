Python | Increment 1’s in list based on pattern



Given a list of binary numbers 0 and 1, Write a Python program to transform
the list in such a way that whenever 1 appears after the occurrence of a
sequence of 0’s, increment it by n+1, where ‘n’ is the last increment.

 **Examples:**

    
    
    **Input :** [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
    **Output :** [0, 1, 0, 0, 2, 2, 0, 0, 0, 3, 3, 3]
    
    **Input :** [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    **Output :** [1, 0, 2, 0, 0, 0, 3, 3, 0, 0, 4, 4, 4, 0, 5, 0, 6]
    

  
**Approach #1 :** Naive Approach

This is a naive approach to the given problem. It uses two variable ‘previous’
and ‘grp’ to store previously incremented number and to store the number of
1’s in a group. Now, using a for loop, increment 1’s accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to increment 1's in

# list based on pattern 

 

def transform(lst):

 

 previous = 0

 grp = 0

 for elem in lst:

 if elem and not previous:

 grp += 1

 previous = elem

 yield (grp if elem else 0)

 

# Driver code

lst = [0, 1, 0, 0, 1, 1, 0, 0, 0,
1, 1, 1]

x = (transform(lst))

res = []

for i in range(0, len(lst)):

 res.append(next(x))

print(res)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [0, 1, 0, 0, 2, 2, 0, 0, 0, 3, 3, 3]
    

