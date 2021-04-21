Python – Maximum of K element in other list



Given two lists, extract maximum of elements with similar K in correspoding
list.

>  **Input** : test_list1 = [4, 3, 6, 2, 8], test_list2 = [3, 6, 3, 4, 3], K =
> 3  
>  **Output** : 8  
>  **Explanation** : Elements corresponding to 3 are, 4, 6, and 8, Max. is 8.
>
>  **Input** : test_list1 = [10, 3, 6, 2, 8], test_list2 = [5, 6, 5, 4, 5], K
> = 5  
>  **Output** : 10  
>  **Explanation** : Elements corresponding to 5 are, 10, 6, and 8, Max. is
> 10.

 **Method #1 : Using loop + max()**

In this, we extract all elements from list 1 which are equal to K in list 2,
and then perform max() to get maximum of them.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum of K element in other list

# Using loop + max()

 

# initializing lists

test_list1 = [4, 3, 6, 2, 9]

test_list2 = [3, 6, 3, 4, 3]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K 

K = 3

 

res = []

for idx in range(len(test_list1)):

 

 # checking for K in 2nd list

 if test_list2[idx] == K :

 res.append(test_list1[idx])

 

# getting Maximum element

res = max(res)

 

# printing result 

print("Extracted Maximum element : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [4, 3, 6, 2, 9]
    The original list 2 is : [3, 6, 3, 4, 3]
    Extracted Maximum element : 9
    

**Method #2 : list comprehension + max() + zip()**

In this, we perform task of pairing elements using zip() and is one-liner
solution provided using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum of K element in other list

# Using list comprehension + max() + zip()

 

# initializing lists

test_list1 = [4, 3, 6, 2, 9]

test_list2 = [3, 6, 3, 4, 3]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K 

K = 3

 

# one liner to solve this problem

res = max([sub1 for sub1, sub2 in zip(test_list1, test_list2)
if sub2 == K])

 

# printing result 

print("Extracted Maximum element : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [4, 3, 6, 2, 9]
    The original list 2 is : [3, 6, 3, 4, 3]
    Extracted Maximum element : 9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

