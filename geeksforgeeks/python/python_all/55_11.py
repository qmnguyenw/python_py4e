Python – Join Tuples if similar initial element



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform concatenation of records from the similarity of initial
element. This problem can have applications in data domains such as Data
Science. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]  
>  **Output** : [(5, 6, 7, 8), (6, 10), (7, 13)]
>
>  **Input** : test_list = [(5, 6), (6, 7), (6, 8), (6, 10), (7, 13)]  
>  **Output** : [(5, 6), (6, 7, 8, 10), (7, 13)]

 **Method #1 : Using loop**  
This is brute way in which this task can be done. In this, we create new
tuple, if we find no occurrence of similar tuple values previously. Slicing is
used to add rest of elements to created tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Join Tuples if similar initial element

# Using loop

 

# initializing list

test_list = [(5, 6), (5, 7), (6, 8), (6,
10), (7, 13)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Join Tuples if similar initial element

# Using loop

res = []

for sub in test_list: 

 if res and res[-1][0] == sub[0]: 

 res[-1].extend(sub[1:]) 

 else:

 res.append([ele for ele in sub]) 

res = list(map(tuple, res))

 

# printing result 

print("The extracted elements : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
    The extracted elements : [(5, 6, 7), (6, 8, 10), (7, 13)]
    

