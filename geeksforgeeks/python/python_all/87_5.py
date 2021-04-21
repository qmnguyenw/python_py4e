Python – Elements frequency count in multiple lists



Sometimes while working with Python lists we can have a problem in which we
need to extract the frequency of elements in list. But this can be added work
if we have more than 1 list we work on. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using dictionary comprehension +set() + count()**  
This is one of the way in which this task can be performed. In this, we
perform the task of counting using count() and set() and the extension of
logic is done using dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Elements frequency count in multiple lists

# using set() + count() + dictionary comprehension

 

# Initializing lists

test_list1 = [1, 3, 2, 4, 5, 1, 2]

test_list2 = [4, 1, 4, 3, 4, 2, 4]

test_list3 = [1, 4, 5, 3, 4, 5, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# Elements frequency count in multiple lists

# using set() + count() + dictionary comprehension

res = {idx : [test_list1.count(idx), test_list2.count(idx),
test_list3.count(idx)]

 for idx in set(test_list1 + test_list2 + test_list3)}

 

# printing result 

print ("The frequency of each element is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [1, 3, 2, 4, 5, 1, 2]  
> The original list 2 is : [4, 1, 4, 3, 4, 2, 4]  
> The original list 3 is : [1, 4, 5, 3, 4, 5, 4]  
> The frequency of each element is : {1: [2, 1, 1], 2: [2, 1, 0], 3: [1, 1,
> 1], 4: [1, 4, 3], 5: [1, 0, 2]}

  

  

**Method #2 : UsingCounter() + map() \+ dictionary comprehension**  
The combination of above functionalities can be used to solve this problem. In
this, the task of finding the frequency is done using Counter() and map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Elements frequency count in multiple lists

# using map() + Counter() + dictionary comprehension

from collections import Counter

 

# Initializing lists

test_list1 = [1, 3, 2, 4, 5, 1, 2]

test_list2 = [4, 1, 4, 3, 4, 2, 4]

test_list3 = [1, 4, 5, 3, 4, 5, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# Elements frequency count in multiple lists

# using map() + Counter() + dictionary comprehension

freq = list(map(Counter, (test_list1, test_list2, test_list3)))

res = {ele: [cnt[ele] for cnt in freq] for ele in {ele
for cnt in freq for ele in cnt}}

 

# printing result 

print ("The frequency of each element is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [1, 3, 2, 4, 5, 1, 2]  
> The original list 2 is : [4, 1, 4, 3, 4, 2, 4]  
> The original list 3 is : [1, 4, 5, 3, 4, 5, 4]  
> The frequency of each element is : {1: [2, 1, 1], 2: [2, 1, 0], 3: [1, 1,
> 1], 4: [1, 4, 3], 5: [1, 0, 2]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

