Python | Test if all elements are present in list



Sometimes, while working with Python list, we have a problem in which we need
to check for a particular list of values and want to be sure if a target list
contains all the given values. This has it’s application in web development
domain when required some type of filtering. Let’s discuss a way in which this
task can be performed.

 **Method : Using list comprehension +all()**  
This task can be performed using the inbuilt functionality of all(). The all()
can be fed with list comprehension logic to check if element of test list is
present in target list and rest is done by all().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all elements are present in list

# Using list comprehension + all()

 

# initializing list

target_list = [6, 4, 8, 9, 10]

 

# initializing test list 

test_list = [4, 6, 9]

 

# printing lists

print("The target list : " + str(target_list))

print("The test list : " + str(test_list))

 

# Test if all elements are present in list

# Using list comprehension + all()

res = all(ele in target_list for ele in test_list)

 

# Printing result

print("Does every element of test_list is in target_list ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The target list : [6, 4, 8, 9, 10]
    The test list : [4, 6, 9]
    Does every element of test_list is in target_list ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

