Python – Substitute prefix part of List



Given 2 list, substitute one list as prefix elements of other.

>  **Input** : test_list1 = [4, 6, 8, 7], test_list2 = [2, 7, 9, 4, 2, 8]  
>  **Output** : [4, 6, 8, 7, 2, 8]  
>  **Explanation** : 4, 6, 8, 7 from list 1 and rest, 2 and 8 from list 2,
> substuting prefix of list 2.
>
>  **Input** : test_list1 = [4, 6], test_list2 = [2, 7, 9, 4, 2, 8]  
>  **Output** : [4, 6, 9, 4, 2, 8]  
>  **Explanation** : 4, 6 from list 1 and rest, 9, 4, 2 and 8 from list 2,
> substuting prefix of list 2.

 **Method #1 : Using len() + list slicing**

In this, we add the list 1 and then part of list 2 after size of list 1, using
len() and list slicing.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substitute prefix part of List

# Using len() + list slicing 

 

# initializing lists

test_list1 = [4, 6, 8, 7]

test_list2 = [2, 7, 9, 4, 2, 8, 6, 4,
1, 10]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# size slicing after length of list 1

res = test_list1 + test_list2[len(test_list1) : ]

 

# printing result 

print("The joined list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 6, 8, 7]
    The original list 2 : [2, 7, 9, 4, 2, 8, 6, 4, 1, 10]
    The joined list : [4, 6, 8, 7, 2, 8, 6, 4, 1, 10]
    

**Method #2 : Using * operator**

In this, we use * operator to perform task of packing and unpacking it to new
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substitute prefix part of List

# Using * operator

 

# initializing lists

test_list1 = [4, 6, 8, 7]

test_list2 = [2, 7, 9, 4, 2, 8, 6, 4,
1, 10]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# * operator reconstructs lists

res = [*test_list1, *test_list2[len(test_list1) : ]]

 

# printing result 

print("The joined list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 6, 8, 7]
    The original list 2 : [2, 7, 9, 4, 2, 8, 6, 4, 1, 10]
    The joined list : [4, 6, 8, 7, 2, 8, 6, 4, 1, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

