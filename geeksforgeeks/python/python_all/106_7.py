Python – Smallest Length String



Sometimes, while working with a lot of data, we can have a problem in which we
need to extract the minimum of all the strings in list. This kind of problem
can have application in many domains. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop**  
This is the brute method in which we perform this task. In this, we run a loop
to keep a memory of smallest string length and return the string which has min
length in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Smallest Length String

# using loop 

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks'] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# Smallest Length String 

# using loop 

min_len = 99999

for ele in test_list: 

 if len(ele) < min_len: 

 min_len = len(ele) 

 res = ele 

 

# printing result 

print("Minimum length string is : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    Minimum length string is : is
    

**Method #2 : Using min() \+ key**  
This method can also be used to solve this problem. In this, we use inbuilt
min() with “len” as key argument to extract the string with the minimum
length.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Smallest Length String

# using min() + key 

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks'] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# Smallest Length String

# using min() + key 

res = min(test_list, key = len) 

 

# printing result 

print("Minimum length string is : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    Minimum length string is : is
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

