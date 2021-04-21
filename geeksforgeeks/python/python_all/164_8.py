Python | Convert case of elements in a list of strings



Given a list of strings, write a Python program to convert all string from
lowercase/uppercase to uppercase/lowercase.

    
    
     **Input :** ['GeEk', 'FOR', 'gEEKS']
    **Output:** ['geeks', 'for', 'geeks']
    
    **Input :** ['fun', 'Foo', 'BaR']
    **Output:** ['FUN', 'FOO', 'BAR']

  
**Method #1 :** Convert Uppercase to Lowercase using map function

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert all string

# from uppercase to lowercase.

 

# Using map function

out = map(lambda x:x.lower(), ['GeEk', 'FOR',
'gEEKS'])

 

# Converting it into list

output = list(out)

 

# printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['geek', 'for', 'geeks']
    

  
**Method #2:** Convert Lowercase to Uppercase using List comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert all string

# from uppercase to lowercase.

 

# Initialisation

input = ['fun', 'Foo', 'BaR']

 

# Converting

lst = [x.upper() for x in input]

 

# printing output

print(lst)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['FUN', 'FOO', 'BAR']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

