Python String find()



The find() method returns the lowest index of the substring if it is found in
given string. If its is not found then it returns -1.  
Syntax :

> str.find(sub,start,end)

 **Parameters :**

>  **sub :** It’s the substring which needs to be searched in the given
> string.  
>  **start :** Starting position where sub is needs to be checked within the
> string.  
>  **end :** Ending position where suffix is needs to be checked within the
> string.

 **NOTE :** If start and end indexes are not provided then by default it takes
0 and length-1 as starting and ending indexes where ending indxes is not
included in our search.

  

  

 **Returns:**

> returns the lowest index of the substring if it is found in given string. If
> it’s not found then it returns -1.

The find() method is similar to index(). The only difference is find() returns
-1 if searched string is not found and index() throws an exception in this
case.

 **CODE 1**

 __

 __  
 __

 __

 __  
 __  
 __

word= 'geeks for geeks'

 

# returns first occurrence of Substring

result = word.find('geeks')

print ("Substring 'geeks' found at index:", result )

 

result = word.find('for')

print ("Substring 'for ' found at index:", result )

 

# How to use find()

if (word.find('pawan') != -1):

 print ("Contains given substring ")

else:

 print ("Doesn't contains given substring")  
  
---  
  
 __

 __

 **Output:**

    
    
    Substring 'geeks' found at index: 0
    Substring 'for ' found at index: 6
    Doesn't contains given substring
    

**CODE 2**

 __

 __  
 __

 __

 __  
 __  
 __

word= 'geeks for geeks'

 

# Substring is searched in 'eks for geeks' 

print(word.find('ge', 2)) 

 

# Substring is searched in 'eks for geeks' 

print(word.find('geeks ', 2)) 

 

# Substring is searched in 's for g' 

print(word.find('g', 4, 10)) 

 

# Substring is searched in 's for g' 

print(word.find('for ', 4, 11))   
  
---  
  
__

__

**Output:**

    
    
    10
    -1
    -1
    6
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

