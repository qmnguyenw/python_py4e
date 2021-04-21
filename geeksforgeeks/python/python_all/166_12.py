Python | Return new list on element insertion



The usual append method adds the new element in the original sequence and does
not return any value. But sometimes we require to have a new list each time we
add a new element to the list. This kind of problem is common in web
development. Let’s discuss certain ways in which this task can be performed.  

 **Method #1 : Using + operator**  
This task can be performed if we make a single element list and concatenate
original list with this newly made single element list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# returning new list on element insertion

# using + operator

 

# initializing list

test_list = [5, 6, 2, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# element to add 

K = 10

 

# using + operator

# returning new list on element insertion

res = test_list + [K]

 

# printing result 

print ("The newly returned added list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 2, 3, 9]
    The newly returned added list : [5, 6, 2, 3, 9, 10]
    

  
**Method #2 : Using * operator**  
Similar kind of task can be used using * operator in which we use * operator
to take all the elements and also add the new element to output the new list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# returning new list on element insertion

# using * operator

 

# initializing list

test_list = [5, 6, 2, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# element to add 

K = 10

 

# using * operator

# returning new list on element insertion

res = [*test_list, K]

 

# printing result 

print ("The newly returned added list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 2, 3, 9]
    The newly returned added list : [5, 6, 2, 3, 9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

