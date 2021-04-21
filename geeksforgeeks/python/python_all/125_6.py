Python | Convert tuple records to single string



Sometimes, while working with data, we can have a problem in which we have
tuple records and we need to change it’s to comma-separated strings. These can
be data regarding names. This kind of problem has its application in the web
development domain. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Usingjoin() \+ list comprehension**  
In this method, we just iterate through the list tuple elements and perform
the join among them separated by spaces to join them as a single string of
records.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple records to single string

# Using list comprehension + join()

 

# Initializing list

test_list = [('Manjeet', 'Singh'), ('Nikhil',
'Meherwal'), ('Akshat', 'Garg')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert tuple records to a single string

# Using list comprehension + join()

res = ', '.join([' '.join(sub) for sub in test_list])

 

# printing result

print("The string after tuple conversion: " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Manjeet', 'Singh'), ('Nikhil', 'Meherwal'), ('Akshat', 'Garg')]
    The string after tuple conversion: Manjeet Singh, Nikhil Meherwal, Akshat Garg
    

**Method #2 : Usingmap() + join()**  
This method performs this task similar to the above function. The difference
is just that it uses map() for extending join logic rather than list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple records to single string

# Using map() + join()

 

# Initializing list

test_list = [('Manjeet', 'Singh'), ('Nikhil',
'Meherwal'), ('Akshat', 'Garg')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert tuple records to a single string

# Using map() + join()

res = ', '.join(map(" ".join, test_list))

 

# printing result

print("The string after tuple conversion: " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Manjeet', 'Singh'), ('Nikhil', 'Meherwal'), ('Akshat', 'Garg')]
    The string after tuple conversion: Manjeet Singh, Nikhil Meherwal, Akshat Garg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

