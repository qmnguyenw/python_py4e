Python | Subtraction of dictionaries



Sometimes, while working with dictionaries, we might have utility problem in
which we need to perform elementary operation among the common keys of
dictionaries. This can be extended to any operation to be performed. Let’s
discuss subtraction of like key values and ways to solve it in this article.

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

# Subtraction of dictionaries

# Using dictionary comprehension + keys()

 

# Initialize dictionaries

test_dict1 = {'gfg' : 6, 'is' : 4, 'best' : 7}

test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

 

# printing original dictionaries 

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using dictionary comprehension + keys()

# Subtraction of dictionaries

res = {key: test_dict2[key] - test_dict1.get(key, 0)

 for key in test_dict2.keys()}

 

# printing result 

print("The difference dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 : {'gfg': 6, 'is': 4, 'best': 7}
    The original dictionary 2 : {'gfg': 10, 'is': 6, 'best': 10}
    The difference dictionary is : {'gfg': 4, 'is': 2, 'best': 3}
    

**Method #2 : UsingCounter() + "-" operator**  
The combination of above method can be used to perform this particular task.
In this, the Counter function converts the dictionary in the form in which the
minus operator can perform the task of subtraction.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subtraction of dictionaries

# Using Counter() + "-" operator

from collections import Counter

 

# Initialize dictionaries

test_dict1 = {'gfg' : 6, 'is' : 4, 'best' : 7}

test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}

 

# printing original dictionaries 

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using Counter() + "-" operator

# Subtraction of dictionaries

temp1 = Counter(test_dict1)

temp2 = Counter(test_dict2)

res = temp2 - temp1

 

# printing result 

print("The difference dictionary is : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 : {'gfg': 6, 'is': 4, 'best': 7}
    The original dictionary 2 : {'gfg': 10, 'is': 6, 'best': 10}
    The difference dictionary is : {'gfg': 4, 'is': 2, 'best': 3}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

