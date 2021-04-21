Python | Shrink given list for repeating elements



Given a list of repetitive elements, Write a python program to shrink the
repetition of the elements and convert the repetition into a tuple element of
the list containing the repeated element and number of times it has repeated,
Thus, converting the given list into a list of tuples.

 **Examples:**

    
    
    **Input :** [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    **Output :** [(1, 3), (2, 1), (3, 3), (4, 4)]
    
    **Input :** ['alice', 'alice', 'bob']
    **Output :** [('alice', 2), ('bob', 1)]
    

**Approach #1 :** Brute force  
This is a Naive approach in order to shrink the list. It takes another list
say, ‘tup_list’. Initialize index to 0 and use a loop to check how many times
each unique element of the list is repeated. Once found the element and its
repeat count, append it to the list in form of a tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Shrink list

# for repeating elements

 

def shrinkList(lst):

 tup_list = []

 i, index = 0, 0

 while(index < len(lst)):

 element_count = 0

 while(i < len(lst) and lst[i] == lst[index]):

 element_count += 1

 i += 1

 tup_list.append((lst[index], element_count))

 index += element_count

 

 return tup_list

 

# Driver Code

lst = [1, 1, 1, 2, 2, 3, 3, 4]

print(shrinkList(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 3), (2, 2), (3, 2), (4, 1)]
    

  
**Approach #2 :** Alternate Brute force  
This is another brute force approach which uses for loop to traverse the list.
It uses a variable ‘prev_element’ to store the previous element. First, it
checks if this is the first unique element or not, if yes, It increments the
counter and stores the element to prev_element. If the element is repeated,
just increment the counter. If all these cases are not true then just append
the prev_element and count as tuple to tup_list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Shrink list

# for repeating elements

 

def shrinkList(lst):

 prev_element = None

 count = 0

 tup_list = []

 

 for ele in lst:

 if (prev_element == ele): 

 count += 1

 

 elif (prev_element is None):

 count += 1

 prev_element = ele

 

 else:

 tup_list.append((prev_element, count))

 count = 1

 prev_element = ele

 

 tup_list.append((prev_element, count))

 return tup_list

 

# Driver Code

lst = [1, 1, 1, 2, 2, 3, 3, 4]

print(shrinkList(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 3), (2, 2), (3, 2), (4, 1)]
    

  
**Approach #3 :** Using Itertools.groupby()  
This is a more pythonic approach to solve the given problem. The
itertools.groupby() make an iterator that returns consecutive keys and
groups from the iterable. It groups similar elements and returns the elements
and their count as list of tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Shrink list

# for repeating elements

from itertools import groupby

 

def shrinkList(lst):

 return ([(element, len(list(i)))

 for element, i in groupby(lst)])

 

# Driver Code

lst = [1, 1, 1, 2, 2, 3, 3, 4]

print(shrinkList(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 3), (2, 2), (3, 2), (4, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

