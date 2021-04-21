Python – Custom dictionary initialization in list



While working with Python, we can have a problem in which we need to
initialize a list of a particular size with custom dictionaries. This task has
it’s utility in web development to store records. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using{dict} + "*" operator**  
This task can be performed using the “*” operator. We can create a list
containing single custom dictionary and then multiply it by Number that is
size of list. The drawback is that similar reference dictionaries will be made
which will point to similar memory location.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom dictionary initialization in list

# using {dict} + "*" operator

 

# Initialize dict 

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# Custom dictionary initialization in list

# using {dict} + "*" operator

res = [test_dict] * 6

 

print("The list of custom dictionaries is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list of custom dictionaries is : [{'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}]
    

**Method #2 : Using {dict} + list comprehension**  
This is perhaps the better and correct way to perform this task. We initialize
the each index of list with dictionary, this way, we have independently
referring dictionaries and don’t point to single reference.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom dictionary initialization in list

# using {dict} + list comprehension

 

# Initialize dict 

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# Custom dictionary initialization in list

# using {dict} + list comprehension

res = [test_dict for sub in range(6)]

 

print("The list of custom dictionaries is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list of custom dictionaries is : [{'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}, {'gfg': 1, 'best': 3, 'is': 2}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

