Python – Sort from Kth index in List



Given a list of elements, perform sort from Kth index of List.

>  **Input** : test_list = [7, 3, 7, 6, 4, 9], K = 2
>
>  **Output** : [7, 3, 4, 6, 7, 9]
>
>  **Explanation** : List is unsorted till 3 (1st index), From 2nd Index, its
> sorted.
>
> **Input** : test_list = [5, 4, 3, 2, 1], K= 3
>
>  
>
>
>  
>
>
>  **Output** : [5, 4, 3, 1, 2]
>
>  **Explanation** : Only last two elements, 1, 2 are sorted.

**Method #1 : Using loop + list slicing**

This is one of the ways in which this task can be performed. In this, we
extract each element before K in list and then perform list slice using slice
symbol and perform sort over the extracted sliced list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Perform sort from Kth index

# Using loop + list slicing

 

# initializing list

test_list = [8, 4, 7, 3, 2, 14, 6]

 

# printing original list

print("The original list : " + str(test_list))

 

# initialzing K

K = 3

 

# Using loop + list slicing

res = []

 

# Using loop to extract elements till K

for idx, ele in enumerate(test_list):

 if idx < K:

 res.append(ele)

 

# join sorted and unsorted segments

res = res + sorted(test_list[K:])

 

# printing result

print("Partially sorted list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [8, 4, 7, 3, 2, 14, 6]
    Partially sorted list : [8, 4, 7, 2, 3, 6, 14]
    
    
    

**Method #2 : Using double List slicing**

This is yet another way in which we perform this task. In this, we perform the
task of list slicing for slicing the unsort part as well and perform
concatenation, delivering a one liner alternative to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Perform sort from Kth index

# Using Using double List slicing

 

# initializing list

test_list = [8, 4, 7, 3, 2, 14, 6]

 

# printing original list

print("The original list : " + str(test_list))

 

# initialzing K

K = 3

 

# Using loop + list slicing

res = []

 

# Using loop to extract elements till K

# Concatenating unsort and sorted part as one liner

res = test_list[:K] + sorted(test_list[K:])

 

# printing result

print("Partially sorted list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [8, 4, 7, 3, 2, 14, 6]
    Partially sorted list : [8, 4, 7, 2, 3, 6, 14]
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

