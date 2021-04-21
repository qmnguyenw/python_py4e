Feistel Cipher



Feistel Cipher model is a structure or a design used to develop many block
ciphers such as DES. Feistel cipher may have invertible, non-invertible and
self invertible components in its design. Same encryption as well as
decryption algorithm is used. A separate key is used for each round. However
same round keys are used for encryption as well as decryption.

## Feistel cipher algorithm

  * Create a list of all the Plain Text characters.
  * Convert the Plain Text to Ascii and then 8-bit binary format.
  * Divide the binary Plain Text string into two halves: left half (L1)and right half (R1)
  * Generate a random binary keys (K1 and K2) of length equal to the half the length of the Plain Text for the two rounds.
  * First Round of Encryption  
 **a.** Generate function f1 using R1 and K1 as follows:

    
        f1= xor(R1, K1)

 **b.** Now the new left half(L2) and right half(R2) after round 1 are as
follows:

    
        R2= xor(f1, L1)
    L2=R1

  * Second Round of Encryption  
 **a.** Generate function f2 using R2 and K2 as follows:

    
        f2= xor(R2, K2)

 **b.** Now the new left half(L2) and right half(R2) after round 1 are as
follows:

  

  

    
        R3= xor(f2, L2)
    L3=R2

  * Concatenation of R3 to L3 is the Cipher Text
  * Same algorithm is used for decryption to retrieve the Plain Text from the Cipher Text.

 **Examples:**

    
    
    Plain Text is: Hello
    Cipher Text:  E1!w(
    Retrieved Plain Text is:  b'Hello'
    
    Plain Text is: Geeks
    Cipher Text: O;Q
    Retrieved Plain Text is:  b'Geeks'
    

__

__  
__

__

__  
__  
__

# Python program to demonstrate

# Feistel Cipher Algorithm

 

import binascii

 

# Random bits key generation

def rand_key(p):

 

 import random

 key1 = ""

 p = int(p)

 

 for i in range(p):

 

 temp = random.randint(0,1)

 temp = str(temp)

 key1 = key1 + temp

 

 return(key1)

 

# Function to implement bit exor

def exor(a,b):

 

 temp = "" 

 

 for i in range(n): 

 

 if (a[i] == b[i]):

 temp += "0"

 

 else: 

 temp += "1"

 

 return temp 

 

# Defining BinarytoDecimal() function 

def BinaryToDecimal(binary): 

 

 # Using int function to convert to 

 # string 

 string = int(binary, 2) 

 

 return string

 

# Feistel Cipher

PT = "Hello"

print("Plain Text is:", PT)

 

# Converting the plain text to

# ASCII

PT_Ascii = [ord(x) for x in PT]

 

# Converting the ASCII to 

# 8-bit binary format

PT_Bin = [format(y,'08b') for y in PT_Ascii]

PT_Bin = "".join(PT_Bin)

 

n = int(len(PT_Bin)//2)

L1 = PT_Bin[0:n]

R1 = PT_Bin[n::]

m = len(R1)

 

# Generate Key K1 for the 

# first round

K1= rand_key(m)

 

# Generate Key K2 for the

# second round

K2= rand_key(m)

 

# first round of Feistel

f1 = exor(R1,K1)

R2 = exor(f1,L1)

L2 = R1

 

# Second round of Feistel

f2 = exor(R2,K2)

R3 = exor(f2,L2)

L3 = R2

 

# Cipher text

bin_data = L3 + R3

str_data =' '

 

for i in range(0, len(bin_data), 7): 

 

 # slicing the bin_data from index range [0, 6] 

 # and storing it in temp_data 

 temp_data = bin_data[i:i + 7] 

 

 # passing temp_data in BinarytoDecimal() function 

 # to get decimal value of corresponding temp_data 

 decimal_data = BinaryToDecimal(temp_data) 

 

 # Deccoding the decimal value returned by 

 # BinarytoDecimal() function, using chr() 

 # function which return the string corresponding 

 # character for given ASCII value, and store it 

 # in str_data 

 str_data = str_data + chr(decimal_data) 

 

print("Cipher Text:", str_data)

 

# Decryption

L4 = L3

R4 = R3

 

f3 = exor(L4,K2)

L5 = exor(R4,f3)

R5 = L4

 

f4 = exor(L5,K1)

L6 = exor(R5,f4)

R6 = L5

PT1 = L6+R6

 

 

PT1 = int(PT1, 2)

RPT = binascii.unhexlify( '%x'% PT1)

print("Retrieved Plain Text is: ", RPT)  
  
---  
  
 __

 __

 **Output:**

    
    
    Plain Text is: Hello
    Cipher Text:  E1!w(
    Retrieved Plain Text is:  b'Hello'

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

