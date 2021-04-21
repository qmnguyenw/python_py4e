Python – Split List on next larger value



Given a List, perform split on next larger value.

>  **Input** : test_list = [4, 2, 3, 7, 5, 1, 3, 4, 11, 2]  
>  **Output** : [[4, 2, 3], [7, 5, 1, 3, 4], [11, 2]]  
>  **Explanation** : After 4, 7 is greater, split happens at that element, and
> so on.
>
>  **Input** : test_list = [4, 2, 3, 7, 5, 1, 3, 4, 1, 2]  
>  **Output** : [[4, 2, 3], [7, 5, 1, 3, 4, 1, 2]]  
>  **Explanation** : After 4, 7 is greater, split happens at that element.

 **Method : Using loop**

In this, we iterate list and keep track of split value, if higher value than
recorded value is found, new list is created from it, and split value is
current value.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split List on next larger value

# Using loop

 

# initializing list

test_list = [4, 2, 3, 7, 5, 9, 3, 4,
11, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# starting value as ref.

curr = test_list[0]

temp = []

res = []

for ele in test_list:

 

 # if curr value greater than split

 if ele > curr:

 res.append(temp)

 curr = ele

 temp = []

 temp.append(ele)

res.append(temp)

 

# printing results

print("Split List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 2, 3, 7, 5, 9, 3, 4, 11, 2]
    Split List : [[4, 2, 3], [7, 5], [9, 3, 4], [11, 2]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

