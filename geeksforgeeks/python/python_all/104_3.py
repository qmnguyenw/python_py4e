Python – Concatenate Dictionary string values



Sometimes, while working with dictionaries, we might have utility problem in
which we need to perform elementary operation among the common keys of
dictionaries. This can be extended to any operation to be performed. Let’s
discuss string concatenation of like key values and ways to solve it in this
article.

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

# Concatenate Dictionary string values

# Using dictionary comprehension + keys()

 

# Initialize dictionaries

test_dict1 = {'gfg' : 'a', 'is' : 'b', 'best' :
'c'}

test_dict2 = {'gfg' : 'd', 'is' : 'e', 'best' :
'f'}

 

# printing original dictionaries 

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using dictionary comprehension + keys()

# Concatenate Dictionary string values

res = {key: test_dict1[key] + test_dict2.get(key, '') for key
in test_dict1.keys()}

 

# printing result 

print("The string concatenation of dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 : {'gfg': 'a', 'is': 'b', 'best': 'c'}
    The original dictionary 2 : {'gfg': 'd', 'is': 'e', 'best': 'f'}
    The string concatenation of dictionary is : {'gfg': 'ad', 'is': 'be', 'best': 'cf'}
    

**Method #2 : UsingCounter() \+ “+” operator**  
The combination of above method can be used to perform this particular task.
In this, the Counter function converts the dictionary in the form in which the
plus operator can perform the task of concatenation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Dictionary string values

# Using Counter() + "+" operator

from collections import Counter

 

# Initialize dictionaries

test_dict1 = {'gfg' : 'a', 'is' : 'b', 'best' :
'c'}

test_dict2 = {'gfg' : 'd', 'is' : 'e', 'best' :
'f'}

 

# printing original dictionaries 

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using Counter() + "+" operator

# Concatenate Dictionary string values

temp1 = Counter(test_dict1)

temp2 = Counter(test_dict2)

res = Counter({key : temp1[key] + temp2[key] for key in
temp1}) 

 

# printing result 

print("The string concatenation of dictionary is : " +
str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 : {'gfg': 'a', 'is': 'b', 'best': 'c'}
    The original dictionary 2 : {'gfg': 'd', 'is': 'e', 'best': 'f'}
    The string concatenation of dictionary is : {'gfg': 'ad', 'is': 'be', 'best': 'cf'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

