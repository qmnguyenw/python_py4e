Python | Extract Score list of String



Sometimes, while programming we can have a problem in which we dedicate to
each character of alphabets a particular score and then according to string,
extract only those score for further computations. This can have application
in gaming domain. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension +ord()**  
The combination of above functions can be used to perform this task. In this,
we perform the task of element iteration using list comprehension and ord()
perform the task of checking for index of list that has to be returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Score list of String

# using list comprehension + ord()

 

# initialize list and string 

test_list = [3, 4, 5, 7, 5, 8, 1, 5,
7, 10,

 6, 7, 9, 11, 3, 1, 3, 6, 7, 9,

 7, 4, 6, 4, 2, 1]

 

test_str = "geeksforgeeks"

 

# printing original list and string

print("The original list : " + str(test_list))

print("The original string : " + str(test_str))

 

# Extract Score list of String

# using list comprehension + ord()

res = [test_list[ord(ele) - 97] for ele in test_str]

 

# printing result

print("The Score list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [3, 4, 5, 7, 5, 8, 1, 5, 7, 10, 6, 7, 9, 11, 3, 1, 3, 6,
> 7, 9, 7, 4, 6, 4, 2, 1]  
> The original string : geeksforgeeks  
> The Score list is : [1, 5, 5, 6, 7, 8, 3, 6, 1, 5, 5, 6, 7]

  

  

**Method #2 : Usingzip() + ascii_lowercase + dict() \+ list comprehension**  
The combination of above functions can also be used to perform this task. In
this, the task of joining list element score to character is done by zip() and
list comprehension is used to output the final result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Score list of String

# using list comprehension + zip() + ascii_lowercase + dict()

import string

 

# initialize list and string 

test_list = [3, 4, 5, 7, 5, 8, 1, 5,
7, 10,

 6, 7, 9, 11, 3, 1, 3, 6, 7, 9,

 7, 4, 6, 4, 2, 1]

 

test_str = "geeksforgeeks"

 

# printing original list and string

print("The original list : " + str(test_list))

print("The original string : " + str(test_str))

 

# Extract Score list of String

# using list comprehension + zip() + ascii_lowercase + dict()

temp = dict(zip(string.ascii_lowercase, test_list))

res = [temp[ele] for ele in test_str]

 

# printing result

print("The Score list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [3, 4, 5, 7, 5, 8, 1, 5, 7, 10, 6, 7, 9, 11, 3, 1, 3, 6,
> 7, 9, 7, 4, 6, 4, 2, 1]  
> The original string : geeksforgeeks  
> The Score list is : [1, 5, 5, 6, 7, 8, 3, 6, 1, 5, 5, 6, 7]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

