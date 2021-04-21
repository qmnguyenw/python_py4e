Python – Convert List to Index and Value dictionary



Given a List, convert it to dictionary, with separate keys for index and
values.

>  **Input** : test_list = [3, 5, 7, 8, 2, 4, 9], idx, val = “1”, “2”  
>  **Output** : {‘1’: [0, 1, 2, 3, 4, 5, 6], ‘2’: [3, 5, 7, 8, 2, 4, 9]}  
>  **Explanation** : Index and values mapped at similar index in diff. keys.,
> as “1” and “2”.
>
>  **Input** : test_list = [3, 5, 7], idx, val = “1”, “2”  
>  **Output** : {‘1’: [0, 1, 2], ‘2’: [3, 5, 7]}  
>  **Explanation** : Index and values mapped at similar index in diff. keys.,
> as “1” and “2”.

 **Method : Using loop + enumerate()**

In this, we iterate for list elements using enumerate() to get index along
with values, and append the values and indices accordingly in separate
dictionaries accordingly.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to Index and Value dictionary

# Using loop + enumerate()

 

# initializing list

test_list = [3, 5, 7, 8, 2, 4, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing keys for index and vals 

idx, val = "indx", "vals"

 

# initializing empty mesh

res = {idx : [], val : []}

for id, vl in enumerate(test_list):

 res[idx].append(id)

 res[val].append(vl)

 

# printing results

print("Constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 5, 7, 8, 2, 4, 9]
    Constructed dictionary : {'indx': [0, 1, 2, 3, 4, 5, 6], 'vals': [3, 5, 7, 8, 2, 4, 9]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

