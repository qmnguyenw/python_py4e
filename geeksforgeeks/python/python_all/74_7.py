Python – Sort Dictionary by Value Difference



Sometimes, while working with Python dictionaries, we can have problem in
which in which we need to perform sorting of items on bases of various
factors. One such can be on basis of absolute difference of dual value list.
This can occur in Python > 3.6, as dictionaries are ordered. This kind of
problem can come in data domain. Let’s discuss a way in which this problem can
be solved.

 **Method : Usingsorted() + lambda + abs() \+ dictionary comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of sorting using sorted(), lambda function is used to
provide the logic and abs() function is used to compute the absolute
difference.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Value Difference

# Using sorted() + lambda + abs() + dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg' : [34, 87],

 'is' : [10, 13], 

 'best' : [19, 27], 

 'for' : [10, 50], 

 'geeks' : [15, 45]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sort Dictionary by Value Difference

# Using sorted() + lambda + abs() + dictionary comprehension

res = dict(sorted(test_dict.items(), key = lambda sub:
abs(sub[1][0] - sub[1][1])))

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [34, 87], ‘is’: [10, 13], ‘best’: [19,
> 27], ‘for’: [10, 50], ‘geeks’: [15, 45]}  
> The sorted dictionary : {‘is’: [10, 13], ‘best’: [19, 27], ‘geeks’: [15,
> 45], ‘for’: [10, 50], ‘gfg’: [34, 87]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

