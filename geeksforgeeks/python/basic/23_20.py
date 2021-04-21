Reversing a List in Python



Python provides us with various ways of reversing a list. We will go through
few of the many techniques on how a list in python can be reversed.  
Examples:

    
    
    Input : list = [10, 11, 12, 13, 14, 15]
    Output : [15, 14, 13, 12, 11, 10]
    
    Input : list = [4, 5, 6, 7, 8, 9]
    Output : [9, 8, 7, 6, 5, 4]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1: Using the reversed() built-in function.**  
In this method, we neither reverse a list in-place(modify the original list),
nor we create any copy of the list. Instead, we get a reverse iterator which
we use to cycle through the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Reversing a list using reversed()

def Reverse(lst):

 return [ele for ele in reversed(lst)]

 

# Driver Code

lst = [10, 11, 12, 13, 14, 15]

print(Reverse(lst))  
  
---  
  
 __

 __

Output:

    
    
    [15, 14, 13, 12, 11, 10]
    

**Method 2: Using the reverse() built-in function.**  
Using the reverse() method we can reverse the contents of the list object
**in-place** i.e., we don’t need to create a new list instead we just copy the
existing elements to the original list in reverse order. This method directly
modifies the original list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Reversing a list using reverse()

def Reverse(lst):

 lst.reverse()

 return lst

 

lst = [10, 11, 12, 13, 14, 15]

print(Reverse(lst))  
  
---  
  
 __

 __

Output:

    
    
    [15, 14, 13, 12, 11, 10]
    

**Method 3: Using the slicing technique.**  
In this technique, a copy of the list is made and the list is not sorted in-
place. Creating a copy requires more space to hold all of the existing
elements. This exhausts more memory.

 __

 __  
 __

 __

 __  
 __  
 __

# Reversing a list using slicing technique

def Reverse(lst):

 new_lst = lst[::-1]

 return new_lst

 

lst = [10, 11, 12, 13, 14, 15]

print(Reverse(lst))  
  
---  
  
 __

 __

Output:

    
    
    [15, 14, 13, 12, 11, 10]
    

To get a better understanding on the slicing technique refer Slicing
Techniques in Python.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

