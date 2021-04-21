Python – Smallest K values in Dictionary



Many times while working with Python dictionary, we can have a particular
problem to find the K minima of values in numerous keys. This problem is quite
common while working with web development domain. Let’s discuss several ways
in which this task can be performed.

 **Method #1 :itemgetter() + items() + sorted()**  
The combination of above method is used to perform this particular task. In
this, we just sort the dictionary values expressed using itemgetter() and
accessed using items().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Smallest K values in Dictionary

# Using sorted() + itemgetter() + items()

from operator import itemgetter

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6,
'for' : 7, 'geeks' : 3 }

 

# Initialize K 

K = 2

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Smallest K values in Dictionary

# Using sorted() + itemgetter() + items()

res = dict(sorted(test_dict.items(), key =
itemgetter(1))[:K])

 

# printing result

print("The minimum K value pairs are " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'geeks': 3, 'is': 4, 'for': 7, 'best': 6, 'gfg': 1}
    The minimum K value pairs are {'geeks': 3, 'gfg': 1}
    

**Method #2 : Usingnsmallest()**  
This task can be performed using the nsmallest function. This is inbuilt
function in heapq library which internally performs this task and can be used
to do it externally. Has the drawback of printing just keys not values.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Smallest K values in Dictionary

# Using nsmallest

from heapq import nsmallest

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6,
'for' : 7, 'geeks' : 3 }

 

# Initialize K

K = 2

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Smallest K values in Dictionary

# Using nsmallest

res = nsmallest(K, test_dict, key = test_dict.get)

 

# printing result

print("The minimum K value pairs are " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'geeks': 3, 'best': 6, 'is': 4, 'gfg': 1, 'for': 7}
    The minimum K value pairs are ['gfg', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

