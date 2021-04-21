Python | Dictionary creation using list contents



Sometimes we need to handle the data coming in the list format and convert
list into dictionary format. This particular problem is quite common while we
deal with Machine Learning to give further inputs in changed formats. Let’s
discuss certain ways in which this inter conversion happens.

 **Method #1 : Using dictionary comprehension +zip()**

In this method, we use dictionary comprehension to perform the iteration and
logic part, the binding of all the lists into one dictionary and with
associated keys is done by zip function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dictionary creation using list contents

# using Dictionary comprehension + zip()

 

# initializing list

keys_list = ["key1", "key2"]

nested_name = ["Manjeet", "Nikhil"]

nested_age = [22, 21]

 

# printing original lists

print("The original key list : " + str(keys_list))

print("The original nested name list : " + str(nested_name))

print("The original nested age list : " + str(nested_age))

 

# using Dictionary comprehension + zip()

# Dictionary creation using list contents

res = {key: {'name': name, 'age': age} for key, name, age
in

 zip(keys_list, nested_name, nested_age)}

 

# print result

print("The dictionary after construction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original key list : [‘key1’, ‘key2’]  
> The original nested name list : [‘Manjeet’, ‘Nikhil’]  
> The original nested age list : [22, 21]  
> The dictionary after construction : {‘key1’: {‘age’: 22, ‘name’: ‘Manjeet’},
> ‘key2’: {‘age’: 21, ‘name’: ‘Nikhil’}}
>
>  
>
>
>  
>

**Method #2 : Using dictionary comprehension +enumerate()**

The similar task can be performed using enumerate function that was
performed by the zip function. The dictionary comprehension performs the task
similar as above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dictionary creation using list contents

# using dictionary comprehension + enumerate()

 

# initializing list

keys_list = ["key1", "key2"]

nested_name = ["Manjeet", "Nikhil"]

nested_age = [22, 21]

 

# printing original lists

print("The original key list : " + str(keys_list))

print("The original nested name list : " + str(nested_name))

print("The original nested age list : " + str(nested_age))

 

# using dictionary comprehension + enumerate()

# Dictionary creation using list contents

res = {val : {"name": nested_name[key], "age": nested_age[key]}

 for key, val in enumerate(keys_list)}

 

# print result

print("The dictionary after construction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original key list : [‘key1’, ‘key2’]  
> The original nested name list : [‘Manjeet’, ‘Nikhil’]  
> The original nested age list : [22, 21]  
> The dictionary after construction : {‘key1’: {‘age’: 22, ‘name’: ‘Manjeet’},
> ‘key2’: {‘age’: 21, ‘name’: ‘Nikhil’}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

