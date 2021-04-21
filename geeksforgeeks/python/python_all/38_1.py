Python – Remove Rows for similar Kth column element



Given a Matrix, remove row if similar element has occurrred in row above in
Kth column.

>  **Input** : test_list = [[3, 4, 5], [2, 3, 5], [10, 4, 3], [7, 8, 9], [9,
> 3, 6]], K = 2  
>  **Output** : [[3, 4, 5], [10, 4, 3], [7, 8, 9], [9, 3, 6]]  
>  **Explanation** : In [2, 3, 5], we already has list [3, 4, 5] having 5 at
> K, i.e 2nd pos.
>
>  **Input** : test_list = [[3, 4, 5], [2, 3, 3], [10, 4, 3], [7, 8, 9], [9,
> 3, 6]], K = 2  
>  **Output** : [[3, 4, 5], [2, 3, 3], [7, 8, 9], [9, 3, 6]]  
>  **Explanation** : In [10, 4, 3], we already has list [2, 3, 3] having 3 at
> K, i.e 2nd pos.

 **Method : Using loop**

In this, we maintain a memoization container which keeps track of elements in
Kth column, if row’s Kth column element is present already, that row is
omitted from result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Rows for similar Kth column element

# Using loop

 

# initializing list

test_list = [[3, 4, 5], [2, 3, 5], [10,
4, 3], [7, 8, 9], [9, 3, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

res = []

memo = []

for sub in test_list:

 

 # in operator used to check if present or not

 if not sub[K] in memo:

 res.append(sub)

 memo.append(sub[K])

 

# printing result 

print("The filtered Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[3, 4, 5], [2, 3, 5], [10, 4, 3], [7, 8, 9], [9, 3, 6]]
    The filtered Matrix : [[3, 4, 5], [2, 3, 5], [7, 8, 9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

