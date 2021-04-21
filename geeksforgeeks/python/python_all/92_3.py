Python | K modulo on each Dictionary Key



Sometimes, while working with dictionaries, we might come across a problem in
which we require to perform a particular operation on each value of keys like
K modulo on each key. This type of problem can occur in web development
domain. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is the naive method in which this task can be performed. In this we
simply run a loop to traverse each key in dictionary and perform the desired
operation of K modulo.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K modulo on each Dictionary Key

# Using loop

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K 

K = 4

 

# Using loop

# K modulo on each Dictionary Key

for key in test_dict: 

 test_dict[key] %= 4

 

# printing result 

print("The dictionary after mod K each key's value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'is': 4, 'best': 7, 'gfg': 6}
    The dictionary after mod K each key's value : {'is': 0, 'best': 3, 'gfg': 2}
    

**Method #2 : Usingupdate() \+ dictionary comprehension**  
An alternate one-liner to perform this task, the combination of above
functions can be used to perform this particular task. The update function is
used to perform the % K over the dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K modulo on each Dictionary Key

# Using update() + dictionary comprehension

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K 

K = 4

 

# Using update() + dictionary comprehension

# K modulo on each Dictionary Key

test_dict.update((x, y % K) for x, y in test_dict.items())

 

# printing result 

print("The dictionary after mod K each key's value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'is': 4, 'best': 7, 'gfg': 6}
    The dictionary after mod K each key's value : {'is': 0, 'best': 3, 'gfg': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

