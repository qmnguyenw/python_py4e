Python – Reverse Dictionary Keys Order



Sometimes, while working with dictionary, we can have a problem in which we
need to reverse the order of dictionary. This is quite a common problem and
can have application in many domains including day-day programming and web
development. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : UsingOrderedDict() + reversed() + items()**  
This method is for older versions of Python. Older versions don’t keep order
in dictionaries, hence have to converted to OrderedDict to execute this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Dictionary Keys Order

# Using OrderedDict() + reversed() + items()

from collections import OrderedDict

 

# initializing dictionary

test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Reverse Dictionary Keys Order

# Using OrderedDict() + reversed() + items()

res = OrderedDict(reversed(list(test_dict.items())))

 

# printing result 

print("The reversed order dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary : {‘is’: 2, ‘best’: 5, ‘gfg’: 4}  
> The reversed order dictionary : OrderedDict([(‘gfg’, 4), (‘best’, 5), (‘is’,
> 2)])

  

  

**Method #2 : Usingreversed() + items()**  
The combination of above functions can be used to solve this problem. This is
for newer versions of Python, which have dictionary in incoming order of
elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Dictionary Keys Order

# Using reversed() + items()

 

# initializing dictionary

test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Reverse Dictionary Keys Order

# Using reversed() + items()

res = dict(reversed(list(test_dict.items())))

 

# printing result 

print("The reversed order dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary : {'gfg': 4, 'is': 2, 'best': 5}
    The reversed order dictionary : {'best': 5, 'is': 2, 'gfg': 4}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

