Python – Sort Nested keys by Value



Sometimes, while working with data records, we can have a problem in which we
need to perform the sorting of nested keys of dictionary by the value of
occurrence. This can have applications in arranging scores, prices etc. Lets
discuss a way in which this task can be performed.

 **Method #1 : Usingsorted() \+ lambda + generator expression**  
The combination of above methods can be used to perform this task. In this, we
perform the task of sorting using sorted() and lambda and generator expression
are used to bind and extracting values of dictionaries.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Nested keys by Value

# Using sorted() + generator expression + lamda

 

# initializing dictionary

test_dict = {'Nikhil' : {'English' : 5, 'Maths' : 2,
'Science' : 14},

 'Akash' : {'English' : 15, 'Maths' : 7, 'Science' :
2},

 'Akshat' : {'English' : 5, 'Maths' : 50, 'Science' :
20}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Sort Nested keys by Value

# Using sorted() + generator expression + lamda

res = {key : dict(sorted(val.items(), key = lambda ele:
ele[1]))

 for key, val in test_dict.items()}

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary : {‘Nikhil’: {‘English’: 5, ‘Maths’: 2, ‘Science’:
> 14}, ‘Akash’: {‘English’: 15, ‘Maths’: 7, ‘Science’: 2}, ‘Akshat’:
> {‘English’: 5, ‘Maths’: 50, ‘Science’: 20}}  
> The sorted dictionary : {‘Nikhil’: {‘Maths’: 2, ‘English’: 5, ‘Science’:
> 14}, ‘Akash’: {‘Science’: 2, ‘Maths’: 7, ‘English’: 15}, ‘Akshat’:
> {‘English’: 5, ‘Science’: 20, ‘Maths’: 50}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

