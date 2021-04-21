Python | Get the number of keys with given value N in dictionary



In this article, we will see how to get the number of keys with some given
value N in a given dictionary. There are multiple methods to do this task.
Let’s see them with help of examples.

 **Simple method –**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Get the number of keys

# with given value N in dictionary

 

# Initialize dictionary 

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 2, 'CS' : 2} 

 

 

# printing original dictionary 

print("The original dictionary : " + str(test_dict)) 

 

# Initialize value 

N = 2

 

# Using loop 

# Selective key values in dictionary 

res = 0

for key in test_dict: 

 if test_dict[key] == N: 

 res = res + 1

 

# printing result 

print("Frequency of N is : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original dictionary : {'CS': 2, 'for': 2, 'is': 2, 'gfg': 1, 'best': 3}
    Frequency of N is : 3
    

**Method #2:** Using sum() + values()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Get the number of keys

# with given value N in dictionary

# Using sum() + values() 

 

# Initialize dictionary 

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 2, 'CS' : 2} 

 

# printing original dictionary 

print("The original dictionary : " + str(test_dict)) 

 

# Initialize value 

N = 2

 

# Using sum() + values() 

# Selective key values in dictionary

res = sum(x == N for x in test_dict.values()) 

 

# printing result 

print("Frequency of K is : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original dictionary : {'is': 2, 'for': 2, 'gfg': 1, 'best': 3, 'CS': 2}
    Frequency of K is : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

