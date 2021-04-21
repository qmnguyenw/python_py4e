Python – Length of shortest string in string list



Sometimes, while working with a lot of data, we can have a problem in which we
need to extract the minimum length string of all the strings in list. This
kind of problem can have application in many domains. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using min() \+ generator expression**  
The combination of above functionalities can be used to perform this task. In
this, we extract all the list lengths using generator expression and return
minimum of them using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum String length

# using min() + generator expression

 

# initialize list 

test_list = ['gfg', 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Minimum String length

# using min() + generator expression

res = min(len(ele) for ele in test_list)

 

# printing result

print("Length of minimum string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best']
    Length of minimum string is : 2
    

**Method #2 : Usinglen() + key argument + min()**  
The combination of above functions can be used to perform this task. In this,
we extract the minimum length using len() and min(). It is faster than above
method as it performs more task built in rather than overhead by generator
expression.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum String length

# using len() + key argument + min()

 

# initialize list 

test_list = ['gfg', 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Minimum String length

# using len() + key argument + min()

res = len(min(test_list, key = len))

 

# printing result

print("Length of minimum string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best']
    Length of minimum string is : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

