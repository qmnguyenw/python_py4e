Python | N largest values in dictionary



Many times while working with Python dictionary, we can have a particular
problem to find the N maxima of values in numerous keys. This problem is quite
common while working with web development domain. Let’s discuss several ways
in which this task can be performed.

 **Method #1 :itemgetter() + items() + sorted()**

The combination of above method is used to perform this particular task. In
this, we just reverse sort the dictionary values expressed using
itemgetter() and accessed using items().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N largest values in dictionary

# Using sorted() + itemgetter() + items()

from operator import itemgetter

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6,
'for' : 7, 'geeks' : 3 }

 

# Initialize N 

N = 3

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# N largest values in dictionary

# Using sorted() + itemgetter() + items()

res = dict(sorted(test_dict.items(), key = itemgetter(1),
reverse = True)[:N])

 

# printing result

print("The top N value pairs are " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 6, 'gfg': 1, 'geeks': 3, 'for': 7, 'is': 4}
    The top N value pairs are  {'for': 7, 'is': 4, 'best': 6}
    

  

  

**Method #2 : Usingnlargest()**  
This task can be performed using the nlargest function. This is inbuilt
function in heapq library which internally performs this task and can be
used to do it externally. Has the drawback of printing just keys not values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N largest values in dictionary

# Using nlargest

from heapq import nlargest

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6,
'for' : 7, 'geeks' : 3 }

 

# Initialize N 

N = 3

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# N largest values in dictionary

# Using nlargest

res = nlargest(N, test_dict, key = test_dict.get)

 

# printing result

print("The top N value pairs are " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': 1, 'best': 6, 'geeks': 3, 'for': 7, 'is': 4}
    The top N value pairs are  ['for', 'best', 'is']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

