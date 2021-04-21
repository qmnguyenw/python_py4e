Python program to check if the list contains three consecutive common numbers
in Python



Our task is to print the element which occurs 3 consecutive times in a Python
list.

 **Example :**

    
    
    **Input :** [4, 5, 5, 5, 3, 8]
    
    **Output :** 5
    
    **Input :** [1, 1, 1, 64, 23, 64, 22, 22, 22]
    
    **Output** : 1, 22
    

**Approach :**

  1. Create a list.
  2. Create a loop for range size – 2.
  3. Check if the element is equal to the next element.
  4. Again check if the next element is equal to the next element.
  5. If both conditions are satisfied then print the element.

 **Example 1 :** Only one occurrence of a 3 consecutively occurring element.

 __

 __  
 __

 __

 __  
 __  
 __

# creating the array

arr = [4, 5, 5, 5, 3, 8]

 

# size of the list

size = len(arr)

 

# looping till length - 2

for i in range(size - 2):

 

 # checking the conditions

 if arr[i] == arr[i + 1] and arr[i + 1] ==
arr[i + 2]:

 

 # printing the element as the 

 # conditions are satisfied 

 print(arr[i])  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    5

 **Example 2 :** Multiple occurrences of 3 consecutively occurring elements.

 __

 __  
 __

 __

 __  
 __  
 __

# creating the array

arr = [1, 1, 1, 64, 23, 64, 22, 22,
22]

 

# size of the list

size = len(arr)

 

# looping till length - 2

for i in range(size - 2):

 

 # checking the conditions

 if arr[i] == arr[i + 1] and arr[i + 1] ==
arr[i + 2]:

 

 # printing the element as the 

 # conditions are satisfied 

 print(arr[i])  
  
---  
  
 __

 __

 **Output :**

    
    
    1
    22
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

