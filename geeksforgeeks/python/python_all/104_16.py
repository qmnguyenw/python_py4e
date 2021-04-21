Python | Extract filtered Dictionary Values



While working with Python dictionaries, there can be cases in which we are
just concerned about getting the filtered values list and don’t care about
keys. This is yet another essential utility and solution to it should be known
and discussed. Let’s perform this task through certain methods.

 **Method #1 : Using loop +keys()**  
The first method that comes to mind to achieve this task is the use of loop to
access each filtered key’s value and append it into a list and return it. This
can be one of method to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract filtered Dictionary Values

# Using loop + keys()

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 2

 

# Extract filtered Dictionary Values

# Using loop + keys()

res = []

for key in test_dict.keys() :

 if test_dict[key] >= K:

 res.append(test_dict[key])

 

# printing result

print("The list of filtered values is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'gfg': 1, 'is': 2}
    The list of filtered values is : [3, 2]
    

**Method #2 : Usingvalues()**  
This task can also be performed using the inbuilt function of values(). This
is the best and most Pythonic way to perform this particular task and returns
the filtered exact desired result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract filtered Dictionary Values

# Using values()

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 2

 

# Extract filtered Dictionary Values

# Using values()

temp = list(test_dict.values())

res = [ele for ele in temp if ele >= K]

 

# printing result

print("The list of filtered values is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'gfg': 1, 'is': 2}
    The list of filtered values is : [3, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

