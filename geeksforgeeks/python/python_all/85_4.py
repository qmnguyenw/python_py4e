Python – Sum of each List element occurrence in another



Sometimes, while working with Python, we can have a problem in which we need
to get occurrence of 1 element in another. But as a modification of this, we
can have a problem in which we need to count the occurrence of all elements of
1 list in another. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using nested loops**  
This is one of the way in which this task can be performed. This is brute
force way in which this task can be performed. In this, we iterate one list
and then target list, if element match, we increase the counter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sum of each List element occurrence in another

# using nested loops

 

# Initializing lists

test_list1 = [1, 3, 4, 5, 1, 4, 4, 6,
7]

test_list2 = [4, 6, 1]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Sum of each List element occurrence in another

# using nested loops

res = 0

for ele in test_list2:

 for ele1 in test_list1:

 if ele1 == ele:

 res = res + 1

 

# printing result 

print ("The occurrence count : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 4, 5, 1, 4, 4, 6, 7]
    The original list 2 is : [4, 6, 1]
    The occurrence count : 6
    

**Method #2 : Usingsum() + count()**  
The combination of above methods can be used to perform this particular task.
This is one liner alternative to the above method. In this counting is done
using count() and accumulation using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sum of each List element occurrence in another

# using sum() + count()

 

# Initializing lists

test_list1 = [1, 3, 4, 5, 1, 4, 4, 6,
7]

test_list2 = [4, 6, 1]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Sum of each List element occurrence in another

# using sum() + count()

res = sum(test_list1.count(idx) for idx in test_list2)

 

# printing result 

print ("The occurrence count : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 4, 5, 1, 4, 4, 6, 7]
    The original list 2 is : [4, 6, 1]
    The occurrence count : 6
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

