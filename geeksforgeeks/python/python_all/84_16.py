Python – Remove leading 0 from Strings List



Sometimes, while working with Python, we can have a problem in which we have
data in which we need to perform processing and then pass the data forward.
One way to process is to remove a stray 0 that may get attached to a string
while data transfer. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usinglstrip() \+ list comprehension**  
This is one of the one liner with the help of which this task can be
performed. In this, we strip the leading 0 using lstrip and the extension of
logic to list is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove leading 0 from Strings List

# using lstrip() + list comprehension

 

# Initializing list

test_list = ['012', '03', '044', '09']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove leading 0 from Strings List

# using lstrip() + list comprehension

res = [ele.lstrip('0') for ele in test_list]

 

# printing result 

print ("The string list after leading 0 removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['012', '03', '044', '09']
    The string list after leading 0 removal : ['12', '3', '44', '9']
    

**Method #2 : Usingstartswith() \+ loop + list slicing**  
This is one of the way in which this task can be performed. In this, we check
for initial 0 using startswith() and then list slicing is used to remake
string excluding 0.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove leading 0 from Strings List

# using startswith() + loop + list slicing

 

# Initializing list

test_list = ['012', '03', '044', '09']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove leading 0 from Strings List

# using startswith() + loop + list slicing

for idx in range(len(test_list)):

 if test_list[idx].startswith('0'):

 test_list[idx] = test_list[idx][1:]

 

# printing result 

print ("The string list after leading 0 removal : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['012', '03', '044', '09']
    The string list after leading 0 removal : ['12', '3', '44', '9']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

