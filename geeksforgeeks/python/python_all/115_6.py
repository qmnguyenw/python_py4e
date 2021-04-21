Python | Convert string List to Nested Character List



Sometimes, while working with Python, we can have a problem in which we need
to perform interconversion of data. In this article we discuss converting
String list to Nested Character list split by comma. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using list comprehension +split()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate through list using list comprehension and can perform split
using split().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String List to Nested Character List

# using split() + list comprehension

 

# initialize list 

test_list = ["a, b, c", "gfg, is, best", "1, 2, 3"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert String List to Nested Character List

# using split() + list comprehension

res = [char.split(', ') for char in test_list]

 

# printing result

print("List after performing conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘a, b, c’, ‘gfg, is, best’, ‘1, 2, 3’]  
> List after performing conversion : [[‘a’, ‘b’, ‘c’], [‘gfg’, ‘is’, ‘best’],
> [‘1’, ‘2’, ‘3’]]

  

  

**Method #2 : Using map() + split() \+ lambda**  
The combination of above functions can be used to perform this task. In this,
we perform the task of iteration using map() and lambda function is used to
apply the logic of split using split() to all the list elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String List to Nested Character List

# using map() + split() + lambda

 

# initialize list 

test_list = ["a, b, c", "gfg, is, best", "1, 2, 3"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert String List to Nested Character List

# using map() + split() + lambda

res = list(map(lambda ele: ele.split(', '), test_list))

 

# printing result

print("List after performing conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘a, b, c’, ‘gfg, is, best’, ‘1, 2, 3’]  
> List after performing conversion : [[‘a’, ‘b’, ‘c’], [‘gfg’, ‘is’, ‘best’],
> [‘1’, ‘2’, ‘3’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

