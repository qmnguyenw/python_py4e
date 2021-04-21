Python | Split dictionary of lists to list of dictionaries



Conversion from one data type to other is essential in various facets of
programming. Be it development or competitive programming. Hence knowledge of
it is quite useful and necessary.

Let’s discuss certain methods by which dictionary of list can be converted to
the corresponding list of dictionaries.

 **Method #1 : Using list comprehension**  
We can use list comprehension as the one-liner alternative to perform various
naive tasks providing readability with a more concise code. We can iterate
through each of dictionary element and corresponding keep constructing the
list of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to convert dictionary of list to 

# list of dictionaries

# using list comprehension

 

# initializing dictionary

test_dict = { "Rash" : [1, 3], "Manjeet" : [1,
4], "Akash" : [3, 4] }

 

# printing original dictionary

print ("The original dictionary is : " + str(test_dict))

 

# using list comprehension

# to convert dictionary of list to 

# list of dictionaries

res = [{key : value[i] for key, value in test_dict.items()}

 for i in range(2)]

 

# printing result

print ("The converted list of dictionaries " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Rash’: [1, 3], ‘Manjeet’: [1, 4], ‘Akash’:
> [3, 4]}  
> The converted list of dictionaries [{‘Rash’: 1, ‘Manjeet’: 1, ‘Akash’: 3},
> {‘Rash’: 3, ‘Manjeet’: 4, ‘Akash’: 4}]
>
>  
>
>
>  
>

  
**Method #2 : Usingzip()**  
This approach used zip function two times, first time when we need to zip
the particular index value of all lists as one and second to get all values of
particular index and zip it with the corresponding keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to convert dictionary of list to 

# list of dictionaries

# using zip()

 

# initializing dictionary

test_dict = { "Rash" : [1, 3], "Manjeet" : [1,
4], "Akash" : [3, 4] }

 

# printing original dictionary

print ("The original dictionary is : " + str(test_dict))

 

# using zip()

# to convert dictionary of list to 

# list of dictionaries

res = [dict(zip(test_dict, i)) for i in
zip(*test_dict.values())]

 

# printing result

print ("The converted list of dictionaries " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Rash’: [1, 3], ‘Akash’: [3, 4], ‘Manjeet’:
> [1, 4]}  
> The converted list of dictionaries [{‘Rash’: 1, ‘Akash’: 3, ‘Manjeet’: 1},
> {‘Rash’: 3, ‘Akash’: 4, ‘Manjeet’: 4}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

