Python – Check if elements index are equal for list elements



Given two lists and check list, test if for each element in check list,
elements occur in similar index in 2 lists.

>  **Input** : test_list1 = [2, 6, 9, 7, 8], test_list2 = [2, 7, 9, 4, 8],
> check_list = [9, 8, 7]  
>  **Output** : False  
>  **Explanation** : 7 is at 4th and 2nd place in both list, hence False.
>
>  **Input** : test_list1 = [2, 6, 9, 7, 8], test_list2 = [2, 6, 9, 4, 8],
> check_list = [9, 8, 6]  
>  **Output** : True  
>  **Explanation** : All from checklist at similar index, hence True.

 **Method #1 : Using loop**

In this, we iterate for all the elements in list, if elements are different
and is present in check list, then False is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if elements index are equal for list elements

# Using loop

 

# initializing lists

test_list1 = [2, 6, 9, 7, 8]

test_list2 = [2, 7, 9, 4, 8]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# initializing check_list

check_list = [9, 8, 2]

 

res = True

for idx, ele in enumerate(test_list1):

 

 # check for indifference and containment

 if test_list1[idx] != test_list2[idx] and ele in
check_list:

 res = False

 break

 

# printing result 

print("Are elements at same index for required instances ?: " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [2, 6, 9, 7, 8]
    The original list 2 : [2, 7, 9, 4, 8]
    Are elements at same index for required instances ?:  True
    

**Method #2 : Using zip() + all() + generator expression**

In this, we pair like indices using zip() and then all() is used to check for
all indices, generator expression is used for iteration logic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if elements index are equal for list elements

# Using zip() + all() + generator expression

 

# initializing lists

test_list1 = [2, 6, 9, 7, 8]

test_list2 = [2, 7, 9, 4, 8]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# initializing check_list

check_list = [9, 8, 2]

 

# checking for all elements equal in check list using all()

res = all(a == b for a, b in zip(test_list1,
test_list2) if a in check_list)

 

# printing result 

print("Are elements at same index for required instances ?: " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [2, 6, 9, 7, 8]
    The original list 2 : [2, 7, 9, 4, 8]
    Are elements at same index for required instances ?:  True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

