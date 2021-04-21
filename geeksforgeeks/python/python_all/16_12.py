Python – Reverse a words in a line and keep the special characters untouched



Reverse the characters in all words in a line including numbers, but leave
special characters and symbols untouched in the same position. Consider the
below examples.

>  **Input:** ‘Bangalore is@#$!123 locked again in jul2020’ should change to  
>  **Output:** ‘erolagnaB si@#$!321 dekcol niaga ni 0202luj’
>
>  **Input:** ‘Bangalore is@#$!123locked locked again in jul2020’ should
> change to  
>  **Output:** ‘erolagnaB si@#$!dekcol321 dekcol niaga ni 0202luj’

Look at the above example, each word is reversed, if there is any special
character, then the word surrounding the special character gets reversed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def reverStringsInLine(s):

 

 sl = s.split(' ')

 rsl = ''

 

 for word in sl:

 str_word = ''

 rev_sub_word = ''

 

 for ch in word:

 

 if ch.isalnum():

 str_word += ch

 

 else:

 

 # If it is special character, then 

 # reverse non special characters and 

 # append special character

 

 rev_sub_word += str_word[::-1] + ch

 

 # Clear the old stached character, as

 # it is already reversed

 str_word = ''

 

 # Keep appening each words, aslo add words

 # ending with non-special character

 r_word = rev_sub_word + str_word[::-1]

 rsl += r_word + ' '

 return rsl

 

 

s = 'Bangalore is@#$!123locked locked again in jul2020'

 

print(reverStringsInLine(s))  
  
---  
  
 __

 __

 **Output:**

    
    
    erolagnaB si@#$!dekcol321 dekcol niaga ni 0202luj 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

