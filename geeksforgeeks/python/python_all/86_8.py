Python – Group similar value list to dictionary



Sometimes, while working with Python list, we can have a problem in which we
need to group similar value lists indices to values into a dictionary. This
can have a good application in domains in which we need grouped dictionary as
output for pair of lists. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using dictionary comprehension**  
This is way in which this task can be performed. In this, we iterate one list
along with other and keep constructing dictionary with similar key from one
list and corresponding values from other. This is one liner solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group similar value list to dictionary

# using dictionary comprehension

 

# Initializing lists

test_list1 = [4, 4, 4, 5, 5, 6, 6, 6,
6]

test_list2 = ['G', 'f', 'g', 'i', 's', 'b',
'e', 's', 't']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Group similar value list to dictionary

# using dictionary comprehension

res = {key : [test_list2[idx] 

 for idx in range(len(test_list2)) if
test_list1[idx]== key]

 for key in set(test_list1)}

 

# printing result 

print ("Mapped resultant dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [4, 4, 4, 5, 5, 6, 6, 6, 6]  
> The original list 2 is : [‘G’, ‘f’, ‘g’, ‘i’, ‘s’, ‘b’, ‘e’, ‘s’, ‘t’]  
> Mapped resultant dictionary : {4: [‘G’, ‘f’, ‘g’], 5: [‘i’, ‘s’], 6: [‘b’,
> ‘e’, ‘s’, ‘t’]}

  

  

**Method #2 : Usingdefaultdict() \+ loop**  
This is yet another way in which this task can be performed. In this we avoid
testing for keys presence in dictionary by creating a defaultdict().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group similar value list to dictionary

# using defaultdict() + loop

from collections import defaultdict

 

# Initializing lists

test_list1 = [4, 4, 4, 5, 5, 6, 6, 6,
6]

test_list2 = ['G', 'f', 'g', 'i', 's', 'b',
'e', 's', 't']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Group similar value list to dictionary

# using defaultdict() + loop

res = defaultdict(set)

for key, val in zip(test_list1, test_list2):

 res[key].add(val)

res = {key: list(val) for key, val in res.items()}

 

# printing result 

print ("Mapped resultant dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [4, 4, 4, 5, 5, 6, 6, 6, 6]  
> The original list 2 is : [‘G’, ‘f’, ‘g’, ‘i’, ‘s’, ‘b’, ‘e’, ‘s’, ‘t’]  
> Mapped resultant dictionary : {4: [‘G’, ‘f’, ‘g’], 5: [‘i’, ‘s’], 6: [‘b’,
> ‘e’, ‘s’, ‘t’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

