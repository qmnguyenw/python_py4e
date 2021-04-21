Python | Elements with Frequency equal K



This is one of the most essential operation that programmer quite often comes
in terms with. Be it development or competitive programming, this utility is
quite essential to master as it helps to perform many tasks that involve this
task to be its subtask. Lets discuss approach to achieve this operation.

 **Method #1 : Naive method**  
As the brute force method, we just count all the elements and then just return
the elements whose count equals K. This is the basic method that one could
think of executing when faced with this issue.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Elements with Frequency equal K

# using naive method

 

# initializing list

test_list = [9, 4, 5, 4, 4, 5, 9, 5]

 

# printing original list

print ("Original list : " + str(test_list))

 

# initializing K 

K = 3

 

# using naive method to 

# get most frequent element

res = []

for i in test_list:

 freq = test_list.count(i)

 if freq == K and i not in res:

 res.append(i)

 

# printing result

print ("Elements with count K are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [9, 4, 5, 4, 4, 5, 9, 5]
    Elements with count K are : [4, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

