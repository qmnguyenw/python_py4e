Python String | split()



 **split()** method returns a list of strings after breaking the given string
by the specified separator.

>  **Syntax :** str.split(separator, maxsplit)
>
>  **Parameters :**  
>  **separator :** This is a delimiter. The string splits at this specified
> separator. If is not provided then any white space is a separator.
>
>  **maxsplit :** It is a number, which tells us to split the string into
> maximum of provided number of times. If it is not provided then there is no
> limit.
>
>  **Returns :** Returns a list of strings after breaking the given string by
> the specified separator.
>
>  
>
>
>  
>

 **CODE 1**

 __

 __  
 __

 __

 __  
 __  
 __

text= 'geeks for geeks'

 

# Splits at space

print(text.split())

 

word = 'geeks, for, geeks'

 

# Splits at ','

print(word.split(','))

 

word = 'geeks:for:geeks'

 

# Splitting at ':'

print(word.split(':'))

 

word = 'CatBatSatFatOr'

 

# Splitting at 3

print([word[i:i+3] for i in range(0, len(word),
3)])  
  
---  
  
 __

 __

Output :

    
    
    ['geeks', 'for', 'geeks']
    ['geeks', 'for', 'geeks']
    ['geeks', 'for', 'geeks']
    ['Cat', 'Bat', 'Sat', 'Fat', 'Or']

 **CODE 2**

 __

 __  
 __

 __

 __  
 __  
 __

word= 'geeks, for, geeks, pawan'

 

# maxsplit: 0

print(word.split(', ', 0))

 

# maxsplit: 4

print(word.split(', ', 4))

 

# maxsplit: 1

print(word.split(', ', 1))  
  
---  
  
 __

 __

Output :

    
    
    ['geeks, for, geeks, pawan']
    ['geeks', 'for', 'geeks', 'pawan']
    ['geeks', 'for, geeks, pawan']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

