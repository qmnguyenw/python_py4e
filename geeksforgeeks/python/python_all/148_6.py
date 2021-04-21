Python | Remove element from given list containing specific digits



Given a list, the task is to remove all those elements from list which
contains the specific digits.

 **Examples:**

    
    
    **Input:** lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13, 15, 16]
           no_delete = ['2', '3', '4', '0']
    **Output:** [1, 5, 6, 7, 8, 9, 11, 15, 16]
    **Explanation:**
    Numbers 2, 3, 4, 10, 12, 13, 14 contains digits 
    from no_delete, therefore remove them.
    
    **Input:** lst = [1, 2, 3, 4, 5, 6, 7, 8, 13, 15, 16]
           no_delete = {'6', '5', '4', '3'}
    **Output:** [1, 2, 7, 8, 9, 10, 11, 12]
    **Explanation:**
    Numbers 3, 4, 5, 6, 13, 14, 15, 16 contains digits 
    from no_delete, therefore remove them.
    

  
Below are some methods to do the task.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all those elements

# from list which contains certain digits

 

# Input List Initialisation

Input = [1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, 12, 14, 13, 15, 16]

 

# Numbers to delete

no_delete = [1, 0]

 

# Output List Initialisation

Output = []

 

# Using iteration to remove all the elements 

for elem in Input:

 flag = 1

 temp = elem

 while elem > 0:

 rem = elem % 10

 elem = elem//10

 if rem in no_delete:

 flag = 0

 if flag == 1:

 Output.append(temp)

 

# Printing Output 

print("Intial list is :", Input)

print("Delete list :", no_delete)

print("List after removing elements is :", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Intial list is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13, 15, 16]
    Delete list : [1, 0]
    List after removing elements is : [2, 3, 4, 5, 6, 7, 8, 9]
    

