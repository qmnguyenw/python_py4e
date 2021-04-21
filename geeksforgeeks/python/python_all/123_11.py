Python | Test if element is dictionary value



Sometimes, while working with Python dictionary, we have a specific use case
in which we just need to find if a particular value is present in dictionary
as it’s any key’s value. This can have use cases in any field of programming
one can think of. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Using loop**  
This is the brute way in which this problem can be solved. In this, we iterate
through the whole dictionary using loops and check for each keys’ value’s for
a match using conditional statement.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if element is dictionary value

# Using loops

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Test if element is dictionary value

# Using loops

res = False

for key in test_dict:

 if(test_dict[key] == 3):

 res = True

 break

 

# printing result

print("Is 3 present in dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'is': 2, 'gfg': 1}
    Is 3 present in dictionary : True
    

**Method #2 : Usingin operator and values()**  
This task can be performed by utilizing above functionalities. The in
operator can be used to get the truth value of presence and values function
is required to extract all values of dictionaries.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if element is dictionary value

# Using in operator and values()

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Test if element is dictionary value

# Using in operator and values()

res = 3 in test_dict.values()

 

# printing result

print("Is 3 present in dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'is': 2, 'gfg': 1}
    Is 3 present in dictionary : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

