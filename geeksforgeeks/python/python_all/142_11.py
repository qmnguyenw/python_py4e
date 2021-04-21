Python | Replace substring in list of strings



While working with strings, one of the most used application is replacing the
part of string with another. Since string in itself is immutable, the
knowledge of this utility in itself is quite useful. Here the replacement of a
substring in list of string is performed. Let’s discuss certain ways in which
this can be performed.

 **Method #1 : Using list comprehension +replace()**  
The replace method can be coupled with the list comprehension technique to
achieve this particular task. List comprehension performs the task of
iterating through the list and replace method replaces the section of
substring with another.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace substring in list of strings

# using list comprehension + replace()

 

# initializing list 

test_list = ['4', 'kg', 'butter', 'for', '40',
'bucks']

 

# printing original list 

print("The original list : " + str(test_list ))

 

# using list comprehension + replace()

# Replace substring in list of strings

res = [sub.replace('4', '1') for sub in test_list]

 

# print result

print("The list after substring replacement : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['4', 'kg', 'butter', 'for', '40', 'bucks']
    The list after substring replacement : ['1', 'kg', 'butter', 'for', '10', 'bucks']
    

**Method #2 : Usingmap() \+ lambda + replace()**  
The combination of these functions can also be used to perform this particular
task. The map and lambda help to perform the task same as list comprehension
and replace method is used to perform the replace functionality. But this
method is poor when it comes to performance than method above.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace substring in list of strings

# using list comprehension + map() + lambda

 

# initializing list 

test_list = ['4', 'kg', 'butter', 'for', '40',
'bucks']

 

# printing original list 

print("The original list : " + str(test_list ))

 

# using list comprehension + map() + lambda

# Replace substring in list of strings

res = list(map(lambda st: str.replace(st, "4",
"1"), test_list))

 

# print result

print("The list after substring replacement : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['4', 'kg', 'butter', 'for', '40', 'bucks']
    The list after substring replacement : ['1', 'kg', 'butter', 'for', '10', 'bucks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

