Python – Check if any list element is present in Tuple



Given a tuple, check if any list element is present in it.

>  **Input** : test_tup = (4, 5, 10, 9, 3), check_list = [6, 7, 10, 11]  
>  **Output** : True  
>  **Explanation** : 10 occurs in both tuple and list.
>
>  **Input** : test_tup = (4, 5, 12, 9, 3), check_list = [6, 7, 10, 11]  
>  **Output** : False  
>  **Explanation** : No common elements.

 **Method #1 : Using loop**

In this, we keep a boolen variable, keeping record of all elements, if found,
then returns True, else False.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if any list element is present in Tuple

# Using loop

 

# initializing tuple

test_tup = (4, 5, 7, 9, 3)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing list 

check_list = [6, 7, 10, 11]

 

res = False

for ele in check_list:

 

 # checking using in operator

 if ele in test_tup :

 res = True

 break

 

# printing result 

print("Is any list element present in tuple ? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : (4, 5, 7, 9, 3)
    Is any list element present in tuple ? : True
    

**Method #2 : Using any()**

This returns True, if any element of list is found in tuple, test using in
operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if any list element is present in Tuple

# Using any()

 

# initializing tuple

test_tup = (4, 5, 7, 9, 3)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing list 

check_list = [6, 7, 10, 11]

 

# generator expression is used for iteration 

res = any(ele in test_tup for ele in check_list)

 

# printing result 

print("Is any list element present in tuple ? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : (4, 5, 7, 9, 3)
    Is any list element present in tuple ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

