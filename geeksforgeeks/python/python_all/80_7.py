Python | Split flatten String List



Sometimes, while working with Python Strings, we can have problem in which we
need to perform the split of strings on a particular deliminitor. In this, we
might need to flatten this to a single String List. Lets discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension +split() + extend()**  
The combination of above functions can be used to perform this task. In this,
we perform the task of split, using split() and add split elements in list
using extend().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split flatten String List

# Using list comprehension + split() + extend()

 

# initializing list

test_list = ['gfg-is-best', 'for-all', 'geeks-and',
'CS']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Split flatten String List

# Using list comprehension + split() + extend()

res = []

[res.extend(idx.split("-")) for idx in test_list] 

 

# printing result 

print("The String List after extension : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg-is-best', 'for-all', 'geeks-and', 'CS']
    The String List after extension : ['gfg', 'is', 'best', 'for', 'all', 'geeks', 'and', 'CS']
    

**Method #2 : Usingsplit() + join()**  
This is one of the way in which this task can be performed. In this, we
perform the task of extension using join() and split().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split flatten String List

# Using split() + join()

 

# initializing list

test_list = ['gfg-is-best', 'for-all', 'geeks-and',
'CS']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Split flatten String List

# Using split() + join()

res = '-'.join(test_list).split('-')

 

# printing result 

print("The String List after extension : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg-is-best', 'for-all', 'geeks-and', 'CS']
    The String List after extension : ['gfg', 'is', 'best', 'for', 'all', 'geeks', 'and', 'CS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

