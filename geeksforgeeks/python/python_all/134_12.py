Python | Get first K items in dictionary



While working with dictionaries, we can come across a problem in which we
might have to get just some of the initial keys in dictionary. This problem
can typically occur in cases of web development domain. Let’s discuss certain
ways in which this problem can be solved.

 **Method #1 : Usingitems() \+ list slicing**  
To solve this problem, combination of above functions have to implied. The
items function can be used to get all the dictionary items and main task is
done by list slicing, which limits the dictionary key-value pair.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get first K items in dictionary

# Using items() + list slicing

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize limit

K = 3

 

# Using items() + list slicing

# Get first K items in dictionary

res = dict(list(test_dict.items())[0: K])

 

# printing result 

print("Dictionary limited by K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘CS’: 5, ‘best’: 3, ‘gfg’: 1, ‘for’: 4}  
> Dictionary limited by K is : {‘is’: 2, ‘CS’: 5, ‘best’: 3}

  

  

**Method #2 : Usingislice() + items()**  
The combination of above functions can be used to perform this particular
task. In these, we perform the slice using the islice() and items function
allows to get the items out of iterable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get first K items in dictionary

# Using islice() + items()

import itertools

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize limit

K = 3

 

# Using islice() + items()

# Get first K items in dictionary

res = dict(itertools.islice(test_dict.items(), K))

 

# printing result 

print("Dictionary limited by K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘CS’: 5, ‘best’: 3, ‘gfg’: 1, ‘for’: 4}  
> Dictionary limited by K is : {‘is’: 2, ‘CS’: 5, ‘best’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

