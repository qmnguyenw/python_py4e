Python program to Test if all y occur after x in List



Given a List, test if all occurrences of y are after the occurrence of x in
the list.

>  **Input** : test_list = [4, 5, 6, 2, 4, 5, 2, 9], x, y = 6, 2  
> **Output** : True  
> **Explanation** : All occurrences of 2 are after 6, hence true.
>
>  **Input** : test_list = [4, 2, 5, 6, 2, 4, 5, 2, 9], x, y = 6, 2  
> **Output** : False  
> **Explanation** : All occurrences of 2 are not after 6, hence true.

**Method #1 : Using** **loop** **+** **index()**

In this, we check for an index of x in the list, and then run a loop to get
the occurrence of y, if any y occurs before x index, the result is False.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if y occurs after x in List

# Using loop + index()

 

# initializing list

test_list = [4, 5, 6, 2, 4, 5, 2, 9]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing x, y 

x, y = 6, 2

 

# getting index of x 

xidx = test_list.index(x)

 

res = True

for idx, ele in enumerate(test_list):

 

 # checking for y and comparing index 

 if ele == y and idx < xidx:

 res = False

 break

 

# printing result 

print("Do all y occur after x : " + str(res))  
  
---  
  
 __

 __

  
**Output:**

    
    
    The original list is : [4, 5, 6, 2, 4, 5, 2, 9]
    Do all y occur after x : True

 **Method #2 : Using** **all()** **\+ index()**

In this, we test for all the indices of y using all(), and index() is used to
get the index of x in the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if y occurs after x in List

# Using all() + index()

 

# initializing list

test_list = [4, 5, 6, 2, 4, 5, 2, 9]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing x, y 

x, y = 6, 2

 

# getting index of x 

xidx = test_list.index(x)

 

# checking for all indices of y in list 

res = all(idx > xidx for idx, ele in enumerate(test_list)
if ele == y)

 

# printing result 

print("Do all y occur after x : " + str(res))  
  
---  
  
 __

 __

  
**Output:**

    
    
    The original list is : [4, 5, 6, 2, 4, 5, 2, 9]
    Do all y occur after x : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

