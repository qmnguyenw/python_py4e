Python – Remove elements at Indices in List



Given List, remove all the elements present in indices list.

>  **Input** : test_list = [5, 6, 3, 7, 8, 1, 2, 10], idx_list = [2, 4, 5]  
>  **Output** : [5, 6, 7, 2, 10]  
>  **Explanation** : 3, 6, and 1 has been removed.
>
>  **Input** : test_list = [5, 6, 3, 7, 8, 1, 2, 10], idx_list = [2]  
>  **Output** : [5, 6, 7, 8, 1, 2, 10]  
>  **Explanation** : 3 has been removed.

 **Method #1 : Using enumerate() + loop**

In this, we iterate for all the elements, and if index is present in list,
then that index element is omitted from result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove elements at Indices in List

# Using loop

 

# initializing list

test_list = [5, 6, 3, 7, 8, 1, 2, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing idx list 

idx_list = [2, 4, 5, 7]

 

res = []

for idx, ele in enumerate(test_list): 

 

 # checking if element not present in index list

 if idx not in idx_list:

 res.append(ele)

 

# printing results

print("Filtered List after removal : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 6, 3, 7, 8, 1, 2, 10]
    Filtered List after removal : [5, 6, 7, 2]
    

**Method #2 : Using enumerate() + list comprehension**

In this, we perform task of iteration using list comprehesion in compact way,
rest all method similar to above.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove elements at Indices in List

# Using enumerate() + list comprehension

 

# initializing list

test_list = [5, 6, 3, 7, 8, 1, 2, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing idx list 

idx_list = [2, 4, 5, 7]

 

# one-liner to test for element in index list

res = [ele for idx, ele in enumerate(test_list) if idx
not in idx_list]

 

# printing results

print("Filtered List after removal : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 6, 3, 7, 8, 1, 2, 10]
    Filtered List after removal : [5, 6, 7, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

