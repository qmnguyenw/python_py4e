Python | Check if any String is empty in list



Sometimes, while working with Python, we can have a problem in which we need
to check for perfection of data in list. One of parameter can be that each
element in list is non-empty. Let’s discuss if a list is perfect on this
factor using certain methods.

 **Method #1 : Usingany() + len()**  
The combination of above functions can be used to perform this task. In this,
we use any() to check for any element in string and len() is used to get if
length of any string is 0 or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if any String is empty in list

# using len() + any()

 

# initialize list 

test_list = ['gfg', 'is', 'best', '', 'for',
'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Check if any String is empty in list

# using len() + any()

res = any(len(ele) == 0 for ele in test_list)

 

# printing result

print("Is any string empty in list? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', '', 'for', 'geeks']
    Is any string empty in list? : True
    

**Method #2 : Usingin operator**  
This task can also be performed using in operator. This checks internally for
all strings in list and returns True if we find any empty string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if any String is empty in list

# using in operator

 

# initialize list 

test_list = ['gfg', 'is', 'best', '', 'for',
'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Check if any String is empty in list

# using in operator

res = '' in test_list

 

# printing result

print("Is any string empty in list? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', '', 'for', 'geeks']
    Is any string empty in list? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

