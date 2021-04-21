Python | Find most common element in a 2D list



Given a 2D list (may or may not be of same length), write a Python program to
find the most common element in the given 2D list.

 **Examples:**

    
    
    **Input :** [[10, 20, 30], [20, 50, 10], [30, 50, 10]]
    **Output :** 10
    
    **Input :** [['geeks', 'wins'], ['techie', 'wins']]
    **Output :** wins
    

**Approach #1 :** Using max() function

First Pythonic approach is to use _max()_ method of Python. We first flatten
the 2D list and then simply apply max() method to find out the maximum
occurring element among all the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find most

# common element in a 2D list

 

def mostCommon(lst):

 flatList = [el for sublist in lst for el in sublist]

 return max(flatList, key = flatList.count)

 

# Driver code

lst = [[10, 20, 30], [20, 50, 10], [30,
50, 10]]

print(mostCommon(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    10
    

