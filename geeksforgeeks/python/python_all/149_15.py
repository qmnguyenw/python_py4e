Python | Extract numbers from list of strings



Sometimes, we can data in many forms and we desire to perform both conversions
and extractions of certain specific parts of a whole. One such issue can be
extracting a number from a string and extending this, sometimes it can be more
than just an element string but a list of it. Let’s discuss certain ways in
which this can be solved.

 **Method #1 : Using list comprehension +split()**

This particular problem can be solved using the list comprehension function to
extend the logic to all the items and split function performs the task of
splitting and to fetch the target desired element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Extracting numbers from list of strings

# using list comprehension + split()

 

# initializing list

test_list = ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + split()

# Extracting numbers from list of strings

res = [int(sub.split('.')[1]) for sub in test_list]

 

# print result

print("The list after Extracting numbers : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']
    The list after Extracting numbers : [24, 18, 8, 21]
    

  

  

**Method #2 : Usingjoin() + isnumeric() \+ list comprehension + map()**

This method is preferred in the instances in which it is not predefined that
the numbers will be ordered in a particular way i.e, this method gives the
flexibility of getting the number from whichever position possible.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Extracting numbers from list of strings

# using join() + isnumeric() + list comprehension + map()

 

# initializing list

test_list = ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']

 

# printing original list

print("The original list : " + str(test_list))

 

# using join() + isnumeric() + list comprehension + map()

# Extracting numbers from list of strings

res = list(map(lambda sub:int(''.join(

 [ele for ele in sub if ele.isnumeric()])), test_list))

 

# print result

print("The list after Extracting numbers : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']
    The list after Extracting numbers : [24, 18, 8, 21]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

