Python String | replace()



 **replace()** is an inbuilt function in Python programming language that
returns a copy of the string where all occurrences of a substring is replaced
with another substring.

 **Syntax :**

    
    
    string.replace(old, new, count)

 **Parameters :**

>  **old –** old substring you want to replace.  
>  **new –** new substring which would replace the old substring.
>
>  **count –** the number of times you want to replace the old substring with
> the new substring. ( **Optional** )
>
>  
>
>
>  
>

 **Return Value :**  
It returns a copy of the string where all occurrences of a substring is
replaced with another substring.

Below is the code demonstrating **_replace()_** :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the

# use of replace() method 

 

string = "geeks for geeks geeks geeks geeks"

 

# Prints the string by replacing geeks by Geeks 

print(string.replace("geeks", "Geeks")) 

 

# Prints the string by replacing only 3 occurrence of Geeks 

print(string.replace("geeks", "GeeksforGeeks", 3))  
  
---  
  
 __

 __

 **Output :**

    
    
    Geeks for Geeks Geeks Geeks Geeks
    GeeksforGeeks for GeeksforGeeks GeeksforGeeks geeks geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

