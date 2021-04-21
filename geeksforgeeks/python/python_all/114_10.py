Python | Longest String in list



Sometimes, while working with Python Lists, we can have a problem in which we
receive Strings as elements and wish to compute the String which has maximum
length. This kind of problem can have applications in many domains. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop**  
This is the brute method in which we perform this task. In this, we run a loop
to keep a memory of longest string length and return the string which has max
length in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest String in list

# using loop

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Longest String in list

# using loop

max_len = -1

for ele in test_list:

 if len(ele) > max_len:

 max_len = len(ele)

 res = ele

 

# printing result

print("Maximum length string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    Maximum length string is : geeks
    

**Method #2 : Usingmax() \+ key**  
This method can also be used to solve this problem. In this, we use inbuilt
max() with “len” as key argument to extract the string with the maximum
length.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest String in list

# using max() + key

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Longest String in list

# using max() + key

res = max(test_list, key = len)

 

# printing result

print("Maximum length string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    Maximum length string is : geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

