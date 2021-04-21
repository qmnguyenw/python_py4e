Python – Convert Uneven Lists into Records



Sometimes, while working with Records, we can have a problem, that we have
keys in one list and values in other. But sometimes, values can be multiple in
order, like the scores or marks of particular subject. This type of problem
can occur in school programming and development domains. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : Using dictionary comprehension +enumerate() \+ list slicing**  
The combination of above functions can be used to solve this problem. In this,
we iterate using dictionary comprehension and enumerate and form desired
result by extracting records values by slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Uneven Lists into Records

# Using dictionary comprehension + enumerate() + list slicing

 

# initializing lists

test_list1 = ['Nikhil', 'Akash', 'Akshat']

test_list2 = [5, 6, 7, 8, 2, 3, 12, 2,
10]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Convert Uneven Lists into Records

# Using dictionary comprehension + enumerate() + list slicing

temp = len(test_list2) // len(test_list1)

res = {key: test_list2[idx :: temp] for idx, key in
enumerate(test_list1)}

 

# printing result 

print("The paired data dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [‘Nikhil’, ‘Akash’, ‘Akshat’]  
> The original list 2 is : [5, 6, 7, 8, 2, 3, 12, 2, 10]  
> The paired data dictionary : {‘Nikhil’: [5, 8, 12], ‘Akshat’: [7, 3, 10],
> ‘Akash’: [6, 2, 2]}

  

  

**Method #2 : Using list comprehension +zip()**  
This task can also be solved using above functions. In this, we use list
comprehension to construct the cumulated score list. In last step we tie both
lists together using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Uneven Lists into Records

# Using list comprehension + zip()

 

# initializing lists

test_list1 = ['Nikhil', 'Akash', 'Akshat']

test_list2 = [5, 6, 7, 8, 2, 3, 12, 2,
10]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Convert Uneven Lists into Records

# Using list comprehension + zip()

temp = len(test_list2) // len(test_list1)

res = [test_list2[idx :: temp] for idx in range(0,
len(test_list1))]

res = dict(zip(test_list1, res))

 

# printing result 

print("The paired data dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [‘Nikhil’, ‘Akash’, ‘Akshat’]  
> The original list 2 is : [5, 6, 7, 8, 2, 3, 12, 2, 10]  
> The paired data dictionary : {‘Nikhil’: [5, 8, 12], ‘Akshat’: [7, 3, 10],
> ‘Akash’: [6, 2, 2]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

