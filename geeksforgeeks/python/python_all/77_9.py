Python – Extract Dictionary values list to List



Sometimes, while working with dictionary records, we can have problems in
which we need to extract all the dictionary values into a single separate
list. This can have possible application in data domains and web-development.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingmap() \+ generator expression**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of extraction of values using generator expression
and map() is used to reconstruct the value lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting Dictionary values list to List

# Using map() + generator expression

 

# initializing dictionary

test_dict = {'gfg' : [4, 6, 7, 8],

 'is' : [3, 8, 4, 2, 1],

 'best' : [9, 5, 2, 1, 0]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extracting Dictionary values to List

# Using map() + generator expression

res = list(map(list, (ele for ele in
test_dict.values())))

 

# printing result 

print("The list of dictionary values : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [3, 8, 4, 2, 1], ‘gfg’: [4, 6, 7, 8],
> ‘best’: [9, 5, 2, 1, 0]}  
> The list of dictionary values : [[3, 8, 4, 2, 1], [4, 6, 7, 8], [9, 5, 2, 1,
> 0]]

  

  

**Method #2 : Usingmap()**  
The combination of above functions can be used to solve this problem. In this
we perform the task of extraction and remaking using map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting Dictionary values list to List

# Using map()

 

# initializing dictionary

test_dict = {'gfg' : [4, 6, 7, 8],

 'is' : [3, 8, 4, 2, 1],

 'best' : [9, 5, 2, 1, 0]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extracting Dictionary values to List

# Using map()

res = list(map(list, (test_dict.values())))

 

# printing result 

print("The list of dictionary values : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [3, 8, 4, 2, 1], ‘gfg’: [4, 6, 7, 8],
> ‘best’: [9, 5, 2, 1, 0]}  
> The list of dictionary values : [[3, 8, 4, 2, 1], [4, 6, 7, 8], [9, 5, 2, 1,
> 0]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

