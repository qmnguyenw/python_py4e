Python – Append Missing elements from other List



Given 2 lists, append elements missing from list 1 to list 2.

>  **Input** : test_list1 = [5, 6, 4, 8, 9, 1], test_list2 = [9, 8, 10]  
>  **Output** : [5, 6, 4, 1, 9, 8, 10]  
>  **Explanation** : 5, 6, 4, 1 added to list 2, in order.
>
>  **Input** : test_list1 = [5, 6, 4, 8, 9, 1], test_list2 = [9, 10]  
>  **Output** : [5, 6, 4, 8, 1, 9, 10]  
>  **Explanation** : 5, 6, 4, 8, 1 added to list 2, in order.

 **Method #1 : Using list comprehension**

In this, we iterate list 1 to check for missing elements in list 2, then add
these elements to list 2.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Missing elements from other List

# Using list comprehension

 

# initializing list

test_list1 = [5, 6, 4, 8, 9, 1]

test_list2 = [9, 8, 7]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# extracting elements from list 1 which are not in list 2

temp1 = [ele for ele in test_list1 if ele not in
test_list2]

 

# constructing result 

res = temp1 + test_list2

 

# printing result 

print("The modified list 2 : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [5, 6, 4, 8, 9, 1]
    The original list 2 is : [9, 8, 7]
    The modified list 2 : [5, 6, 4, 1, 9, 8, 7]
    

**Method #2 : Using set() + “-” operator + extend()**

In this, we check for elements of list 1 missing from list 2 using set() and –
operator and extend() is used to join both the list to get desired result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Missing elements from other List

# Using set() + "-" operator + extend()

 

# initializing list

test_list1 = [5, 6, 4, 8, 9, 1]

test_list2 = [9, 8, 7]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# finding missing words

rem_list = (set(test_list1) - set(test_list2))

 

# checking order

res = [ele for ele in test_list1 if ele in rem_list] 

 

# joining result

res.extend(test_list2)

 

# printing result 

print("The modified list 2 : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [5, 6, 4, 8, 9, 1]
    The original list 2 is : [9, 8, 7]
    The modified list 2 : [5, 6, 4, 1, 9, 8, 7]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

