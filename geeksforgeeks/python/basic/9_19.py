Substitution Cipher



Hiding some data is known as encryption. When plain text is encrypted it
becomes unreadable and is known as ciphertext. In a Substitution cipher, any
character of plain text from the given fixed set of characters is substituted
by some other character from the same set depending on a key. For example with
a shift of 1, A would be replaced by B, B would become C, and so on.

 **Note:** Special case of Substitution cipher is known as Caesar cipher where
the key is taken as 3.

#### Mathematical representation

The encryption can be represented using modular arithmetic by first
transforming the letters into numbers, according to the scheme, A = 0, B =
1,…, Z = 25. Encryption of a letter by a shift n can be described
mathematically as.

![E_n\(x\)=\(x+n\)mod\\ 26](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c8ec2929f6200eac3e62ce0606b45a7d_l3.svg)  
(Encryption Phase with shift n)

![D_n\(x\)=\(x-n\)mod\\ 26](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2fa18340a62f44efc5fc32cb361a047e_l3.svg)  
(Decryption Phase with shift n)

  

  

![substitution-cipher](https://media.geeksforgeeks.org/wp-
content/uploads/20191216171403/substitution-cipher-300x126.png)

 **Examples:**

    
    
    **Plain Text:** I am studying Data Encryption
    **Key:** 4
    **Output:** M eq wxyhCmrk Hexe IrgvCtxmsr
    
    **Plain Text:** ABCDEFGHIJKLMNOPQRSTUVWXYZ
    **Key:** 4
    **Output:** EFGHIJKLMNOPQRSTUVWXYZabcd
    

**Algorithm for Substitution Cipher:**  
 **Input:**

  * A String of both lower and upper case letters, called PlainText.
  * An Integer denoting the required key.

 **Procedure:**

  * Create a list of all the characters.
  * Create a dictionary to store the subtitution for all characters.
  * For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.
  * Print the new string generated.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Substitution Cipher

 

 

import string

 

 

# A list containing all characters

all_letters= string.ascii_letters

 

 

""" 

create a dictionary to store the substitution 

for the given alphabet in the plain text 

based on the key

"""

 

 

dict1 = {}

key = 4

 

for i in range(len(all_letters)):

 dict1[all_letters[i]] =
all_letters[(i+key)%len(all_letters)]

 

 

plain_txt= "I am studying Data Encryption"

cipher_txt=[]

 

# loop to generate ciphertext

 

for char in plain_txt:

 if char in all_letters:

 temp = dict1[char]

 cipher_txt.append(temp)

 else:

 temp =char

 cipher_txt.append(temp)

 

cipher_txt= "".join(cipher_txt)

print("Cipher Text is: ",cipher_txt)

 

 

""" 

create a dictionary to store the substitution

for the given alphabet in the cipher 

text based on the key

"""

 

 

dict2 = {} 

for i in range(len(all_letters)):

 dict2[all_letters[i]] =
all_letters[(i-key)%(len(all_letters))]

 

# loop to recover plain text

decrypt_txt = []

 

for char in cipher_txt:

 if char in all_letters:

 temp = dict2[char]

 decrypt_txt.append(temp)

 else:

 temp = char

 decrypt_txt.append(temp)

 

decrypt_txt = "".join(decrypt_txt)

print("Recovered plain text :", decrypt_txt)   
  
---  
  
__

__

**Output:**

    
    
    Cipher Text is:  M eq wxyhCmrk Hexe IrgvCtxmsr
    Recovered plain text : I am studying Data Encryption
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

