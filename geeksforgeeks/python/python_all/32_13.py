Python program to sort strings by substring range



Given a String List, sort by range of substrings.

>  **Input** : test_list = [“geeksforgeeks”, “best”, “geeks”, “preparation”,
> “interview”], i, j = 1, 3  
> **Output** : [‘geeksforgeeks’, ‘geeks’, ‘best’, ‘interview’, ‘preparation’]
>
>  **Explanation** : “eek” < “eek” < “est” < “nte” < “rep”.
>
>  **Input** : test_list = [“apple”, “orange”, “banana”], i, j = 2, 4  
> **Output** : [‘orange’, ‘banana’, ‘apple’]  
> **Explanation** : “ang” < “nan” < “ple”.

**Method #1 : Using sort() + slicing**

  

  

In this, we perform task of sorting using sort() and task of extracting a
range is done using slicing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings By Substring Range

# Using sort() + slicing

 

# helper function

def get_substr(test_str):

 

 # getting range

 return test_str[i : j]

 

# initializing list

test_list = ["geeksforgeeks", "best", "geeks",
"preparation"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

i, j = 1, 3

 

# calling func.

test_list.sort(key=get_substr)

 

# printing result 

print("Strings after sorting : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

> The original list is : [‘geeksforgeeks’, ‘best’, ‘geeks’, ‘preparation’]  
> Strings after sorting : [‘geeksforgeeks’, ‘geeks’, ‘best’, ‘preparation’]

 **Method #2 : Using lambda function + sort() + slicing**

In this, we perform slicing using lambda function rather than calling external
function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings By Substring Range

# Using lambda function + sort() + slicing

 

# initializing list

test_list = ["geeksforgeeks", "best", "geeks",
"preparation"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

i, j = 1, 3

 

# lambda function providing sort fnc.

test_list.sort(key=lambda test_str : test_str[i : j])

 

# printing result 

print("Strings after sorting : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

> The original list is : [‘geeksforgeeks’, ‘best’, ‘geeks’, ‘preparation’]  
> Strings after sorting : [‘geeksforgeeks’, ‘geeks’, ‘best’, ‘preparation’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

