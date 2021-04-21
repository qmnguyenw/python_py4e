Python | Lead and Trail padding of strings list



Sometimes, while working with string lists, we can have a problem in which we
need to pad each string in list with a particular string. This type of problem
can come in many places in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension**

This task can be performed using list comprehension. In this, we iterate each
string element and reconstruct a new string list after adding required string
at rear and front of each string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Trail and lead padding of strings list

# using list comprehension

 

# initialize list 

test_list = ["a", "b", "c"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize pad_str

pad_str = 'gfg'

 

# Trail and lead padding of strings list

# using list comprehension

res = [pad_str + ele + pad_str for ele in test_list]

 

# printing result

print("The String list after padding : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['a', 'b', 'c']
    The String list after padding : ['gfgagfg', 'gfgbgfg', 'gfgcgfg']
    

  

  

**Method #2: Using list comprehension + string formatting**

This task can also be performed using a combination of above functionalities.
In this, we perform the task of padding using formatted string than +
operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Trail and lead padding of strings list

# using list comprehension + string formatting

 

# initialize list 

test_list = ["a", "b", "c"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize pad_str

pad_str = 'gfg'

 

# Trail and lead padding of strings list

# using list comprehension + string formatting

temp = pad_str + '{0}' + pad_str

res = [temp.format(ele) for ele in test_list]

 

# printing result

print("The String list after padding : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['a', 'b', 'c']
    The String list after padding : ['gfgagfg', 'gfgbgfg', 'gfgcgfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

