Python Remove Duplicates from a List



The job is simple. We need to take a list, with duplicate elements in it and
generate another list which only contains the element without the duplicates
in them.

 **Examples:**

    
    
    Input : [2, 4, 10, 20, 5, 2, 20, 4]
    Output : [2, 4, 10, 20, 5]
    
    Input : [28, 42, 28, 16, 90, 42, 42, 28]
    Output : [28, 42, 16, 90]

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

We can use not in on list to find out the duplicate items. We create a result
list and insert only those that are not already not in.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove duplicate elements

def Remove(duplicate):

 final_list = []

 for num in duplicate:

 if num not in final_list:

 final_list.append(num)

 return final_list

 

# Driver Code

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]

print(Remove(duplicate))  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 4, 10, 20, 5]

 **Easy Implementation:**

  

  

A quick way to do the above using set data structure from the python standard
library (Python 3.x implementation is given below)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

duplicate= [2, 4, 10, 20, 5, 2, 20, 4]

print(list(set(duplicate)))  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 4, 10, 20, 5] 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

