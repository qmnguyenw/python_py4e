Python – Group Sublists by another List



Sometimes, while working with lists, we can have a problem in which we need to
group all the sublists, separated by elements present in different list. This
type of custom grouping is uncommon utility but having solution to these can
always be handy. Lets discuss certain way in which this task can be performed.

 **Method #1 : Using loop + generator(yield)**  
This is brute force way in which this task can be performed. In this, we
iterate the list and make groups dynamically using yield. We keep track of
elements occurred and restart list when we find element in second list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group Sublists by another List

# using loop + generator(yield)

 

# helper function

def grp_ele(test_list1, test_list2):

 temp = []

 for i in test_list1: 

 if i in test_list2:

 if temp: 

 yield temp 

 temp = []

 yield i 

 else: 

 temp.append(i)

 if temp: 

 yield temp

 

# Initializing lists

test_list1 = [8, 5, 9, 11, 3, 7]

test_list2 = [9, 11]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Group Sublists by another List

# using loop + generator(yield)

res = list(grp_ele(test_list1, test_list2))

 

# printing result 

print ("The Grouped list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [8, 5, 9, 11, 3, 7]
    The original list 2 is : [9, 11]
    The Grouped list is : [[8, 5], 9, 11, [3, 7]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

