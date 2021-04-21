Python – Smallest missing element after K



Given a List, get the smallest missing element after K in List.

>  **Input** : test_list = [1, 3, 4, 5, 7, 9, 10], K = 5  
> **Output** : 6  
> **Explanation** : After 5, 6 is 1st element missing in list.
>
>  **Input** : test_list = [1, 3, 4, 5, 7, 9, 11], K = 9  
> **Output** : 10  
> **Explanation** : After 9, 10 is 1st element missing in list.

**Approach: Using loop**

In this, we iterate through numbers and check for element missing in list,
which is greater than K using conditionals.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Smallest missing element after K

# Using loop

 

# initializing list

test_list = [1, 3, 4, 5, 7, 9, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 7

 

ele = 1

 

# infinite loop to break at element found

while(1):

 

 # checking if greater than K and not in list

 if ele > K and ele not in test_list:

 res = ele

 break

 ele = ele + 1

 

# printing result

print("The Smallest element greater than K in list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 3, 4, 5, 7, 9, 10]
    The Smallest element greater than K in list : 8
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

