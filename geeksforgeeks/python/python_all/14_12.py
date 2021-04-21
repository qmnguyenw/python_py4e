Python – Test if elements of list are in Min/Max range from other list



Given two lists, the task is to write a Python Program to return true if all
elements from second list are in range of min and max values of the first
list.

 **Examples:**

>  **Input** : test_list = [5, 6, 3, 7, 8, 10, 9], range_list = [4, 7, 9, 6]  
> **Output** : True  
> **Explanation** : Min and max in list 1 are 3 and 10, all elements are in
> range in other list.  
>
>
> **Input** : test_list = [5, 6, 3, 7, 8, 10, 9], range_list = [4, 7, 9, 16]  
> **Output** : False  
> **Explanation** : Min and max in list 1 are 3 and 10, all elements are not
> in range in other list.

**Method #1 : Using loop +** **min()** **+** **max()**

  

  

In this, we iterate for all the elements in second list and compare for each
element, if any element is less than min or greater than max, result is
flagged off and false is returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Min/Max range test from other list

# Using loop + min() + max()

 

# initializing list

test_list = [5, 6, 3, 7, 8, 10, 9]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing range_list

range_list = [4, 7, 9, 6]

 

res = True

for ele in range_list:

 

 # flag off list in case of any off range element

 if ele max(test_list):

 res = False

 break

 

# printing result

print("Are all elements in min/max range? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 6, 3, 7, 8, 10, 9]
    Are all elements in min/max range? : True

 **Method #2 : Using** **all()** **+** **min()** **+** **max()**

In this, we check for all the elements to be in range using all(), and min()
and max() are used to get the maximum and minimum elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Min/Max range test from other list

# Using all() + min() + max()

 

# initializing list

test_list = [5, 6, 3, 7, 8, 10, 9]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing range_list

range_list = [4, 7, 9, 6]

 

# checking for all values in range using all()

res = all(ele >= min(test_list) and ele <=
max(test_list)

 for ele in range_list)

 

# printing result

print("Are all elements in min/max range? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 6, 3, 7, 8, 10, 9]
    Are all elements in min/max range? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

