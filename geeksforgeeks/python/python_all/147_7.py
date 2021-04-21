Python | Split Sublist Strings



Yet another variation of splitting strings is splitting the strings that are
an element of the sublist. This is quite peculiar problem, but one can get the
data in this format and knowledge of splitting it anyways quite useful. Let’s
discuss certain ways in which this particular task can be performed.

 **Method #1 : Using list comprehension +split()**

This method is the shorthand version of the longer loop version that one could
choose to solve this particular problem. We just split the strings fetching
the sublist using the loop in list comprehension using split function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split Sublist Strings

# using split() + list comprehension

 

# initializing list

test_list = [['GfG is best'], ['All love Gfg'], ['Including
me']]

 

# printing original list

print("The original list : " + str(test_list))

 

# using split() + list comprehension

# Split Sublist Strings

res = [sub.split() for subl in test_list for sub in
subl]

 

# print result

print("The list after splitting strings : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[‘GfG is best’], [‘All love Gfg’], [‘Including me’]]  
> The list after splitting strings : [[‘GfG’, ‘is’, ‘best’], [‘All’, ‘love’,
> ‘Gfg’], [‘Including’, ‘me’]]
>
>  
>
>
>  
>

**Method #2 : Usingmap() \+ lambda + split()**

This task can also be performed using the combination of above 3 functions.
The map function binds the splitting logic to each element which is written
using the lambda function that uses split function to perform the split.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split Sublist Strings

# using map() + lambda + split()

 

# initializing list

test_list = [['GfG is best'], ['All love Gfg'], ['Including
me']]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + lambda + split()

# Split Sublist Strings

res = list(map(lambda sub: sub[0].split(' '),
test_list))

 

# print result

print("The list after splitting strings : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[‘GfG is best’], [‘All love Gfg’], [‘Including me’]]  
> The list after splitting strings : [[‘GfG’, ‘is’, ‘best’], [‘All’, ‘love’,
> ‘Gfg’], [‘Including’, ‘me’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

