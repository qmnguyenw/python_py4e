Python – Test Common Elements Order



Sometimes, while working with lists, we can have a problem in which we need to
test if list containes common elements. This type of problem has been dealt
many times and has lot of solutions. But sometimes, we might have a problem in
which we need to check that those common elements appear in same order in both
list or not. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +set()**  
The combination of above functions can be used to perform this task. In this,
we iterate through the lists and check using conditions of we have in order
common elements or not. The duplication removal is performed using set().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test Common Elements Order

# using loop + set()

 

# helper function

def common_ord(test_list1, test_list2):

 comm = set(test_list1)

 comm.intersection_update(test_list2)

 pr_idx = 0

 for ele in test_list1:

 if ele in comm:

 try:

 pr_idx = test_list2.index(ele, pr_idx)

 except ValueError:

 return False

 return True

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'for', 'Geeks']

test_list2 = [1, 'Gfg', 2, 'Geeks']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Test Common Elements Order

# using loop + set()

res = common_ord(test_list1, test_list2)

 

# printing result 

print ("Are common elements in order ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['Gfg', 'is', 'for', 'Geeks']
    The original list 2 is : [1, 'Gfg', 2, 'Geeks']
    Are common elements in order ? : True
    

**Method #2 : Using list comprehension +set()**  
The combination of above functions perform the task in similar way. The
difference is that we use shorter constructs as compared to upper method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test Common Elements Order

# using list comprehension + set()

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'for', 'Geeks']

test_list2 = [1, 'Gfg', 2, 'Geeks']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Test Common Elements Order

# using list comprehension + set()

temp = set(test_list1) & set(test_list2)

temp1 = [val for val in test_list1 if val in temp]

temp2 = [val for val in test_list2 if val in temp]

res = temp1 == temp2

 

# printing result 

print ("Are common elements in order ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['Gfg', 'is', 'for', 'Geeks']
    The original list 2 is : [1, 'Gfg', 2, 'Geeks']
    Are common elements in order ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

