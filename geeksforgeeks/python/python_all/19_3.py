Python program to remove each y occurrence before x in List



Given a list, remove all the occurrence of y before element x in list.

>  **Input** : test_list = [4, 5, 7, 4, 6, 7, 4, 9, 1, 4], x, y = 6, 4  
> **Output** : [5, 7, 6, 7, 4, 9, 1, 4]  
> **Explanation** : All occurrence of 4 before 6 are removed.
>
>  **Input** : test_list = [4, 5, 7, 4, 6, 7, 4, 9, 1, 4], x, y = 6, 7  
> **Output** : [4, 5, 4, 6, 7, 4, 9, 1, 4]  
> **Explanation** : All occurrence of 7 before 6 are removed.  
>

**Method #1 : Using list comprehension + index()**

In this, we get the index of x using index(), and check for y before x, if
present that is excluded from the result list. The iteration and comparison
are performed using list comparison.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove each y occurrence before x in List

# Using list comprehension + index()

 

# initializing list

test_list = [4, 5, 7, 4, 6, 7, 4, 9,
1, 4]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing x and y 

x, y = 6, 4

 

# getting index using index()

xidx = test_list.index(x)

 

# retain all values other than y, and y if its index greater than x index

res = [ele for idx, ele in enumerate(test_list) if ele
!= y or (ele == y and idx > xidx) ]

 

# printing result 

print("Filtered List " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 5, 7, 4, 6, 7, 4, 9, 1, 4]
    Filtered List [5, 7, 6, 7, 4, 9, 1, 4]
    

**Method #2 : Using loop + index()**

This task of filtering is done using comparison operators in the loop,
index(), is used to get the index of x in list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove each y occurrence before x in List

# Using loop + index()

 

# initializing list

test_list = [4, 5, 7, 4, 6, 7, 4, 9,
1, 4]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing x and y 

x, y = 6, 4

 

# getting index using index()

xidx = test_list.index(x)

 

# filtering using comparison operators

res = []

for idx, ele in enumerate(test_list):

 if ele != y or (ele == y and idx > xidx):

 res.append(ele)

 

# printing result 

print("Filtered List " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 5, 7, 4, 6, 7, 4, 9, 1, 4]
    Filtered List [5, 7, 6, 7, 4, 9, 1, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

