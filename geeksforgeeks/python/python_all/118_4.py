Python | Find Mixed Combinations of string and list



Sometimes, while working with Python, we can have a problem in which we need
to make combinations of string and character list. This type of problem can
come in domains in which we need to interleave the data. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop +enumerate() + replace()**  
This task can be performed using combination of above functions. In this, we
just iterate each element of character list and insert each combination using
brute force way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mixed Combinations of string and list

# using loop + enumerate() + replace()

 

# initialize list and string 

test_list = ["a", "b", "c"]

test_str = "gfg"

 

# printing original list and string

print("The original list : " + str(test_list))

print("The original string : " + test_str)

 

# Mixed Combinations of string and list

# using loop + enumerate() + replace()

res = []

for idx, ele in enumerate(test_str):

 res += [test_str[ : idx] + test_str[idx : ].replace(ele, k,
1)

 for k in test_list]

 

# printing result

print("The list after mixed Combinations : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘a’, ‘b’, ‘c’]  
> The original string : gfg  
> The list after mixed Combinations : [‘afg’, ‘bfg’, ‘cfg’, ‘gag’, ‘gbg’,
> ‘gcg’, ‘gfa’, ‘gfb’, ‘gfc’]

  

  

**Method #2 : Using list comprehension**  
The above functionality can be used to perform this task. In this, we provide
a one-line alternative using comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mixed Combinations of string and list

# using list comprehension

 

# initialize list and string 

test_list = ["a", "b", "c"]

test_str = "gfg"

 

# printing original list and string

print("The original list : " + str(test_list))

print("The original string : " + test_str)

 

# Mixed Combinations of string and list

# using list comprehension

res = [test_str[ : idx] + ele + test_str[idx + 1 : ]\

 for idx in range(len(test_str)) for ele in test_list]

 

# printing result

print("The list after mixed Combinations : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘a’, ‘b’, ‘c’]  
> The original string : gfg  
> The list after mixed Combinations : [‘afg’, ‘bfg’, ‘cfg’, ‘gag’, ‘gbg’,
> ‘gcg’, ‘gfa’, ‘gfb’, ‘gfc’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

