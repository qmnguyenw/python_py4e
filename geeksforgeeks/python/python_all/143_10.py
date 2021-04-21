Python | Split on last occurrence of delimiter



The splitting of string has always been discussed in various applications and
use cases. One of the interesting variation of list splitting can be splitting
the list on delimiter but this time only on the last occurrence of it. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Using rsplit(str, 1)**  
The normal string split can perform the split from the front, but Python also
offers another method which can perform this very task from the rear end, and
hence increasing the versatility of applications.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split on last occurrence of delimiter

# using rsplit()

 

# initializing string 

test_string = "gfg, is, good, better, and best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using rsplit()

# Split on last occurrence of delimiter

res = test_string.rsplit(', ', 1)

 

# print result

print("The splitted list at the last comma : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : gfg, is, good, better, and best
    The splitted list at the last comma : ['gfg, is, good, better', 'and best']
    

**Method #2 : Usingrpartition()**  
This function can also perform the desired reverse partition, but the
drawbacks to use this is construction of additional delimiter value and also
the speed is slower than above method and hence not recommended.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split on last occurrence of delimiter

# using rpartition()

 

# initializing string 

test_string = "gfg, is, good, better, and best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using rpartition()

# Split on last occurrence of delimiter

res = test_string.rpartition(', ')

 

# print result

print("The splitted list at the last comma : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : gfg, is, good, better, and best
    The splitted list at the last comma : ('gfg, is, good, better', ', ', 'and best')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

