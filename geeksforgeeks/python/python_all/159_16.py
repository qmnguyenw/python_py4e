Python | Replace list elements with its ordinal number



Given a list of lists, write a Python program to replace the values in the
inner lists with their ordinal values.

 **Examples:**

    
    
    **Input :** [[1, 2, 3], [ 4, 5, 6], [ 7, 8, 9, 10]]
    **Output :** [[0, 0, 0], [1, 1, 1], [2, 2, 2, 2]]
    
    **Input :** [['a'], [ 'd', 'e', 'b', 't'], [ 'x', 'l']]
    **Output :** [[0], [1, 1, 1, 1], [2, 2]]
    

  
**Approach #1 :** Naive Approach

This method is a one-liner Naive approach in which we make use of two for
loops using _i_ and _j_ variable and iterate through each inner list to
replace it with the _i th_ ordinal number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Replace element

# in a list with its ordinal number 

 

def replaceOrdinal(lst):

 return [[i for j in range(len(lst[i]))] 

 for i in range(len(lst))]

 

# Driver Code

lst = [[1, 2, 3], [ 4, 5, 6], [ 7, 8,
9, 10]]

print(replaceOrdinal(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[0, 0, 0], [1, 1, 1], [2, 2, 2, 2]]
    

