Python | Print all the common elements of two lists



Given two lists, print all the common element of two lists.

Examples:

    
    
    Input : list1 = [1, 2, 3, 4, 5] 
            list2 = [5, 6, 7, 8, 9]
    Output : {5}
    Explanation: The common elements of 
    both the lists are 3 and 4 
    
    Input : list1 = [1, 2, 3, 4, 5] 
            list2 = [6, 7, 8, 9]
    Output : No common elements 
    Explanation: They do not have any 
    elements in common in between them
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1:Using Set’s & property**

Convert the lists to sets and then print **set1 &set2;**. set1&set2; returns
the common elements set, where set1 is the list1 and set2 is the list2.

  

  

 _Below is the Python3 implementation of the above approach:_

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the common elements

# in two lists

def common_member(a, b):

 a_set = set(a)

 b_set = set(b)

 

 if (a_set & b_set):

 print(a_set & b_set)

 else:

 print("No common elements") 

 

 

a = [1, 2, 3, 4, 5]

b = [5, 6, 7, 8, 9]

common_member(a, b)

 

a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9]

common_member(a, b)  
  
---  
  
 __

 __

 **Output:**

    
    
    {5}
    No common elements
    

**Method 2:Using Set’s intersection property**

Convert the list to set by conversion. Use intersection function to check if
both sets have any elements in common. If they have any elements in common,
then print the intersection of both the sets.

Below is the Python3 implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find common elements in

# both sets using intersection function in

# sets

 

 

# function 

def common_member(a, b): 

 a_set = set(a)

 b_set = set(b)

 

 # check length 

 if len(a_set.intersection(b_set)) > 0:

 return(a_set.intersection(b_set)) 

 else:

 return("no common elements")

 

 

a = [1, 2, 3, 4, 5]

b = [5, 6, 7, 8, 9]

print(common_member(a, b))

 

a =[1, 2, 3, 4, 5]

b =[6, 7, 8, 9]

print(common_member(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    {5}
    No common elements
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

