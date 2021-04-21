Python – Convert List of lists to list of Sets



Given a list containing lists, the task is to write a Python Program to
convert it to a list containing sets.

 **Examples:**

    
    
     **Input :** [[1, 2, 1], [1, 2, 3], [2, 2, 2, 2], [0]]
    **Output :** [{1, 2}, {1, 2, 3}, {2}, {0}]
    
    **Input :** [[4, 4], [5, 5, 5], [1, 2, 3]]
    **Output :** [{4}, {5}, {1, 2, 3}]

 **Method 1: Using** **list comprehension**

This can easily be achieved using list comprehension. We just iterate through
each list converting the lists to the sets.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# python3 program to convert list

# of lists to a list of sets

 

 

# initializing list

test_list = [[1, 2, 1], [1, 2, 3], [2, 2,
2, 2], [0]]

 

# printing original list

print("The original list of lists : " + str(test_list))

 

# using list comprehension

# convert list of lists to list of sets

res = [set(ele) for ele in test_list]

 

# print result

print("The converted list of sets : " + str(res))  
  
---  
  
 __

 __

