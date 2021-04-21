Python | Add list elements with a multi-list based on index



Given two lists, one is a simple list and second is a multi-list, the task is
to add both lists based on index.

 **Example:**

    
    
     **Input:**
    List = [1, 2, 3, 4, 5, 6]
    List of list = [[0], [0, 1, 2], [0, 1], [0, 1], [0, 1, 2], [0]]
    
    **Output:**
    [[1], [2, 3, 4], [3, 4], [4, 5], [5, 6, 7], [6]]
    
    **Explanation:**
    [1] = [1+0]
    [2, 3, 4] = [0+2, 1+2, 2+2]
    [3, 4] = [3+0, 3+1]
    [4, 5] = [4+0, 4+1]
    [5, 6, 7] = [5+0, 5+1, 5+2]
    [6] = [6+0]
    

Let’s discuss some methods to do this task.

 **Method #1: Using iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to add list elements

# with a multi-list based on index 

 

# List initialization

List = [1, 2, 3, 4, 5, 6]

List_of_List = [[0], [0, 1, 2], [0, 1],

 [0, 1], [0, 1, 2], [0]]

Output = []

 

# Iteration 

for x in range(len(List)):

 temp = []

 for y in List_of_List[x]:

 temp.append(y + List[x])

 Output.append(temp)

 

# Printing

print("Initial list is:", List)

print("Initial list of list is :", List_of_List)

print("Output is", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial list is: [1, 2, 3, 4, 5, 6]
    Initial list of list is : [[0], [0, 1, 2], [0, 1], [0, 1], [0, 1, 2], [0]]
    Output is [[1], [2, 3, 4], [3, 4], [4, 5], [5, 6, 7], [6]]
    

