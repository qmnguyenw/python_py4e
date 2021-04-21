Python | Extract length of longest string in list



Sometimes, while working with a lot of data, we can have a problem in which we
need to extract the maximum length of all the strings in list. This kind of
problem can have application in many domains. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingmax() \+ generator expression**  
The combination of above functionalities can be used to perform this task. In
this, we extract all the list lengths using generator expression and return
maximum of them using max().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting length of longest string in list

# using max() + generator expression

 

# initialize list 

test_list = ['gfg', 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extracting length of longest string in list

# using max() + generator expression

res = max(len(ele) for ele in test_list)

 

# printing result

print("Length of maximum string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best']
    Length of maximum string is : 4
    

**Method #2 : Usinglen() + key argument + max()**  
The combination of above functions can be used to perform this task. In this,
we extract the maximum length using len() and max(). It is faster than above
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

# Extracting length of longest string in list

# using len() + key argument + max()

 

# initialize list 

test_list = ['gfg', 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extracting length of longest string in list

# using len() + key argument + max()

res = len(max(test_list, key = len))

 

# printing result

print("Length of maximum string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best']
    Length of maximum string is : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

