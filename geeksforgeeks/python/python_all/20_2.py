Python – Test if tuple list has Single element



Given a Tuple list, check if it is composed of only one element, used multiple
times.

>  **Input** : test_list = [(3, 3, 3), (3, 3), (3, 3, 3), (3, 3)]  
> **Output** : True  
> **Explanation** : All elements are equal to 3.
>
>  **Input** : test_list = [(3, 3, 3), (3, 3), (3, 4, 3), (3, 3)]  
> **Output** : False  
> **Explanation** : All elements are not equal to any particular element.  
>

**Method #1: Using loop**

In this, we check for all the elements and compare them with the initial
element of the initial tuple in the tuple list, if any element is different,
the result is flagged off.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if tuple list has Single element

# Using loop 

 

# initializing list

test_list = [(3, 3, 3), (3, 3), (3, 3,
3), (3, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for similar elements in list 

res = True

for sub in test_list:

 flag = True

 for ele in sub:

 

 # checking for element to be equal to initial element

 if ele != test_list[0][0]:

 flag = False

 break

 if not flag:

 res = False

 break

 

# printing result 

print("Are all elements equal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [(3, 3, 3), (3, 3), (3, 3, 3), (3, 3)]
    Are all elements equal : True

 **Method #2 : Using** **all()** **+** **list comprehension**

In this, we perform task of checking all elements to be same using all(), list
comprehension is used to perform task of iterating through all the tuples in
the tuple list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if tuple list has Single element

# Using all() + list comprehension

 

# initializing list

test_list = [(3, 3, 3), (3, 3), (3, 3,
3), (3, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for single element using list comprehension

res = all([all(ele == test_list[0][0] for ele
in sub) for sub in test_list])

 

# printing result

print("Are all elements equal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [(3, 3, 3), (3, 3), (3, 3, 3), (3, 3)]
    Are all elements equal : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

