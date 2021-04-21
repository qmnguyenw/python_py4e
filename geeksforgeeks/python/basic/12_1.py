Generating Strong Password using Python



Having a weak password is not good for a system that demands high
confidentiality and security of user credentials. It turns out that people
find it difficult to make up a strong password that is strong enough to
prevent unauthorized users from memorizing it.  

This article uses a mixture of numbers, alphabets, and other symbols found on
the computer keyboard to form a 12-character password which is unpredictable
and cannot easily be memorized.  

  * The components of the password are represented in the form of arrays.
  * Use the random method to select at least one character from each array of characters.
  * Since the 12-character password is required, so fill the rest of the length of the password left with randomly selected characters from an array formed from the combination of all the characters needed in the final password. Anytime the password is generated, shuffle the password using random.shuffle() to ensure that the final password does not follow a particular pattern.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import random

import array

# maximum length of password needed

# this can be changed to suit your password length

MAX_LEN = 12

# declare arrays of the character that we need in out password

# Represented as chars to enable easy string concatenation

DIGITS = ['0', '1', '2', '3', '4', '5', '6',
'7', '8', '9'] 

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e',
'f', 'g', 'h',

 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

 'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E',
'F', 'G', 'H',

 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',

 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

 'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?',
'.', '/', '|', '~', '>',

 '*', '(', ')', '<']

# combines all the character arrays above to form one array

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS
+ SYMBOLS

# randomly select at least one character from each character set above

rand_digit = random.choice(DIGITS)

rand_upper = random.choice(UPCASE_CHARACTERS)

rand_lower = random.choice(LOCASE_CHARACTERS)

rand_symbol = random.choice(SYMBOLS)

# combine the character randomly selected above

# at this stage, the password contains only 4 characters but

# we want a 12-character password

temp_pass = rand_digit + rand_upper + rand_lower +
rand_symbol

# now that we are sure we have at least one character from each

# set of characters, we fill the rest of

# the password length by selecting randomly from the combined

# list of character above.

for x in range(MAX_LEN - 4):

 temp_pass = temp_pass + random.choice(COMBINED_LIST)

 # convert temporary password into array and shuffle to

 # prevent it from having a consistent pattern

 # where the beginning of the password is predictable

 temp_pass_list = array.array('u', temp_pass)

 random.shuffle(temp_pass_list)

# traverse the temporary password array and append the chars

# to form the password

password = ""

for x in temp_pass_list:

 password = password + x

 

# print out password

print(password)  
  
---  
  
 __

 __

 **Output :**  

    
    
    yf2byU$@zTg5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

