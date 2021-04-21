Python | Threshold Size Greater Strings Frequency



Sometimes, while working with huge amount of data, we can have a problem in
which we need to know count of just specific sized strings which are greater
than a specific length. This kind of problem can occur during validation cases
across many domains. Let’s discuss certain ways to handle this in Python
strings list.

 **Method #1 : Using list comprehension +len()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate for all the strings and return only strings which have length
greater than K checked using len(). The count is extracted using len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Threshold Size Greater Strings Frequency

# using list comprehension + len()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 3

 

# Threshold Size Greater Strings Frequency

# using list comprehension + len()

res = len([ele for ele in test_list if len(ele) >=
K])

 

# printing result

print("The frequency of threshhold K sized strings are : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The frequency of threshhold K sized strings are : 4
    

**Method #2 : Usingfilter() + len() \+ lambda**  
The combination of above functionalities can be used to perform this task. In
this, we extract the elements using filter() and logic is compiled in a lambda
function. The count is extracted using len().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Threshold Size Greater Strings Frequency

# using filter() + lambda + len()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 3

 

# Threshold Size Greater Strings Frequency

# using filter() + lambda + len()

res = len(list(filter(lambda ele: len(ele) >= K,
test_list)))

 

# printing result

print("The frequency of threshhold K sized strings are : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The frequency of threshhold K sized strings are : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

