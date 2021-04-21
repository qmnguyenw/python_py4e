Python | Concatenate N consecutive elements in String list



Sometimes, while working with data, we can have a problem in which we need to
perform the concatenation of N consecutive Strings in list of Strings. This
can have many applications across domains. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingformat() + zip() + iter() \+ list comprehension**  
The combination of above methods can be used to perform this particular task.
In this we perform the task of grouping using zip() and iter(), format() is
used to specify grouping delimiter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive N concatenation in String list

# using format() + zip() + iter() + list comprehension

 

# initialize list 

test_list = ['gfg', 'is', 'good', 'for', 'geek',
'people']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize N 

N = 3

 

# Consecutive N concatenation in String list

# using format() + zip() + iter() + list comprehension

temp = '{} ' * N 

res = [temp.format(*ele) for ele in
zip(*[iter(test_list)] * N)]

 

# printing result

print("List after N concatenation of String : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'good', 'for', 'geek', 'people']
    List after N concatenation of String : ['gfg is good ', 'for geek people ']
    

**Method #2 : Usingstarmap() + zip() + iter() + format()**  
The combination of above functions perform the similar task. The only
difference is that starmap() is used instead of list comprehension for list
construction.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive N concatenation in String list

# using starmap() + zip() + iter() + format()

from itertools import starmap

 

# initialize list 

test_list = ['gfg', 'is', 'good', 'for', 'geek',
'people']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize N 

N = 3

 

# Consecutive N concatenation in String list

# using starmap() + zip() + iter() + format()

temp = '{} ' * N

res = list(starmap(temp.format, zip(*[iter(test_list)]
* N)))

 

# printing result

print("List after N concatenation of String : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'good', 'for', 'geek', 'people']
    List after N concatenation of String : ['gfg is good ', 'for geek people ']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

