Python – Compare Unordered Dictionary List



Sometimes, while working with Records, we can have problem in which we need to
perform the comparison between records. This can be of type list of
dictionaries, if they are equal or not. This has applications in many domains.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using"==" operator ( Only keys Unordered )**  
For the case in which just the keys of dictionaries are unordered, and the
ordering in list is in correct way, the test can be done using “==” operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Compare Unordered Dictionary List

# Using "==" operator

 

# initializing lists

test_list1 = [{'Manjeet' : 12, 'Himani' : 15},
{'Akshat' : 20, 'Vashu' : 15}]

test_list2 = [{'Himani' : 15, 'Manjeet' : 12},
{'Vashu' : 15, 'Akshat' : 20}]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Compare Unordered Dictionary List

# Using "==" operator

res = test_list1 == test_list2

 

# printing result 

print("Are Dictionary Lists equal ? : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [{‘Himani’: 15, ‘Manjeet’: 12}, {‘Akshat’: 20,
> ‘Vashu’: 15}]  
> The original list 2 is : [{‘Himani’: 15, ‘Manjeet’: 12}, {‘Vashu’: 15,
> ‘Akshat’: 20}]  
> Are Dictionary Lists equal ? : True

  

  

**Method #2 : Usingsorted() \+ key + lambda ( In case of Unordered keys and
list position )**  
The combination of above functions can also be used to solve this problem. In
this, we perform the task of sorting to resolve the list positioning and then
compare.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Compare Unordered Dictionary List

# Using sorted() + key + lambda

 

# initializing lists

test_list1 = [{'Manjeet' : 12, 'Himani' : 15},
{'Akshat' : 20, 'Vashu' : 15}]

test_list2 = [{'Vashu' : 15, 'Akshat' : 20}, {'Himani'
: 15, 'Manjeet' : 12}]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Compare Unordered Dictionary List

# Using sorted() + key + lambda

res = sorted(test_list1, key = lambda ele:
sorted(ele.items())) == sorted(

 test_list2, key = lambda ele: sorted(ele.items()))

 

# printing result 

print("Are Dictionary Lists equal ? : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [{‘Himani’: 15, ‘Manjeet’: 12}, {‘Akshat’: 20,
> ‘Vashu’: 15}]  
> The original list 2 is : [{‘Himani’: 15, ‘Manjeet’: 12}, {‘Vashu’: 15,
> ‘Akshat’: 20}]  
> Are Dictionary Lists equal ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

