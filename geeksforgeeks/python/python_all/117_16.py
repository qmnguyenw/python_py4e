Python – Split heterogeneous type list



Sometimes, we might be working with many data types and in these instances, we
can have a problem in which list that we receive might be having elements from
different data types. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension +isinstance()**  
The combination of above both functionalities can be used to perform this
task. In this, we just extract the similar element types using different list
comprehensions and detect the type using isinstance().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split heterogenous type list

# using list comprehension + isinstance

 

# initialize list 

test_list = ['gfg', 1, 2, 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Split heterogenous type list

# using list comprehension + isinstance

res_str = [ele for ele in test_list if isinstance(ele,
str)]

res_int = [ele for ele in test_list if isinstance(ele,
int)]

 

# printing result

print("Integer list : " + str(res_int))

print("String list : " + str(res_str))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 1, 2, 'is', 'best']
    Integer list : [1, 2]
    String list : ['gfg', 'is', 'best']
    

**Method #2 : Using defaultdict() \+ loop**  
This is yet another way in which this problem can be solved. In this, we
initialize the list as data type for defaultdict() and loop through each
element and save each datatype list in defaultdict.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split heterogenous type list

# using defaultdict() + loop

from collections import defaultdict

 

# initialize list 

test_list = ['gfg', 1, 2, 'is', 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Split heterogenous type list

# using defaultdict() + loop

res = defaultdict(list)

for ele in test_list:

 res[type(ele)].append(ele)

 

# printing result

print("Integer list : " + str(res[int]))

print("String list : " + str(res[str]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 1, 2, 'is', 'best']
    Integer list : [1, 2]
    String list : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

