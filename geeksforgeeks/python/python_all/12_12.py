Python program to find the String in a List



Given a list, the task is to write a Python program to check whether a list
contains a particular string or not.

 **Examples:**

>  **Input** : l=[1, 1.0, ‘have’, ‘a’, ‘geeky’, ‘day’]; s=’geeky’
>
>  **Output:** geeky is present in the list
>
>  **Input:** l=[‘hello’,’ geek’, ‘have’, ‘a’, ‘geeky’, ‘day’]; s=’nice’
>
>  
>
>
>  
>
>
>  **Output:** nice is not present in the list

 **Method #1:** Using in operator

The _in_ operator comes handy for checking if a particular string/element
exists in the list or not.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# assign list

l = [1, 2.0, 'have', 'a', 'geeky', 'day']

 

# assign string

s = 'geeky'

 

# check if string is present in the list

if s in l:

 print(f'{s} is present in the list')

else:

 print(f'{s} is not present in the list')  
  
---  
  
 __

 __

 **Output:**

    
    
    geeky is present in the list

 **Method #2:** Using count() function

The _count()_ function is used to count the occurrence of a particular string
in the list. If the count of a string is more than 0, it means that particular
string exists in the list, else that string doesn’t exist in the list.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# assing list

l = ['1', 1.0, 32, 'a', 'geeky', 'day']

 

# assign string

s = 'prime'

 

# check if string is present in list

if l.count(s) > 0:

 print(f'{s} is present in the list')

else:

 print(f'{s} is not present in the list')  
  
---  
  
 __

 __

 **Output:**

    
    
    prime is not present in the list

 **Method #3:** Using List Comprehension

List comprehensions are used for creating new lists from other iterables like
tuples, strings, arrays, lists, etc. It is used to transform iterative
statements into formulas.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# assign list

l = ['hello', 'geek', 'have', 'a', 'geeky',
'day']

 

# assign string

s = 'geek'

 

# list comprehension

compre = [i for i in l if s in l]

 

# check if sting is present in list

if len(compre) > 0:

 print(f'{s} is present in the list')

else:

 print(f'{s} is not present in the list')  
  
---  
  
 __

 __

 **Output:**

    
    
    geeky is present in the list

 **Method #4:** Using any() function

The _any()_ function is used to check the existence of an element in the list.
it’s like- if any element in the string matches the input element, print that
the element is present in the list, else, print that the element is not
present in the list.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# assign list

l = ['hello', 'geek', 'have', 'a', 'geeky',
'day']

 

# assign string

s = 'prime'

 

# check if string is present in list

if any(s in i for i in l):

 print(f'{s} is present in the list')

else:

 print(f'{s} is not present in the list')  
  
---  
  
 __

 __

 **Output:**

    
    
    prime is not present in the list

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

