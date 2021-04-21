Python | Even values update in dictionary



Sometimes, while working with dictionaries, we might come across a problem in
which we require to perform a particular operation on even value of keys. This
type of problem can occur in web development domain. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is the naive method in which this task can be performed. In this we
simply run a loop to traverse each key and check for even in dictionary and
perform the desired operation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Even values update in dictionary

# Using loop

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using loop

# Even values update in dictionary

for key in test_dict: 

 if test_dict[key] % 2 == 0:

 test_dict[key] *= 3

 

# printing result 

print("The dictionary after triple even key's value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'best': 7, 'is': 4, 'gfg': 6}
    The dictionary after triple even key's value : {'best': 7, 'is': 12, 'gfg': 18}
    

**Method #2 : Usingupdate() \+ dictionary comprehension**  
An alternate one-liner to perform this task, the combination of above
functions can be used to perform this particular task. The update function is
used to perform the necessary operation over the dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Even values update in dictionary

# Using update() + dictionary comprehension

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using update() + dictionary comprehension

# Even values update in dictionary

test_dict.update((x, y * 3) for x, y in test_dict.items() if
y % 2 == 0)

 

# printing result 

print("The dictionary after triple even key's value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'best': 7, 'is': 4, 'gfg': 6}
    The dictionary after triple even key's value : {'best': 7, 'is': 12, 'gfg': 18}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

