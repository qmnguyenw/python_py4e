Python – Pair lists elements to Dictionary



Sometimes, while working with records we can have problem in which we can have
pair of lists, we need to pair similar like elements to single key value
dictionary. This is very peculiar problem but can have applications in data
domains. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +extend() + enumerate()**  
The combination of above functionalities can be employed to solve this
question. In this, we iterate for the lists and append like elements to
similar key using extend().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair lists elements to Dictionary

# Using loop + extend() + enumerate()

 

# initializing lists

test_list1 = [1, 2, 3, 1, 1, 2, 3]

test_list2 = [[4, 5], [6, 7], [2, 3], [10,
12], 

 [56, 43], [98, 100], [0, 13]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Pair lists elements to Dictionary

# Using loop + extend() + enumerate()

res = dict()

for idx, val in enumerate(test_list1):

 if val in res:

 res[val].extend(list(test_list2[idx]))

 else:

 res[val] = list(test_list2[idx])

 

# printing result 

print("The Like elements compiled Dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [1, 2, 3, 1, 1, 2, 3]  
> The original list 2 is : [[4, 5], [6, 7], [2, 3], [10, 12], [56, 43], [98,
> 100], [0, 13]]  
> The Like elements compiled Dictionary is : {1: [4, 5, 10, 12, 56, 43], 2:
> [6, 7, 98, 100], 3: [2, 3, 0, 13]}

  

  

**Method #2 : Usingdefaultdict() + zip()**  
The combination of above tasks can also be used to solve this problem. In
this, we pair elements using zip() and initialize the dictionary values as a
list to avoid testing for existance of first value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair lists elements to Dictionary

# Using defaultdict() + zip()

from collections import defaultdict

 

# initializing lists

test_list1 = [1, 2, 3, 1, 1, 2, 3]

test_list2 = [[4, 5], [6, 7], [2, 3], [10,
12], 

 [56, 43], [98, 100], [0, 13]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Pair lists elements to Dictionary

# Using defaultdict() + zip()

res = defaultdict(list)

for ele1, ele2 in zip(test_list1, test_list2):

 res[ele1].extend(ele2)

 

# printing result 

print("The Like elements compiled Dictionary is : " +
str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [1, 2, 3, 1, 1, 2, 3]  
> The original list 2 is : [[4, 5], [6, 7], [2, 3], [10, 12], [56, 43], [98,
> 100], [0, 13]]  
> The Like elements compiled Dictionary is : {1: [4, 5, 10, 12, 56, 43], 2:
> [6, 7, 98, 100], 3: [2, 3, 0, 13]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

