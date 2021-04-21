Python | Find missing numbers in a sorted list range



Given a range of sorted list of integers with some integers missing in
between, write a Python program to find all the missing integers.

 **Examples:**

    
    
    **Input :** [1, 2, 4, 6, 7, 9, 10]
    **Output :** [3, 5, 8]
    
    **Input :** [5, 6, 10, 11, 13]
    **Output :** [7, 8, 9, 12]
    

  
**Method #1 :** List comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find missing

# integers in list

 

def find_missing(lst):

 return [x for x in range(lst[0], lst[-1]+1) 

 if x not in lst]

 

# Driver code

lst = [1, 2, 4, 6, 7, 9, 10]

print(find_missing(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 5, 8]
    

  
**Method #2 :** List comprehension using _zip()_

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find missing

# integers in list

 

def find_missing(lst):

 return [i for x, y in zip(lst, lst[1:]) 

 for i in range(x + 1, y) if y - x > 1]

 

# Driver code

lst = [1, 2, 4, 6, 7, 9, 10]

print(find_missing(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 5, 8]
    

  
**Method #3 :** Using _set_

The use of Python set is an efficient and tricky way to find the missing
numbers in the list. We convert the list to set and simply output the
difference between this set and a set that contains integers ranging from
_min(lst)_ and _max(lst)_.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find missing

# integers in list

 

def find_missing(lst):

 return sorted(set(range(lst[0], lst[-1])) -
set(lst))

 

# Driver code

lst = [1, 2, 4, 6, 7, 9, 10]

print(find_missing(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 5, 8]
    

  
**Method #4 :** Using _difference()_

This is a similar approach to the previous one with a slight difference that
instead of using ‘-‘ operator to find the difference between both the sets, we
can use Python _difference()_ method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find missing

# integers in list

 

def find_missing(lst):

 start = lst[0]

 end = lst[-1]

 return sorted(set(range(start, end +
1)).difference(lst))

 

# Driver code

lst = [1, 2, 4, 6, 7, 9, 10]

print(find_missing(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 5, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

