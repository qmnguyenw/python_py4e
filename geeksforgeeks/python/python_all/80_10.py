Python | Rear stray character String split



Sometimes, while working with Python Strings, we can have problem in which we
need to split a string. But sometimes, we can have a case in which we have
after splitting a blank space at rear end of list. This is usually not
desired. Lets discussed ways in which this can be avoided.

 **Method #1 : Usingsplit() + rstrip()**  
The combination of above functions can be used to solve this problem. In this,
we remove the stray character from the string before split(), to avoid the
empty string in split list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear stray character String split

# Using split() + rstrip()

 

# initializing string

test_str = 'gfg, is, best, '

 

# printing original string

print("The original string is : " + test_str)

 

# Rear stray character String split

# Using split() + rstrip()

res = test_str.rstrip(', ').split(', ')

 

# printing result 

print("The evaluated result is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg, is, best,
    The evaluated result is : ['gfg', 'is', 'best']
    

**Method #2 : Usingsplit()**  
The use of rstrip() can be avoided by passing additional arguments while
performing the split().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear stray character String split

# Using split()

 

# initializing string

test_str = 'gfg, is, best, '

 

# printing original string

print("The original string is : " + test_str)

 

# Rear stray character String split

# Using split()

res = test_str.split(', ')[0:-1]

 

# printing result 

print("The evaluated result is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg, is, best,
    The evaluated result is : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

