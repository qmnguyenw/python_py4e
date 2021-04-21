Python | Split a list into sublists of given lengths



The problem of splitting a list into sublists is quite generic but to split in
sublist of given length is not so common. Given a list of lists and list of
length, the task is to split the list into sublists of given length.

 **Example:**

    
    
     **Input :** Input = [1, 2, 3, 4, 5, 6, 7]
            length_to_split = [2, 1, 3, 1]
    
    **Output:** [[1, 2], [3], [4, 5, 6], [7]]
    

**Method #1:** Using islice to split a list into sublists of given length,
is the most elegant way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split a list

# into sublists of given length.

 

from itertools import islice

 

# Input list initialization

Input = [1, 2, 3, 4, 5, 6, 7]

 

# list of length in which we have to split

length_to_split = [2, 1, 3, 1]

 

# Using islice

Inputt = iter(Input)

Output = [list(islice(Inputt, elem))

 for elem in length_to_split]

 

# Printing Output

print("Initial list is:", Input)

print("Split length list: ", length_to_split)

print("List after splitting", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial list is: [1, 2, 3, 4, 5, 6, 7]
    Split length list:  [2, 1, 3, 1]
    List after splitting [[1, 2], [3], [4, 5, 6], [7]]
    

