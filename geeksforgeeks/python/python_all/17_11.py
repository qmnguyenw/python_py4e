Python Program to Find the Total Sum of a Nested List Using Recursion



A nested list is given. The task is to print the sum of this list using
recursion. A nested list is a list whose elements can also be a list.

**Examples :**

    
    
     **Input:** [1,2,[3]]
    **Output:** 6
    
    **Input:** [[4,5],[7,8,[20]],100]
    **Output:** 144
    
    **Input:** [[1,2,3],[4,[5,6]],7]
    **Output:** 28

 **Recursion:** In recursion, a function calls itself repeatedly. This
technique is generally used when a problem can be divided into smaller
subproblems of the same form.

 **Implementation:**

Iterate through the list and whenever we find that an element of the list is
also a list that means we have to do the same task of finding sum with this
element list (which can be nested) as well. So we have found a subproblem and,
we can call the same function to perform this task and just changing the
argument to this sublist. And when the element is not a list, then simply add
its value to the global total variable.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to find sum

# of nested list using Recursion

def sum_nestedlist( l ):

 

 # specify that global variable is

 # referred to here in this function

 total = 0

 

 for j in range(len(l)):

 

 if type(l[j]) == list :

 

 # call the same function if

 # the element is a list

 sum_nestedlist(l[j])

 else:

 

 # if it's a single element

 # and not a list, add it to total

 total += l[j] 

 

 return total

 

print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))  
  
---  
  
 __

 __

 **Output:**

    
    
    144

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

