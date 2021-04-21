Python – Replace duplicate Occurrence in String



Sometimes, while working with Python strings, we can have problem in which we
need to perform the replace of a word. This is quite common task and has been
discussed many times. But sometimes, the requirement is to replace occurrence
of only duplicate, i.e from second occurrence. This has applications in many
domains. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingsplit() + enumerate() \+ loop**  
The combination of above functions can be used to perform this task. In this,
we separate the words using split. In this, we memoize the first occurrence in
set and check if the value is saved before and then is replaced is already
occurred.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace duplicate Occurrence in String

# Using split() + enumerate() + loop

 

# initializing string

test_str = 'Gfg is best . Gfg also has Classes now. \

 Classes help understand better . '

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing replace mapping 

repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

 

# Replace duplicate Occurrence in String

# Using split() + enumerate() + loop

test_list = test_str.split(' ')

res = set()

for idx, ele in enumerate(test_list):

 if ele in repl_dict:

 if ele in res:

 test_list[idx] = repl_dict[ele]

 else:

 res.add(ele)

res = ' '.join(test_list)

 

# printing result 

print("The string after replacing : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : Gfg is best . Gfg also has Classes now. Classes
> help understand better .  
> The string after replacing : Gfg is best . It also has Classes now. They
> help understand better .

  

  

**Method #2 : Usingkeys() + index() \+ list comprehension**  
This is yet another way in which this task can be performed. In this, we don’t
require memoization. This is one liner approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace duplicate Occurrence in String

# Using keys() + index() + list comprehension

 

# initializing string

test_str = 'Gfg is best . Gfg also has Classes now. Classes help
understand better . '

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing replace mapping 

repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

 

# Replace duplicate Occurrence in String

# Using keys() + index() + list comprehension

test_list = test_str.split(' ')

res = ' '.join([repl_dict.get(val) if val in repl_dict.keys()
and test_list.index(val) != idx 

 else val for idx, val in enumerate(test_list)])

 

# printing result 

print("The string after replacing : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : Gfg is best . Gfg also has Classes now. Classes
> help understand better .  
> The string after replacing : Gfg is best . It also has Classes now. They
> help understand better .

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

