Python – Convert List to List of dictionaries



Given list values and keys list, convert these values to key value pairs in
form of list of dictionaries.

>  **Input** : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]  
>  **Output** : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]  
>  **Explanation** : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.
>
>  **Input** : test_list = [“Gfg”, 10], key_list = [“name”, “id”]  
>  **Output** : [{‘name’: ‘Gfg’, ‘id’: 10}]  
>  **Explanation** : Conversion of lists to list of records by keys mapping.

 **Method #1 : Using loop + dictionary comprehension**

This is one of the ways in which this task can be performed. In this, we
perform mapping values using dictionary comprehension. The iteration is
performed using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to List of dictionaries

# Using dictionary comprehension + loop

 

# initializing lists

test_list = ["Gfg", 3, "is", 8, "Best", 10,
"for", 18, "Geeks", 33]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing key list 

key_list = ["name", "number"]

 

# loop to iterate through elements

# using dictionary comprehension

# for dictionary construction

n = len(test_list)

res = []

for idx in range(0, n, 2):

 res.append({key_list[0]: test_list[idx], key_list[1] :
test_list[idx + 1]})

 

# printing result 

print("The constructed dictionary list : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [‘Gfg’, 3, ‘is’, 8, ‘Best’, 10, ‘for’, 18, ‘Geeks’, 33]  
> The constructed dictionary list : [{‘name’: ‘Gfg’, ‘number’: 3}, {‘name’:
> ‘is’, ‘number’: 8}, {‘name’: ‘Best’, ‘number’: 10}, {‘name’: ‘for’,
> ‘number’: 18}, {‘name’: ‘Geeks’, ‘number’: 33}]

 **Method #2 : Using dictionary comprehension + list comprehension**

The combination of above functions is used to solve this problem. In ths, we
perform a similar task as above method. But difference is that its performed
as shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to List of dictionaries

# Using zip() + list comprehension

 

# initializing lists

test_list = ["Gfg", 3, "is", 8, "Best", 10,
"for", 18, "Geeks", 33]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing key list 

key_list = ["name", "number"]

 

# using list comprehension to perform as shorthand

n = len(test_list)

res = [{key_list[0]: test_list[idx], key_list[1]: test_list[idx
+ 1]}

 for idx in range(0, n, 2)]

 

# printing result 

print("The constructed dictionary list : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [‘Gfg’, 3, ‘is’, 8, ‘Best’, 10, ‘for’, 18, ‘Geeks’, 33]  
> The constructed dictionary list : [{‘name’: ‘Gfg’, ‘number’: 3}, {‘name’:
> ‘is’, ‘number’: 8}, {‘name’: ‘Best’, ‘number’: 10}, {‘name’: ‘for’,
> ‘number’: 18}, {‘name’: ‘Geeks’, ‘number’: 33}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

