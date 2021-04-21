Python | Get first N key:value pairs in given dictionary



Given a dictionary, the task is to get N key:value pairs from given
dictionary. This type of problem can be useful while some cases, like fetching
first N values in web development.

Note that the given dictionary is unordered, the first N pairs will not be
same here all the time. In case, you need to maintain order in your problem,
you can use ordered dictionary.

 **Code #1:** Using itertools.islice() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get N key:value pairs in given dictionary

# using itertools.islice() method

 

import itertools 

 

# Initialize dictionary

test_dict = {'Geeks' : 1, 'For':2, 'is' : 3,
'best' : 4, 'for' : 5, 'CS' : 6} 

 

# printing original dictionary 

print("The original dictionary : " + str(test_dict)) 

 

# Initialize limit 

N = 3

 

# Using islice() + items() 

# Get first N items in dictionary 

out = dict(itertools.islice(test_dict.items(), N)) 

 

# printing result 

print("Dictionary limited by K is : " + str(out))   
  
---  
  
__

__

**Output:**

> The original dictionary : {‘for’: 5, ‘best’: 4, ‘CS’: 6, ‘is’: 3, ‘Geeks’:
> 1, ‘For’: 2}  
> Dictionary limited by K is : {‘for’: 5, ‘best’: 4, ‘CS’: 6}
>
>  
>
>
>  
>

**Code #2:** Using slicing on dictionary item list

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get N key:value pairs in given dictionary

# using list slicing

 

# Initialize dictionary

test_dict = {'Geeks' : 1, 'For':2, 'is' : 3,
'best' : 4, 'for' : 5, 'CS' : 6} 

 

# printing original dictionary 

print("The original dictionary : " + str(test_dict)) 

 

# Initialize limit 

N = 3

 

# Using items() + list slicing 

# Get first K items in dictionary 

out = dict(list(test_dict.items())[0: N]) 

 

# printing result 

print("Dictionary limited by K is : " + str(out))   
  
---  
  
__

__

**Output:**

> The original dictionary : {‘best’: 3, ‘gfg’: 1, ‘is’: 2, ‘CS’: 5, ‘for’: 4}  
> Dictionary limited by K is : {‘best’: 3, ‘gfg’: 1, ‘is’: 2}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

