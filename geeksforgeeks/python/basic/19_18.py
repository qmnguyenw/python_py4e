Python program to right rotate a list by n



Given a list, right rotate the list by n position.

Examples :

    
    
    Input : n = 2 
             List_1 = [1, 2, 3, 4, 5, 6]
    Output : List_1 = [5, 6, 1, 2, 3, 4]
    We get output list after right rotating 
    (clockwise) given list by 2.
    
    Input :  n = 3
             List_1 = [3, 0, 1, 4, 2, 3]
    Output : List_1 = [4, 2, 3, 3, 0, 1]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach #1 :** Traverse the first list one by one and then put the
elements at required places in a second list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to right rotate a list by n

 

# Returns the rotated list

def rightRotate(lists, num):

 output_list = []

 

 # Will add values from n to the new list

 for item in range(len(lists) - num, len(lists)):

 output_list.append(lists[item])

 

 # Will add the values before

 # n to the end of new list 

 for item in range(0, len(lists) - num): 

 output_list.append(lists[item])

 

 return output_list

 

# Driver Code

rotate_num = 3

list_1 = [1, 2, 3, 4, 5, 6]

 

print(rightRotate(list_1, rotate_num))  
  
---  
  
 __

 __

Output :

    
    
    [4, 5, 6, 1, 2, 3]
    

**Time complexity :** **O(n)**  

  

  

**Approach #2 :** Another approach to solve this problem by using _slicing
technique_. One way of slicing list is by using **len()** method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to right rotate

# a list by n using list slicing

n = 3

 

list_1 = [1, 2, 3, 4, 5, 6]

list_1 = (list_1[len(list_1) - n:len(list_1)] 

 + list_1[0:len(list_1) - n])

print(list_1)  
  
---  
  
 __

 __

Output:

    
    
    [4, 5, 6, 1, 2, 3]
    

  
**Approach #3 :** In the above method, last n elements of list_1 was taken and
then remaining elements of list_1. Another way is without using len() method.

 __

 __  
 __

 __

 __  
 __  
 __

# Right Rotating a list to n positions

n = 3

 

list_1 = [1, 2, 3, 4, 5, 6]

list_1 = (list_1[-n:] + list_1[:-n])

 

print(list_1)  
  
---  
  
 __

 __

Output :

    
    
    [4, 5, 6, 1, 2, 3]
    

**Time complexity :** **O(n)**  
  
**Note :**list_1[:] will return the whole list as the blank space on left of
slicing operator refers to start of list i.e 0 and blank space on right refers
to ending position of list.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

