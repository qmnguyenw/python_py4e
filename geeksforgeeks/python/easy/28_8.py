Morse Code Translator In Python



Morse code is a method of transmitting text information as a series of on-off
tones, lights, or clicks that can be directly understood by a skilled listener
or observer without special equipment. It is named for Samuel F. B. Morse, an
inventor of the telegraph.

 **Algorithm**

The algorithm is very simple. Every character in the English language is
substituted by a series of ‘dots’ and ‘dashes’ or sometimes just singular
‘dot’ or ‘dash’ and vice versa.  
Please refer this wikipedia image for details.

 **Encryption**

  1. In case of encryption we extract each character (if not a space) from a word one at a time and match it with its corresponding morse code stored in whichever data structure we have chosen(if you are coding in python, dictionaries can turn out to be very useful in this case)
  2. Store the morse code in a variable which will contain our encoded string and then we add a space to our string which will contain the result.
  3. While encoding in morse code we need to add 1 space between every character and 2 consecutive spaces between every word.
  4. If the character is a space then add another space to the variable containing the result. We repeat this process till we traverse the whole string

 **Decryption**

  

  

  1. In case of decryption, we start by adding a space at the end of the string to be decoded (this will be explained later).
  2. Now we keep extracting characters from the string till we are not getting any space.
  3. As soon as we get a space we look up the corresponding English language character to the extracted sequence of characters (or our morse code) and add it to a variable which will store the result.
  4. Remember keeping track of the space is the most important part of this decryption process. As soon as we get 2 consecutive spaces we will add another space to our variable containing the decoded string.
  5. The last space at the end of the string will help us identify the last sequence of morse code characters (since a space acts as a check for extracting characters and start decoding them).

 **Implementation**

Python provides a data structure called dictionary which stores information in
the form of key-value pairs which is very convenient for implementing a cipher
such as the morse code. We can save the morse code chart in a dictionary where
**(key-value pairs) = > (English Characters-Morse Code)**. The plaintext
(English characters) take the place of keys and the ciphertext (Morse code)
form the values of the corresponding keys. The values of keys can be accessed
from the dictionary in the same way we access the values of an array through
their index and vice versa.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to implement Morse Code Translator

 

'''

VARIABLE KEY

'cipher' -> 'stores the morse translated form of the english string'

'decipher' -> 'stores the english translated form of the morse string'

'citext' -> 'stores morse code of a single character'

'i' -> 'keeps count of the spaces between morse characters'

'message' -> 'stores the string to be encoded or decoded'

'''

 

# Dictionary representing the morse code chart

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',

 'C':'-.-.', 'D':'-..', 'E':'.',

 'F':'..-.', 'G':'--.', 'H':'....',

 'I':'..', 'J':'.---', 'K':'-.-',

 'L':'.-..', 'M':'--', 'N':'-.',

 'O':'---', 'P':'.--.', 'Q':'--.-',

 'R':'.-.', 'S':'...', 'T':'-',

 'U':'..-', 'V':'...-', 'W':'.--',

 'X':'-..-', 'Y':'-.--', 'Z':'--..',

 '1':'.----', '2':'..---', '3':'...--',

 '4':'....-', '5':'.....', '6':'-....',

 '7':'--...', '8':'---..', '9':'----.',

 '0':'-----', ', ':'--..--', '.':'.-.-.-',

 '?':'..--..', '/':'-..-.', '-':'-....-',

 '(':'-.--.', ')':'-.--.-'}

 

# Function to encrypt the string

# according to the morse code chart

def encrypt(message):

 cipher = ''

 for letter in message:

 if letter != ' ':

 

 # Looks up the dictionary and adds the

 # correspponding morse code

 # along with a space to separate

 # morse codes for different characters

 cipher += MORSE_CODE_DICT[letter] + ' '

 else:

 # 1 space indicates different characters

 # and 2 indicates different words

 cipher += ' '

 

 return cipher

 

# Function to decrypt the string

# from morse to english

def decrypt(message):

 

 # extra space added at the end to access the

 # last morse code

 message += ' '

 

 decipher = ''

 citext = ''

 for letter in message:

 

 # checks for space

 if (letter != ' '):

 

 # counter to keep track of space

 i = 0

 

 # storing morse code of a single character

 citext += letter

 

 # in case of space

 else:

 # if i = 1 that indicates a new character

 i += 1

 

 # if i = 2 that indicates a new word

 if i == 2 :

 

 # adding space to separate words

 decipher += ' '

 else:

 

 # accessing the keys using their values (reverse of encryption)

 decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT

 .values()).index(citext)]

 citext = ''

 

 return decipher

 

# Hard-coded driver function to run the program

def main():

 message = "GEEKS-FOR-GEEKS"

 result = encrypt(message.upper())

 print (result)

 

 message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ...
"

 result = decrypt(message)

 print (result)

 

# Executes the main function

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

    
    
    **Output:**
    --. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... 
    GEEKS-FOR-GEEKS
    

This article is contributed by Palash Nigam . If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

