Python | Split given dictionary in half



While working with dictionaries, sometimes we might have a problem in which we
need to reduce the space taken by single container and wish to divide the
dictionary into 2 halves. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Usingitems() + len() \+ list slicing**  
The combination of above functions can easily perform this particular task in
which slicing into half is done by list slicing and items of dictionary are
extracted by items()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split dictionary by half

# Using items() + len() + list slicing

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2,
'CS' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using items() + len() + list slicing

# Split dictionary by half

res1 =
dict(list(test_dict.items())[len(test_dict)//2:])

res2 =
dict(list(test_dict.items())[:len(test_dict)//2])

 

# printing result 

print("The first half of dictionary : " + str(res1))

print("The second half of dictionary : " + str(res2))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘CS’: 10, ‘for’: 2, ‘is’: 4, ‘gfg’: 6}  
> The first half of dictionary : {‘is’: 4, ‘gfg’: 6}  
> The second half of dictionary : {‘for’: 2, ‘CS’: 10}

  

  

**Method #2 : Usingslice() + len() + items()**  
The combination of above functions can be used to perform this particular
task. In this, we perform task similar to above method, just the difference is
the slice operation is performed by slice() instead of list slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split dictionary by half

# Using items() + len() + slice()

from itertools import islice

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2,
'CS' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using items() + len() + slice()

# Split dictionary by half

inc = iter(test_dict.items())

res1 = dict(islice(inc, len(test_dict) // 2)) 

res2 = dict(inc)

 

# printing result 

print("The first half of dictionary : " + str(res1))

print("The second half of dictionary : " + str(res2))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘CS’: 10, ‘for’: 2, ‘is’: 4, ‘gfg’: 6}  
> The first half of dictionary : {‘is’: 4, ‘gfg’: 6}  
> The second half of dictionary : {‘for’: 2, ‘CS’: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

