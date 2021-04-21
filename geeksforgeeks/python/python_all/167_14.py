Python | Check if all elements in a list are identical



Given a list, write a Python program to check if all the elements in that list
are identical.

 **Examples:**

    
    
    **Input :** ['a', 'b', 'c']
    **Output :** False
    
    **Input :** [1, 1, 1, 1]
    **Output :** True
    

**Approach #1 :** Using loop  
Start a for loop and check if first element is identical to all other elements
in the list. This approach takes O(n) time complexity.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to check if

# all elements in a list are identical

def check(list):

 return all(i == list[0] for i in list)

 

# Driver code

print(check(['a', 'b', 'c']))

print(check([1, 1, 1]))  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    True
    

  
**Approach #2 :** Using Set  
Converting given list into set removes all duplicate elements, If the
resultant set size is less than or equal to 1 then the list contains all
identical elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to check if

# all elements in a list are identical

def check(list):

 return len(set(list)) <= 1

 

# Driver code

print(check(['a', 'b', 'c']))

print(check([1, 1, 1]))  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    True
    

  
**Approach #3 :** Using count()  
By counting the number of times the first element occurs in the list, we can
check if the count is equal to the size of list or not. In simple words, check
if the first element is repeated throughout the list or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to check if

# all elements in a list are identical

def check(list):

 return list.count(list[0]) == len(list)

 

# Driver code

print(check(['a', 'b', 'c']))

print(check([1, 1, 1]))  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    True
    

  
**Approach #4 :** Alternative method  
Another method is to take the first element and multiply it with the length of
given list to form a new list, So that the new list contains identical
elements to first elements of given list size, and then compare it with the
given list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to check if

# all elements in a list are identical

def check(x):

 return x and [x[0]]*len(x) == x

 

# Driver code

print(check(['a', 'b', 'c']))

print(check([1, 1, 1]))  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    True
    

  
**Approach #5 :** Using extended slices  
Python slice notation is used to retrieve a subset of values. Thus, we compare
the start to end of the list to end to start of the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to check if

# all elements in a list are identical

def check(list):

 return list[1:] == list[:-1]

 

# Driver code

print(check(['a', 'b', 'c']))

print(check([1, 1, 1]))  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

