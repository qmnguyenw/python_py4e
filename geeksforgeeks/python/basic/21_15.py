Python Set | update()



 **update()** function in set adds elements from a set (passed as an argument)
to the set.

>  **Syntax :**  
>  set1.update(set2)  
> Here set1 is the set in which set2 will be added.
>
>  **Parameters :**  
>  Update() method takes only a single argument. The single argument can be a
> set, list, tuples or a dictionary. It automatically converts into a set and
> adds to the set.
>
>  **Return value :** This method adds set2 to set1 and returns nothing.

 **Code #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# use of update() method 

 

 

list1 = [1, 2, 3] 

list2 = [5, 6, 7] 

list3 = [10, 11, 12]

 

# Lists converted to sets 

set1 = set(list2) 

set2 = set(list1)

 

# Update method 

set1.update(set2)

 

# Print the updated set 

print(set1) 

 

 

# List is passed as an parameter which 

# gets automatically converted to a set 

set1.update(list3) 

print(set1)  
  
---  
  
 __

 __

Output :

    
    
    {1, 2, 3, 5, 6, 7}
    {1, 2, 3, 5, 6, 7, 10, 11, 12}
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# use of update() method 

 

list1 = [1, 2, 3, 4] 

list2 = [1, 4, 2, 3, 5] 

alphabet_set = {'a', 'b', 'c'}

 

# lists converted to sets 

set1 = set(list2) 

set2 = set(list1)

 

# Update method 

set1.update(set2) 

 

# Print the updated set 

print(set1) 

 

set1.update(alphabet_set)

print(set1)  
  
---  
  
 __

 __

Output :

    
    
    {1, 2, 3, 4, 5}
    {1, 2, 3, 4, 5, 'c', 'b', 'a'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

