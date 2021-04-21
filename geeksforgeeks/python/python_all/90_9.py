Python – Double each List element



Sometimes, while working with data, we have just a simple application in which
we require to double the contents of a list and make it 100% increase in its
magnitude. This is having application in web development and machine learning
domains. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This the brute force way in which this task can be performed. In this, we just
add the same element again to that index element and all the contents of list
are added to itself i.e doubled.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Double List

# using loop

 

# Initializing list

test_list = [12, 67, 98, 34, 43]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Double List

# using loop

res = []

for ele in test_list:

 res.append(ele + ele)

 

# printing result 

print ("Double List is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [12, 67, 98, 34, 43]
    Double List is : [24, 134, 196, 68, 86]
    

**Method #2 : Using list comprehension**  
This task can also be performed using list comprehension. This is similar to
above function. Just the difference is that its compact and one liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Double List

# using list comprehension

 

# Initializing list

test_list = [12, 67, 98, 34, 43]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Double List

# using list comprehension

res = [ele + ele for ele in test_list]

 

# printing result 

print ("Double List is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [12, 67, 98, 34, 43]
    Double List is : [24, 134, 196, 68, 86]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

