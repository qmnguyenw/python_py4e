Python program to Sort a List of Strings by the Number of Unique Characters



Given a list of strings. The task is to sort the list of strings by the number
of unique characters.

 **Examples:**

>  **Input** : test_list = [‘gfg’, ‘best’, ‘for’, ‘geeks’],  
> **Output** : [‘gfg’, ‘for’, ‘best’, ‘geeks’]  
> **Explanation** : 2, 3, 4, 4 are unique elements in lists.
>
>  **Input** : test_list = [‘gfg’, ‘for’, ‘geeks’],  
> **Output** : [‘gfg’, ‘for’, ‘geeks’]  
> **Explanation** : 2, 3, 4 are unique elements in lists.

**Method #1 : Using sort() +** **len()** **+** **set()**

  

  

In this, we perform task of sorting using sort(), and len and sort functions
are used to get length of unique characters in string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Unique characters

# Using sort() + len() + set()

 

# helper function

def hlper_fnc(ele):

 

 # getting Unique elements count 

 return len(list(set(ele)))

 

# initializing list

test_list = ['gfg', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# perform sort

test_list.sort(key = hlper_fnc)

 

# printing result 

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'best', 'for', 'geeks']
    Sorted List : ['gfg', 'for', 'best', 'geeks']
    

**Method #2 : Using** **sorted()** **+** **len()** **+** **set()** **+**
**lambda**

Similar to above method, difference being not inplace sort, and also uses
lambda function for performing task.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Unique characters

# Using sorted() + len() + set() + lambda

 

# initializing list

test_list = ['gfg', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# perform sort

res = sorted(test_list, key = lambda sub :
len(list(set(sub))))

 

# printing result 

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'best', 'for', 'geeks']
    Sorted List : ['gfg', 'for', 'best', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

