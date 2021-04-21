Python Program to Replace all Occurrences of ‘a’ with $ in a String



Given a string, the task is to write a Python program to replace all
occurrence of ‘a’ with $.

 **Examples:**

    
    
     **Input:** Ali has all aces
    **Output:** $li h$s $ll $ces
    
    **Input:** All Exams are over
    **Output:** $ll Ex$ms $re Over

The **first approach** uses splitting of the given specified string into a set
of characters. An empty string variable is used to store modified string . We
loop over the character array and check if the character at this index is
equivalent to ‘a’ , and then append ‘$’ sign, in case the condition is
satisfied. Otherwise, the original character is copied into the new string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring a string variable

str = "Amdani athani kharcha rupaiya."

 

# declaring an empty string variable for storing modified string

modified_str = ''

 

# iterating over the string

for char in range(0, len(str)):

 # checking if the character at char index is equivalent to 'a'

 if(str[char] == 'a'):

 # append $ to modified string

 modified_str += '$'

 else:

 # append original string character

 modified_str += str[char]

 

print("Modified string : ")

print(modified_str)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Modified string :
    $md$ni $th$ni kh$rch$ rup$iy$.

The **second approach** uses the inbuilt method replace() to replace all the
occurrences of a particular character in the string with the new specified
character. The method has the following syntax :

    
    
    replace( oldchar , newchar)

This method doesn’t change the original string, and the result has to be
explicitly stored in the String variable.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring a string variable

str = "An apple A day keeps doctor Away."

 

# replacing character a with $ sign

str = str.replace('a', '$')

print("Modified string : ")

print(str)  
  
---  
  
 __

 __

 **Output:**

    
    
    Modified string :
    $n $pple $ d$y keeps doctor $w$y.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

