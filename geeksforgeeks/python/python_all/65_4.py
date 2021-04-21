Python – Consecutive elements maximum frequencies



Sometimes, while working with Python lists we can have a problem in which we
need to extract the maximum frequencies of consecutive elements. This kind of
problem can occur as application in many domains such as day-day programming
and competitive programming. Let’s discuss certain ways in which this task can
be performed.

>  **Input** : test_list = [7, 6, 7, 7]  
>  **Output** : {7: 2, 6: 1}
>
>  **Input** : test_list = [7, 7, 7]  
>  **Output** : {7: 3}

 **Method #1 : Using loop +groupby()**  
The combination of above functions can be used to perform this task. In this,
we group all the consecutive elements and then generate the dictionary of
maximum frequencies using dictionary keys comparison with current maximum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive elements maximum frequencies

# Using loop + groupby()

from itertools import groupby

 

# initializing list

test_list = [5, 6, 7, 7, 6, 6, 5, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Consecutive elements maximum frequencies

# Using loop + groupby()

res = {}

for key, val in groupby(test_list):

 sub = sum(1 for _ in val)

 if res.get(key, float('-inf')) < sub:

 res[key] = sub

 

# printing result 

print("The maximum frequencies : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [5, 6, 7, 7, 6, 6, 5, 7]
    The maximum frequencies : {5: 1, 6: 2, 7: 2}
    

