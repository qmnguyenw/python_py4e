Python – Storing Elements Greater than K as Dictionary



Sometimes, while working with python lists, we can have a problem in which we
need to extract elements greater than K. But sometimes, we don’t require to
store duplicacy and hence store by key value pair in dictionary. To track of
number position of occurrence in dictionary.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we store
elements in form of dictionary by checking for elements greater than K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Storing Elements Greater than K as Dictionary

# using loop

 

# Initializing list

test_list = [12, 44, 56, 34, 67, 98, 34]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 50

 

# Storing Elements Greater than K as Dictionary

# using loop

res = dict()

count = 1

for ele in test_list:

 if ele > K:

 res[count] = ele

 count = count + 1

 

# printing result 

print ("The dictionary after storing elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [12, 44, 56, 34, 67, 98, 34]
    The dictionary after storing elements : {1: 56, 2: 67, 3: 98}
    

**Method #2 : Using dictionary comprehension**  
This is yet another way in which this task can be performed. In this, we just
perform similar task in a shorted construct using dictionary comprehension and
enumerate() for indexing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Storing Elements Greater than K as Dictionary

# using dictionary comprehension

 

# Initializing list

test_list = [12, 44, 56, 34, 67, 98, 34]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 50

 

# Storing Elements Greater than K as Dictionary

# using dictionary comprehension

res = {idx: ele for idx, ele in enumerate(test_list) if ele
>= K}

 

# printing result 

print ("The dictionary after storing elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [12, 44, 56, 34, 67, 98, 34]
    The dictionary after storing elements : {2: 56, 4: 67, 5: 98}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

