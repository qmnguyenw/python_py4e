Python | Clearing list as dictionary value



Clearing a list is a common problem and solution to it has been discussed many
times. But sometimes, we don’t have a native list but list is a value to
dictionary key. Clearing it is not as easy as clearing an original list. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Using loop +clear()**  
This is the most generic method in which we can perform this particular
function. We just run a loop till the last dictionary key and clear the key’s
list value as they occur using clear function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# clearing list as dict. value

# using loop + clear()

 

# initializing dict.

test_dict = {"Akash" : [1, 4, 3],

 "Nikhil" : [3, 4, 1],

 "Akshat" : [7, 8]}

 

# printing original dict

print("The original dict : " + str(test_dict))

 

# using loop + clear()

# clearing list as dict. value

for key in test_dict:

 test_dict[key].clear()

 

# print result

print("The dictionary after clearing value list : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dict : {‘Nikhil’: [3, 4, 1], ‘Akshat’: [7, 8], ‘Akash’: [1, 4,
> 3]}  
> The dictionary after clearing value list : {‘Nikhil’: [], ‘Akshat’: [],
> ‘Akash’: []}

  

  

**Method #2 : Using dictionary comprehension**  
We can reduce the lines of code and merge the above functionality using just
the dictionary comprehension and clearing the list using the list re-
initialization.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# clearing list as dict. value

# using dictionary comprehension

 

# initializing dict.

test_dict = {"Akash" : [1, 4, 3],

 "Nikhil" : [3, 4, 1],

 "Akshat" : [7, 8]}

 

# printing original dict

print("The original dict : " + str(test_dict))

 

# using dictionary comprehension

# clearing list as dict. value

test_dict = {key : [] for key in test_dict}

 

# print result

print("The dictionary after clearing value list : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dict : {‘Nikhil’: [3, 4, 1], ‘Akshat’: [7, 8], ‘Akash’: [1, 4,
> 3]}  
> The dictionary after clearing value list : {‘Nikhil’: [], ‘Akshat’: [],
> ‘Akash’: []}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

