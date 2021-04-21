Python – Words with Particular Rear letter



Sometimes, we require to get the words that end with the specific letter. This
kind of use case is quiet common in the places of common programming projects
or competitive programming. Let’s discuss certain shorthands to deal with this
problem in Python.

 **Method #1 : Using list comprehension +lower()**  
This problem can be solved using the combination of above two functions, list
comprehension performs the task of extending the logic to whole list and lower
function checks for case insensitivity with the target word of argument
letter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Words with Particular Rear letter

# using list comprehension + lower()

 

# initializing list

test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']

 

# initializing check letter

check = 'T'

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + lower()

# Words with Particular Rear letter

res = [idx for idx in test_list if idx[len(idx) -
1].lower() == check.lower()]

 

# print result

print("The list of matching last letter : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Akash', 'Nikhil', 'Manjeet', 'akshat']
    The list of matching last letter : ['Manjeet', 'akshat']
    

**Method #2 : Using list comprehension +endswith() + lower()**  
This method is similar to the above method but rather than checking for
equality with operator, it checks using the endswith function which is inbuilt
provided by python inbuilt library.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Words with Particular Rear letter

# using list comprehension + endswith() + lower()

 

# initializing list

test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']

 

# initializing check letter

check = 'T'

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + endswith() + lower()

# Words with Particular Rear letter

res = [idx for idx in test_list if
idx.lower().endswith(check.lower())]

 

# print result

print("The list of matching last letter : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Akash', 'Nikhil', 'Manjeet', 'akshat']
    The list of matching last letter : ['Manjeet', 'akshat']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

