Python program to remove the nth index character from a non-empty string



Given a String, the task is to write a Python program to remove the nth index
character from a non-empty string

 **Examples:**

    
    
     **Input:** str = "Stable"
    **Output:** Modified string after removing  4 th character 
    Stabe.
     
    **Input:** str = "Arrow"
    **Output:** Modified string after removing  4 th character 
    Arro

The **first approach** uses a new string variable for storing the modified
string. We keep a track of the characters of the string and as soon as we
encounter a character at nth index, we don’t copy it to the modified string
variable. Else, we copy it to a new variable.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring a string variable

str = "Geeksforgeeks is fun."

 

# index to remove character at

n = 4

 

# declaring an empty string variable for storing modified string

modified_str = ''

 

# iterating over the string

for char in range(0, len(str)):

 

 # checking if the char index is equivalent to n

 if(char != n):

 # append original string character

 modified_str += str[char]

 

print("Modified string after removing ", n, "th character ")

print(modified_str)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Modified string after removing  4 th character  
    Geekforgeeks is fun.

 **Time Complexity =** O(n), where n is the length of the string.

**Space Complexity =** O(n)

The **second approach** uses the idea of extraction of a sequence of
characters within a range of index values. The syntax used in Python is as
follows :

> **string_name[start_index : end_index]**  
>  – extracts the characters starting at start_index  
> and less than end_index, that is, up to end_index-1.  
> If we don’t specify the end_index, it computes till the length of the
> string.

Therefore, we extract all the characters of a string in two parts, first until
nth index and the other beginning with n+1th index. We then append these two
parts together.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring a string variable

str = "Geeksforgeeks is fun."

 

# index to remove character at

n = 8

 

# extracts 0 to n-1th index

first_part = str[0:n]

 

# extracts characters from n+1th index until the end

second_part = str[n+1:]

print("Modified string after removing ", n, "th character ")

 

# combining both the parts together

print(first_part+second_part)  
  
---  
  
 __

 __

 **Output:**

    
    
    Modified string after removing  8 th character  
    Geeksforeeks is fun.

 **Time Complexity =** O(n), where n is the length of the string.

 **Space Complexity =** O(n)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

