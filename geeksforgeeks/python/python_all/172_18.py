Python | Check if all the values in a list are less than a given value



Given a list, write a Python program to check if all the values in a list are
less than the given value.

 **Examples:**

    
    
     **Input :** list = [11, 22, 33, 44, 55] 
            value = 22 
    **Output :** No
    
    **Input :** list = [11, 22, 33, 44, 55] 
            value = 65 
    **Output :** Yes

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method #1:** Traversing the list  
Compare each element by iterating through the list and check if all the
elements in the given list are less than the given value or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if all values

# in the list are less than given value

 

# Function to check the value

def CheckForLess(list1, val): 

 

 # traverse in the list 

 for x in list1: 

 

 # compare with all the 

 # values with value

 if val <= x: 

 return False

 return True

 

# Driver code 

list1 = [11, 22, 33, 44, 55] 

val = 65

if (CheckForLess(list1, val)): print("Yes")

else: print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

  

  

**Method #2:** Using all() function  
Using all() function we can check if all values are less than any given
value in a single line. It returns true if the given condition inside the
all() function is true for all values, else it returns false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if all values

# in the list are less than given value

 

# Function to check the value

def CheckForLess(list1, val): 

 return(all(x < val for x in list1)) 

 

# Driver code 

list1 = [11, 22, 33, 44, 55] 

val = 65

if (CheckForLess(list1, val)): print("Yes")

else: print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

