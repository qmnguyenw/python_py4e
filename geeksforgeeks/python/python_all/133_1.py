Python | Sort dictionary by value list length



While working with Python, one might come to a problem in which one needs to
perform a sort on dictionary list value length. This can be typically in case
of scoring or any type of count algorithm. Let’s discuss a method by which
this task can be performed.

 **Method : Usingsorted() + join() \+ lambda**  
The combination of above functions can be used to perform this particular
task. In this, we just use the lambda function to perform this particular
task, sorted and join function perform the required sorting and
encapsulation of result respectively.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary by value list length

# using sorted() + join() + lambda

 

# Initialize dictionary

test_dict = {'is' : [1, 2], 'gfg' : [3], 'best' :
[1, 3, 4]}

 

# Printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using sorted() + join() + lambda

# Sort dictionary by value list length

res = ' '.join(sorted(test_dict, key = lambda key:
len(test_dict[key])))

 

# printing result 

print("Sorted keys by value list : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': [1, 2], 'best': [1, 3, 4], 'gfg': [3]}
    Sorted keys by value list : gfg is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

