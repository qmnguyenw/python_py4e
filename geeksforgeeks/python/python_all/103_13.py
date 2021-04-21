Python | Records with Key’s value greater than K



The problem of getting the suitable dictionaries that has a atleast value of
the corresponding key is quite common when one starts working with dictionary.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is the brute force method by which this task can be performed. For this,
we just use naive check and compare and append the records which have a
particular key’s value greater than K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records with Key's value greater than K

# Using loop

 

# Initialize list

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6}, 

 {'it' : 5, 'is' : 7, 'best' : 8},

 {'CS' : 10, 'is' : 8, 'best' : 10}]

 

# Printing original list

print("The original list is : " + str(test_list))

 

# Initialize K 

K = 6

 

# Using loop

# Records with Key's value greater than K

res = []

for sub in test_list:

 if sub['is'] >= K:

 res.append(sub)

 

# printing result 

print("The filtered dictionary records is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [{'best': 6, 'gfg': 2, 'is': 4}, {'best': 8, 'it': 5, 'is': 7}, {'best': 10, 'CS': 10, 'is': 8}]
    The filtered dictionary records is : [{'best': 8, 'it': 5, 'is': 7}, {'best': 10, 'CS': 10, 'is': 8}]
    

**Method #2 : Usinglist() \+ dictionary comprehension**  
The combination of these methods can also be used to perform this task. This
difference is that it’s a one liner and more efficient as list function uses
iterator as internal implementation which are quicker than generic methods.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find dictionary matching value in list

# Using list() + dictionary comprehension

 

# Initialize list

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6}, 

 {'it' : 5, 'is' : 7, 'best' : 8},

 {'CS' : 10, 'is' : 8, 'best' : 10}]

 

# Printing original list

print("The original list is : " + str(test_list))

 

# Initialize K 

K = 6

 

# Using list() + dictionary comprehension

# Find dictionary matching value in list

res = list((sub for sub in test_list if sub['is'] >=
K))

 

# printing result 

print("The filtered dictionary records : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [{'best': 6, 'gfg': 2, 'is': 4}, {'best': 8, 'it': 5, 'is': 7}, {'best': 10, 'CS': 10, 'is': 8}]
    The filtered dictionary records is : [{'best': 8, 'it': 5, 'is': 7}, {'best': 10, 'CS': 10, 'is': 8}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

