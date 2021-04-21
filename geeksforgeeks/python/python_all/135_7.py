Python | Priority key assignment in dictionary



Sometimes, while working with dictionaries, we have an application in which we
need to assign a variable with a single value that would be from any of given
keys, whichever occurs first in priority. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop**  
This task can be performed in a brute force manner using loop. In this, we can
just loop through the dictionary keys and priority list. If we find the key,
we break and assign variable with it’s value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Priority key assignment in dictionary

# Using loop

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2,
'CS' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize priority keys

prio_list = ['best', 'gfg', 'CS']

 

# Using loop

# Priority key assignment in dictionary

res = None

for key in test_dict:

 if key in prio_list :

 res = test_dict[key]

 break

 

# printing result 

print("The variable value after assignment : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'gfg': 6, 'is': 4, 'CS': 10, 'for': 2}
    The variable value after assignment : 6
    

**Method #2 : Using nestedget()**  
This problem can be solved by nesting the get() to get the value on priority.
Even if it provides a cleaner and one-liner alternative to solve the problem,
it is not recommended if we have more candidate keys to check for priority.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Priority key assignment in dictionary

# Using nested get()

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2,
'CS' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize priority keys

prio_list = ['best', 'gfg', 'CS']

 

# Using nested get()

# Priority key assignment in dictionary

res = test_dict.get(prio_list[0], test_dict.get(prio_list[1],

 test_dict.get(prio_list[2])))

 

# printing result 

print("The variable value after assignment : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'gfg': 6, 'is': 4, 'CS': 10, 'for': 2}
    The variable value after assignment : 6
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

