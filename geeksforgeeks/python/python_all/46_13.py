Python program to check if a string has at least one letter and one number



Given a string in Python. The task is to check whether the string has at least
one letter(character) and one number. Return “True” if the given string full
fill above condition else return “False” (without quotes).  
 **Examples:**

    
    
    **Input:** welcome2ourcountry34
    **Output:** True
    
    **Input:** stringwithoutnum
    **Output:** False
    

**Approach:**  
The approach is simple we will use loop and two flags for letter and number.
These flags will check whether the string contains letter and number. In the
end, we will take AND of both flags to check if both are true or not. Letters
can be checked in Python String using the isalpha() method and numbers can be
checked using the isdigit() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def checkString(str):

 

 # intializing flag variable

 flag_l = False

 flag_n = False

 

 # checking for letter and numbers in 

 # given string

 for i in str:

 

 # if string has letter

 if i.isalpha():

 flag_l = True

 

 # if string has number

 if i.isdigit():

 flag_n = True

 

 # returning and of flag

 # for checking required condition

 return flag_l and flag_n

 

 

# driver code

print(checkString('thishasboth29'))

print(checkString('geeksforgeeks'))  
  
---  
  
 __

 __

 **Output** :

    
    
    True
    False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

