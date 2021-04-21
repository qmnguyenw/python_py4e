Python – Convert Matrix to overlapping Tuple Pairs



Sometimes, while working with Python data, we can have a problem in which we
need to perform overlap of elements in Matrix, and convert them as tuple
pairs. This kind of problem can occur in various application in data domain.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [[5, 6, 3], [8, 6, 2], [2, 5, 1]]  
>  **Output** : [(5, 6), (6, 3), (8, 6), (6, 2), (2, 5), (5, 1)]
>
>  **Input** : test_list = [[5, 6, 3]]  
>  **Output** : [(5, 6), (6, 3)]

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate each list and extract consecutive elements and add them as pair in
result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to overlapping Tuple Pairs

# Using loop

 

# initializing list

test_list = [[5, 6, 7], [8, 6, 5], [2, 5,
7]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Matrix to overlapping Tuple Pairs

# Using loop

res = []

for sub in test_list:

 res.append((sub[0], sub[1]))

 res.append((sub[1], sub[2]))

 

# printing result 

print("Filtered tuples : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [[5, 6, 7], [8, 6, 5], [2, 5, 7]]
    Filtered tuples : [(5, 6), (6, 7), (8, 6), (6, 5), (2, 5), (5, 7)]
    

