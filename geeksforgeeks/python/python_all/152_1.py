Python | Print diagonals of 2D list



Given a 2D list (with equal length of sublists), write a Python program to
print both the diagonals of the given 2D list.

 **Examples:**

    
    
    **Input :** [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    **Output :** Diagnol 1 - [1, 5, 9]
             Diagnol 2 - [3, 5, 7]
    
    **Input :** [['a', 'b'], ['c', 'd']]
    **Output :** Diagnol 1 - ['a', 'd']
             Diagnol 2 - ['b', 'c']
    
    

**Approach #1 :** Using Python xrange()

We can use one-liner list comprehension along with xrange() function.
_xrange()_ is used to iterate a certain number of times in for loops. Thus, we
print the element at [i][i] position in every iteration of loop. [Works in
Python2]

 __

 __  
 __

 __

 __  
 __  
 __

# Python2 program to print diagonals in 2D list

 

def printDiagnol(lst):

 # To print Primary Diagnol

 print('Diagnol 1 -'),

 print([lst[i][i] for i in xrange(len(lst))])

 

 # To print Secondry Diagnol

 print('Diagnol 2 -'),

 print([lst[i][len(lst)-1-i] for i in
xrange(len(lst))])

 

 

# Driver code

lst = [[1, 2, 3],

 [4, 5, 6], 

 [7, 8, 9]]

 

printDiagnol(lst)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Diagnol 1 - [1, 5, 9]
    Diagnol 2 - [3, 5, 7]
    

