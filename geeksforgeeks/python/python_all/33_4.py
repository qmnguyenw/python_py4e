Python program for sum of consecutive numbers with overlapping in lists



Given a List, perform summation of consecutive elements, by overlapping.

>  **Input** : test_list = [4, 7, 3, 2]  
> **Output** : [11, 10, 5, 6]  
> **Explanation** : 4 + 7 = 11, 7 + 3 = 10, 3 + 2 = 5, and 2 + 4 = 6.
>
> **Input** : test_list = [4, 7, 3]  
> **Output** : [11, 10, 7]  
> **Explanation** : 4+7=11, 7+3=10, 3+4=7.  
>

**Method 1 : Using list comprehension + zip()**

In this, we zip list, with consecutive elements’ using zip() and then perform
summation using + operator. The iteration part is done using list
comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [4, 7, 3, 2, 9, 2, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using zip() to get pairing.

# last element is joined with first for pairing

res = [a + b for a, b in zip(test_list, test_list[1:]
+ [test_list[0]])]

 

# printing result

print("The Consecutive overlapping Summation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 7, 3, 2, 9, 2, 1]
    The Consecutive overlapping Summation : [11, 10, 5, 11, 11, 3, 5]
    
    

**Method #2 : Using sum() + list comprehension + zip()**

In this, we perform the task of getting summation using sum() and rest all
functionalities kept similar to the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive overlapping Summation

# Using sum() + list comprehension + zip()

 

# initializing list

test_list = [4, 7, 3, 2, 9, 2, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using sum() to compute elements sum

# last element is joined with first for pairing

res = [sum(sub) for sub in zip(test_list, test_list[1:]
+ [test_list[0]])] 

 

# printing result 

print("The Consecutive overlapping Summation : " + str(res))  
  
---  
  
 __

 __

  

**Output**

    
    
    The original list is : [4, 7, 3, 2, 9, 2, 1]
    The Consecutive overlapping Summation : [11, 10, 5, 11, 11, 3, 5]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

