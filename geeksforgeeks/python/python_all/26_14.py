Python – Dual Tuple Alternate summation



Given dual tuple, perform summation of alternate elements, i.e of indices
alternatively.

>  **Input** : test_list = [(4, 1), (5, 6), (3, 5), (7, 5)]  
> **Output** : 18  
> **Explanation** : 4 + 6 + 3 + 5 = 18, Alternatively are added to sum.
>
> **Input** : test_list = [(4, 1), (5, 6), (3, 5)]  
> **Output** : 13  
> **Explanation** : 4 + 6 + 3 = 183, Alternatively are added to sum.

**Method #1 : Using loop**

In this, we iterate through each tuple, and check for index in list, if even,
1st element of tuple is summed else 2nd is added to be computed sum.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dual Tuple Alternate summation

# Using loop

 

# initializing list

test_list = [(4, 1), (5, 6), (3, 5), (7,
5), (1, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = 0

for idx in range(len(test_list)):

 

 # checking for Alternate element

 if idx % 2 == 0:

 res += test_list[idx][0]

 else:

 res += test_list[idx][1]

 

# printing result

print("Summation of Alternate elements of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 1), (5, 6), (3, 5), (7, 5), (1, 10)]
    Summation of Alternate elements of tuples : 19
    
    

**Method #2 : Using list comprehension + sum()**

In this, we perform task of getting summation using _sum()_ , and list
comprehension is used to provide compact solution for iteration of tuples in
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

# Dual Tuple Alternate summation

# Using list comprehension + sum()

 

# initializing list

test_list = [(4, 1), (5, 6), (3, 5), (7,
5), (1, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# summation using sum(), list comprehension offers shorthand

res = sum([test_list[idx][0] if idx % 2 == 0 else
test_list[idx][1] for idx in range(len(test_list))])

 

# printing result 

print("Summation of Alternate elements of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 1), (5, 6), (3, 5), (7, 5), (1, 10)]
    Summation of Alternate elements of tuples : 19
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

