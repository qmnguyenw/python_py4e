Python – Multiply two list



There can be many situations in which one requires to find index wise product
of two different lists. This can have a possible applications in day-day
programming. Lets discuss various ways in which this task can be performed.

 **Method #1 : Naive Method**  
In this method, we simply run a loop and append to the new list the product of
the both list elements at similar index till we reach end of the smaller list.
This is the basic method to achieve this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Multiplying two lists

# naive method 

 

# initializing lists

test_list1 = [1, 3, 4, 6, 8]

test_list2 = [4, 5, 6, 2, 10]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using naive method to 

# Multiplying two lists

res_list = []

for i in range(0, len(test_list1)):

 res_list.append(test_list1[i] * test_list2[i])

 

# printing resultant list 

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list 1 : [1, 3, 4, 6, 8]
    Original list 2 : [4, 5, 6, 2, 10]
    Resultant list is : [4, 15, 24, 12, 80]
    

**Method #2 : Using List Comprehension**  
The shorthand for the above explained technique, list comprehensions are
usually quicker to type and hence must be preferred to perform these kind of
programming tasks.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Multiplying two lists

# list comprehension

 

# initializing lists

test_list1 = [1, 3, 4, 6, 8]

test_list2 = [4, 5, 6, 2, 10]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using list comprehension to 

# Multiplying two lists

res_list = [test_list1[i] * test_list2[i] for i in
range(len(test_list1))]

 

# printing resultant list 

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list 1 : [1, 3, 4, 6, 8]
    Original list 2 : [4, 5, 6, 2, 10]
    Resultant list is : [4, 15, 24, 12, 80]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

