Python – Dictionary Values Division



Sometimes, while working with dictionaries, we might have utility problem in
which we need to perform elementary operation among the common keys of
dictionaries. This can be extended to any operation to be performed. Let’s
discuss division of like key values and ways to solve it in this article.

 **Method #1 : Using dictionary comprehension +keys()**  
The combination of above two can be used to perform this particular task. This
is just a shorthand to the longer method of loops and can be used to perform
this task in one line.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Values Division

# Using dictionary comprehension + keys()

 

# Initialize dictionaries

test_dict1 = {'gfg' : 20, 'is' : 24, 'best' :
100}

test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

 

# printing original dictionaries 

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using dictionary comprehension + keys()

# Dictionary Values Division

res = {key: test_dict1[key] // test_dict2.get(key, 0)

 for key in test_dict1.keys()}

 

# printing result 

print("The divided dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 : {'is': 24, 'best': 100, 'gfg': 20}
    The original dictionary 2 : {'is': 6, 'best': 10, 'gfg': 10}
    The divided dictionary is : {'is': 4, 'best': 10, 'gfg': 2}
    

**Method #2 : Using Counter() \+ “//” operator**  
The combination of above method can be used to perform this particular task.
In this, the Counter function converts the dictionary in the form in which the
divide operator can perform the task of division.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Values Division

# Using Counter() + "//" operator

from collections import Counter

 

# Initialize dictionaries

test_dict1 = {'gfg' : 20, 'is' : 24, 'best' :
100}

test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

 

# printing original dictionaries 

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using Counter() + "//" operator

# Dictionary Values Division

temp1 = Counter(test_dict1)

temp2 = Counter(test_dict2)

res = Counter({key : temp1[key] // temp2[key] for key in
temp1})

 

# printing result 

print("The division dictionary is : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 : {'is': 24, 'best': 100, 'gfg': 20}
    The original dictionary 2 : {'is': 6, 'best': 10, 'gfg': 10}
    The divided dictionary is : {'is': 4, 'best': 10, 'gfg': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

