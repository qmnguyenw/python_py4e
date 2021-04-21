Python – Filter Non-None dictionary Keys



Many times, while working with dictionaries, we wish to get keys for a non-
null keys. This finds application in Machine Learning in which we have to feed
data with no none values. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
In this we just run a loop for all the keys and check for values, if its not
None, we append into a list which stores keys of all Non None keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non-None dictionary Keys

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using loop

# Non-None dictionary Keys

res = []

for ele in test_dict:

 if test_dict[ele] is not None :

 res.append(ele)

 

# printing result 

print("Non-None keys list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'for': 2, 'CS': None, 'Gfg': 1}
    Non-None keys list : ['for', 'Gfg']
    

**Method #2 : Using dictionary comprehension**  
This task can also be performed using dictionary comprehension. In this, we
perform similar operation as above method, just as a shorthand.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non-None dictionary Keys

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Non-None dictionary Keys

# Using dictionary comprehension

res = list({ele for ele in test_dict if test_dict[ele]})

 

# printing result 

print("Non-None keys list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'for': 2, 'CS': None, 'Gfg': 1}
    Non-None keys list : ['for', 'Gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

