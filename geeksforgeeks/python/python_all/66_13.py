Python – Paired elements grouping



Sometimes, while working with Python records, we can have a problem in which
we have tuple list as data and we desire to group all the elements which form
a chain, i.e are indirect pairs of each other or are connected components.
This kind of problem can occur in domains such as competitive programming.
Let’s discuss certain way in which this task can be performed.

>  **Input** : test_list = [(1, 3), (4, 5)]  
>  **Output** : []
>
>  **Input** : test_list = [(1, 3), (3, 5)]  
>  **Output** : [{1, 3, 5}]

 **Method : Using loop +set() + intersection()**  
The combination of above functionalities can be used to solve this problem. In
this, we iterate for all the elements and then for all the elements occurring
after that in nested loop. The intersection of elements is performed, and if,
any element if found similar, i.e size >= 0, then tuple is merged in similar
chain.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Paired elements grouping

# Using loop + set() + intersection()

 

# initializing list

test_list = [(1, 3), (4, 5), (1, 7), (3,
4), (7, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Paired elements grouping

# Using loop + set() + intersection()

res = []

for sub in test_list:

 idx = test_list.index(sub)

 sub_list = test_list[idx + 1:]

 if idx <= len(test_list) - 2:

 for ele in sub_list:

 intrsct = set(sub).intersection(set(ele))

 if len(intrsct) > 0:

 res.append(set(sub + ele))

 

# printing result 

print("The grouped list : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(1, 3), (4, 5), (1, 7), (3, 4), (7, 8)]
    The grouped list : [{1, 3, 7}, {1, 3, 4}, {3, 4, 5}, {8, 1, 7}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

