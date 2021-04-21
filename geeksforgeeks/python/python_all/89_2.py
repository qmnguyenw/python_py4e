Python – Conditional String Append



Sometimes, while working with data, we have a problem in which we need to
perform append operation in string on a particular condition. This kind of
problem is common in web development and day-day programming. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way to perform this task. In this, we run a loop and check
for the condition and according to that append the string to original string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Conditional String Append

# using loop

 

def append_str(item, boy_str, girl_str):

 if len(item) > 4 and item[-5] == ' ':

 return item + girl_str

 return item + boy_str

 

# initializing list 

test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet
Kaur']

 

# initializing append string 

boy_str = " Boy"

girl_str = " Girl"

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Conditional String Append

# using loop

res = [append_str(item, boy_str, girl_str) for item in
test_list]

 

# printing result 

print ("The filtered strings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
    The filtered strings are : ['Manjeet Singh Boy', 'Harsimran Kaur Girl', 'Sarbjeet Kaur Girl']
    

**Method #2 : Using list comprehension**  
List comprehension is shorthand to longer method of loops. This solved problem
in similar way but in shorter constructs.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Conditional String Append

# using list comprehension

 

# initializing list 

test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet
Kaur']

 

# initializing append string 

boy_str = " Boy"

girl_str = " Girl"

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Conditional String Append

# using list comprehension

res = [ele + girl_str if ele[-5] == ' ' else ele
+ boy_str for ele in test_list]

 

# printing result 

print ("The filtered strings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
    The filtered strings are : ['Manjeet Singh Boy', 'Harsimran Kaur Girl', 'Sarbjeet Kaur Girl']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

