Python – Diagonal element addition among lists



Sometimes, while working with Python lists, we can have a problem in which we
need to perform addition of lists in diagonal manner that i.e. adding ith
element of 1 list to i + 1 element of other list. This kind of problem can
have application in day-day programming. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate one list and test add the i + 1th element of other list and construct
the resultant list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Diagonal element addition among lists

# using loop

 

# Initializing lists

test_list1 = [1, 6, 8, 5, 3]

test_list2 = [8, 10, 3, 4, 5]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Diagonal element addition among lists

# using loop

res = []

for idx in range(0, len(test_list1) - 1):

 res.append(test_list1[idx] + test_list2[idx + 1])

 

# printing result 

print ("List after diagonal addition : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 6, 8, 5, 3]
    The original list 2 is : [8, 10, 3, 4, 5]
    List after diagonal addition : [11, 9, 12, 10]
    

**Method #2 : Using zip() \+ list comprehension**  
This is yet another way in which this task can be performed. In this, we group
ith with i+1th element of other list using zip(). The task of performing
addition is done in list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Diagonal element addition among lists

# using zip() + list comprehension

 

# Initializing lists

test_list1 = [1, 6, 8, 5, 3]

test_list2 = [8, 10, 3, 4, 5]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Diagonal element addition among lists

# using zip() + list comprehension

res = [i + j for i, j in zip(test_list1,
test_list2[1:])]

 

# printing result 

print ("List after diagonal addition : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 6, 8, 5, 3]
    The original list 2 is : [8, 10, 3, 4, 5]
    List after diagonal addition : [11, 9, 12, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

