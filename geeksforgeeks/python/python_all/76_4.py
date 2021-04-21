Python – Sort List by Dictionary values



Sometimes while working with Python dictionary, we can have problem in which
we need to perform a sort of list according to corresponding value in
dictionary. This can have application in many domains, including data and web
development. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingsorted() + key + lambda**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of sorting using sorted(). The lambda function is used to
get key’s values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort List by Dictionary values

# Using sorted() + key + lambda

 

# initializing list

test_list = ['gfg', 'is', 'best']

 

# initializing Dictionary

test_dict = {'gfg' : 56, 'is' : 12, 'best' : 76}

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sort List by Dictionary values

# Using sorted() + key + lambda

res = sorted(test_list, key = lambda ele: test_dict[ele])

 

# printing result 

print("The list after sorting : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    The original dictionary is : {'best': 76, 'gfg': 56, 'is': 12}
    The list after sorting : ['is', 'gfg', 'best']
    

**Method #2 : Usingsorted() + key + get()**  
This method performs the task in similar way as above method. The difference
is that it accesses values get().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort List by Dictionary values

# Using sorted() + key + get()

 

# initializing list

test_list = ['gfg', 'is', 'best']

 

# initializing Dictionary

test_dict = {'gfg' : 56, 'is' : 12, 'best' : 76}

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sort List by Dictionary values

# Using sorted() + key + get()

res = sorted(test_list, key = test_dict.get)

 

# printing result 

print("The list after sorting : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    The original dictionary is : {'best': 76, 'gfg': 56, 'is': 12}
    The list after sorting : ['is', 'gfg', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

