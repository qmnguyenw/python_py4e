Python | Selective key values in dictionary



Sometimes while working with Python dictionaries, we might have a problem in
which we require to just get the selective key values from the dictionary.
This problem can occur in web development domain. Let’s discuss certain ways
in which this problem can be solved.

 **Method #1 : Using list comprehension +get()**  
The combination of above functions can be used to perform this particular
task. In this, we access the values using the get method and traverse the
dictionary using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective key values in dictionary

# Using list comprehension + get()

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize key list 

key_list = ['gfg', 'best', 'CS']

 

# Using list comprehension + get()

# Selective key values in dictionary

res = [test_dict.get(key) for key in key_list]

 

# printing result 

print("The values of Selective keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘gfg’: 1, ‘for’: 4, ‘CS’: 5, ‘best’: 3}  
> The values of Selective keys : [1, 3, 5]

  

  

**Method #2 : Usingitemgetter()**  
This single function can be used to perform this particular task. It is built
in to perform this specific task. It takes chain of keys and returns the
corresponding values as a tuple which can be type casted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective key values in dictionary

# Using itemgetter()

from operator import itemgetter

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize key list 

key_list = ['gfg', 'best', 'CS']

 

# Using itemgetter()

# Selective key values in dictionary

res = list(itemgetter(*key_list)(test_dict))

 

# printing result 

print("The values of Selective keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘gfg’: 1, ‘for’: 4, ‘CS’: 5, ‘best’: 3}  
> The values of Selective keys : [1, 3, 5]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

