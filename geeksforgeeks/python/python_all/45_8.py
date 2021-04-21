Python – Assign pair elements from Tuple Lists



Given a tuple list, assign with each element, its pair elements from other
similar pairs.

>  **Input** : test_list = [(5, 3), (7, 5), (8, 4)]  
>  **Output** : {5: [3], 7: [5], 8: [4], 4: []}  
>  **Explanation** : 1st elements are paired with respective 2nd elements from
> all tuples.
>
>  **Input** : test_list = [(5, 3)]  
>  **Output** : {5: [3]}  
>  **Explanation** : Only one tuples, 5 paired with 3.

 **Method : Using setdefault() + loop**

In this, we use brute way to solve this, iterate for each tuple, and set
default values for each, key and value as empty list, appending the elements
to respective list if already present.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign pair elements from Tuple Lists

# Using setdefault + loop

 

# initializing list

test_list = [(5, 3), (7, 5), (2, 7), (3,
8), (8, 4)]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing dictionary

res = dict()

for key, val in test_list:

 

 # adding to both, corresponding keys and values

 res.setdefault(val, [])

 res.setdefault(key, []).append(val)

 

# printing results 

print("The resultant pairings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)]
    The resultant pairings : {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

