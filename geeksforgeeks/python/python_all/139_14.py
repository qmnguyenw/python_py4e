Python | Column wise sum of nested list



Given a nested list (where sublists are of equal length), write a Python
program to find the column-wise sum of the given list and return it in a new
list.

 **Examples:**

    
    
    **Input :** [[1, 5, 3],
             [2, 7, 8],
             [4, 6, 9]]
    **Output :** [7, 18, 20]
    
    **Input :** [[20, 5],
             [2, 54],
             [45, 9], 
             [72, 3]]
    **Output :** [139, 71]
    

**Method #1 :** _zip_ using list comprehension

We can find sum of each column of the given nested list using zip function
of python enclosing it within list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Column wise sum of nested list

 

def column_sum(lst):

 

 return [sum(i) for i in zip(*lst)]

 

# Driver code

lst = [[1, 5, 3], [2, 7, 8], [4, 6,
9]]

print(column_sum(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [7, 18, 20]
    

