Python – Get Last N characters of a string



Given a string and an integer N, the task is to write a python program to
print the last N characters of the string.

**Example:**

>  **Input:** Geeks For Geeks!; N = 4
>
>  **Output:** eks!
>
>  **Explanation:** The given string is Geeks For Geeks! and the last 4
> characters is eks!.
>
>  
>
>
>  
>
>
>  **Input:** PYTHON; N=1
>
>  **Output:** N
>
>  **Explanation:** The given string is PYTHON and the last character is N.

 **Method 1:** Using a loop to get to the last N characters of the given
string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# get input

Str = "Geeks For Geeks!"

N = 4

 

# print the string

print(Str)

 

# iterate loop

while(N > 0):

 

 # print character

 print(Str[-N], end='')

 

 # decrement the value of N

 N = N-1  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks For Geeks!
    eks!

 **Method 2:** Using list slicing to print the last n characters of the given
string. ****

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# get input

Str = "Geeks For Geeks!"

N = 4

 

# print the string

print(Str)

 

# get length of string

length = len(Str)

 

# create a new string of last N characters

Str2 = Str[length - N:]

 

# print Last N characters

print(Str2)  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks For Geeks!
    eks!

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

