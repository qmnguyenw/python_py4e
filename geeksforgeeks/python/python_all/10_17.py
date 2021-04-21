Python program to print elements which are multiples of elements given in a
list



Given a list, the task here is to write a Python program to extract elements
which are multiple of all elements of custom list.

>  **Input** : test_list = [4, 24, 8, 10, 12, 23], div_list = [6, 4]  
> **Output** : [24, 12]  
> **Explanation** : 24 and 12 divides 6 and 4 both.
>
>  **Input** : test_list = [4, 24, 8, 10, 12, 23], div_list = [6, 4, 7]  
> **Output** : []  
> **Explanation** : No elements divides 6, 4 and 7.

**Method 1:** Using list comprehension and all()

In this, we perform task of checking for all elements to be multiple using %
operator and all(). List comprehension is used to iterate through all the
elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing List

test_list = [4, 24, 8, 10, 12, 23]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing divisor list

div_list = [6, 4]

 

# using all() to test for all elements

res = [ele for ele in test_list if all(ele % j ==
0 for j in div_list)]

 

# printing result

print("All elements multiple of divisor list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 24, 8, 10, 12, 23]
>
> All elements multiple of divisor list : [24, 12]

 **Method 2:** Using filter(), lambda and all()

In this, we perform task of filtering using filter() and lambda, rest all the
operations are performed like above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing List

test_list = [4, 24, 8, 10, 12, 23]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing divisor list

div_list = [6, 4]

 

# using all() to test for all elements

# using filter() and lambda to perform filtering

res = list(filter(lambda ele: all(ele % j == 0
for j in div_list), test_list))

 

# printing result

print("All elements multiple of divisor list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 24, 8, 10, 12, 23]
>
> All elements multiple of divisor list : [24, 12]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

