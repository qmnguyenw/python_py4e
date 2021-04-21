Python | Find number of lists in a tuple



Given a tuple of lists, the task is to find number of lists in a tuple. This
is a very basic problem but can be useful while making some utility
application.

 **Method #1: Using _len_**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find number of list in a tuple

 

# Initial list 

Input1 = ([1, 2, 3, 4], [5, 6, 7, 8])

Input2 = ([1, 2], [3, 4], [5, 6])

Input3 = ([9, 8, 7, 6, 5, 4, 3, 2,
1], [1, 2, 3])

 

# Using len to find no of list in tuple

Output1 = len(Input1)

Output2 = len(Input2)

Output3 = len(Input3)

 

# Printing

print("Initial list :")

print(Input1)

print("No of list in tuples are :")

print(Output1)

print("\n")

 

print("Initial list :")

print(Input2)

print("No of list in tuples are :")

print(Output2)

print("\n")

 

 

print("Initial list :")

print(Input3)

print("No of list in tuples are :")

print(Output3)

print("\n")  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list :
    ([1, 2, 3, 4], [5, 6, 7, 8])
    No of list in tuples are :
    2
    
    
    Initial list :
    ([1, 2], [3, 4], [5, 6])
    No of list in tuples are :
    3
    
    
    Initial list :
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3])
    No of list in tuples are :
    2
    

  
**Method #2: Using function and isinstance**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find number of list in a tuple

 

# Using find function

def find(Input):

 if isinstance(Input, list):

 return 1

 else:

 return len(Input)

 

# List initialization

Input1 = ([1, 2, 3, 4], [5, 6, 7, 8])

Input2 = ([1, 2], [3, 4], [5, 6])

Input3 = ([9, 8, 7, 6, 5, 4, 3, 2,
1])

 

# using find

Output1 = find(Input1)

Output2 = find(Input2)

Output3 = find(Input3)

 

# printing

print("Initial list :")

print(Input1)

print("No of list in tuples are :")

print(Output1)

print("\n")

 

print("Initial list :")

print(Input2)

print("No of list in tuples are :")

print(Output2)

print("\n")

 

 

print("Initial list :")

print(Input3)

print("No of list in tuples are :")

print(Output3)

print("\n")  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list :
    ([1, 2, 3, 4], [5, 6, 7, 8])
    No of list in tuples are :
    2
    
    
    Initial list :
    ([1, 2], [3, 4], [5, 6])
    No of list in tuples are :
    3
    
    
    Initial list :
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    No of list in tuples are :
    1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

