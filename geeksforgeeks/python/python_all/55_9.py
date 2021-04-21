Python – Rearrange elements second index greater than first



Given 2 lists, for a given index, 2nd list element is always larger than
first, and if not, we rearrange it.

>  **Input** : test_list1 = [36, 38, 40, 132], test_list2 = [35, 37, 39, 41,
> 133]  
>  **Output** : [37, 39, 41, 133]  
>  **Explanation** : Each element in result list is greater than its index
> counterpart of 1st list. (Eg. 37 > 36)
>
>  **Input** : test_list1 = [2, 6], test_list2 = [5, 3, 8]  
>  **Output** : [5, 8]  
>  **Explanation** : Here 5 > 2 and 8 > 6.

 **Method : Using loop**  
This is brute way to tackle this problem. In this, we try to get best suitable
next higher element after the whole list traversal and perform the necessary
rearrangement.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rearrange elements second index greater than first

# Using loop

 

# initializing lists

test_list1 = [14, 16, 18, 110]

test_list2 = [13, 15, 17, 19, 111]

 

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Rearrange elements second index greater than first

# Using loop

x = y = 0

res1, res2 = [], []

while x < len(test_list2) and y < len(test_list1):

 

 # checking for greater element

 if test_list2[x] > test_list1[y]:

 res2.append(test_list2[x])

 res1.append(test_list1[y])

 while y < len(test_list1) and test_list2[x] > test_list1[y]:

 res1[-1] = test_list1[y]

 y += 1

 x += 1

 

# printing result 

print("List 2 after conversion : " + str(res2))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list 1 is : [14, 16, 18, 110]
    The original list 2 is : [13, 15, 17, 19, 111]
    List 2 after conversion : [15, 17, 19, 111]
    

