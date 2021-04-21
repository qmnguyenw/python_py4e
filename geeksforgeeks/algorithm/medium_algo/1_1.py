Implementation of RC4 algorithm



RC4 is a symmetric stream cipher and variable key length algorithm. This
symmetric key algorithm is used identically for encryption and decryption such
that the data stream is simply XORed with the generated key sequence. The
algorithm is serial as it requires successive exchanges of state entries based
on the key sequence. The algorithm works in two phases:

 ** _Key Scheduling Algorithm(KSA)_ :**

  * It is used to generate a State array by applying a permutation using a variable-length key consisting of **0** to **256 bytes**.
  * The state vector is identified as **S[0]** , **S[1]…. S[255]** is initialized with **{0, 1, 2, …, 255}**. The key **K[0]** , **K[1], …., K[255]** can be of any length from **0** to **256 bytes** and is used to initialize permutation S. Each K[I] and S[I] is a byte.
  * K is a temporary array if the length of the key is 256 bytes copy it to K else after copying the remaining positions of K are filled with repeated Key Values until full.

    
    
    S[] is permutation of 0, 1, ..., 255
    key[] contains N bytes of key
    
    for i = 0 to 255
        S[i] = i
        
        // Selects a keystream byte from
        // the table
        K[i] = key[i (mod N)]
        i++
    j = 0
    
    for i = 0 to 255
        j = (j + S[i] + K[i]) mod 256
        
        // Swaps elements in the current
        // lookup table
        swap(S[i], S[j])
    i = j = 0

 ** _Pseudo-Random Generation Algorithm(PRGA)_ :** It used to generate
keystream byte from State vector array after one more round of permutation.

    
    
    Keystream Generation(i := 0, j := 0 )
    
    while Generating Output:
        i = (i + 1) mod 256
        j = (j + S[i]) mod 256
        swap(S[i], S[j])
        t = (S[i] + S[j]) mod 256
        keystreamByte = S[t]
    
    At each iteration, swap elements in table
    and select keystream byte

Then, perform XOR between the keystream generated and the plain text for
encryption.

Follow the same procedure as above for decryption, taking cipher text in place
of plain text everywhere.

  

  

 **Examples:**

>  **Input:** plain text = 001010010010, key = 101001000001, n= 3  
>  **Output:**  
>  cipher text = 110011100011  
> decrypted text = 001010010010
>
>  **Input:** plain text = 1111000000001111, key = 0101010111001010, n= 4  
>  **Output:**  
>  cipher text = 0011011110100010  
> decrypted text = 1111000000001111

Below is the implementation of the above approach with a detailed output of
all the important steps involved:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for the above approach

# of RC4 algorithm

 

# Function for encryption

def encryption():

 

 global key, plain_text, n

 

 # Given text and key

 plain_text = "001010010010"

 key = "101001000001"

 

 # n is the no: of bits to

 # be considered at a time

 n = 3

 

 print("Plain text : ", plain_text)

 print("Key : ", key)

 print("n : ", n)

 

 print(" ")

 

 # The initial state vector array

 S = [i for i in range(0, 2**n)]

 print("S : ", S)

 

 key_list = [key[i:i + n] for i in range(0,
len(key), n)]

 

 # Convert to key_stream to decimal

 for i in range(len(key_list)):

 key_list[i] = int(key_list[i], 2)

 

 # Convert to plain_text to decimal

 global pt

 

 pt = [plain_text[i:i + n] for i in range(0,
len(plain_text), n)]

 

 for i in range(len(pt)):

 pt[i] = int(pt[i], 2)

 

 print("Plain text ( in array form ): ", pt)

 

 # Making key_stream eqaul

 # to length of state vector

 diff = int(len(S)-len(key_list))

 

 if diff != 0:

 for i in range(0, diff):

 key_list.append(key_list[i])

 

 print("Key list : ", key_list)

 print(" ")

 

 # Perform the KSA algorithm

 def KSA():

 j = 0

 N = len(S)

 

 # Iterate over the range [0, N]

 for i in range(0, N):

 

 # Find the key

 j = (j + S[i]+key_list[i]) % N

 

 # Update S[i] and S[j]

 S[i], S[j] = S[j], S[i]

 print(i, " ", end ="")

 

 # Print S

 print(S)

 

 initial_permutation_array = S

 

 print(" ")

 print("The initial permutation array is : ",

 initial_permutation_array)

 

 print("KSA iterations : ")

 print(" ")

 KSA()

 print(" ")

 

 # Perform PGRA algorithm

 def PGRA():

 

 N = len(S)

 i = j = 0

 global key_stream

 key_stream = []

 

 # Iterate over [0, length of pt]

 for k in range(0, len(pt)):

 i = (i + 1) % N

 j = (j + S[i]) % N

 

 # Update S[i] and S[j]

 S[i], S[j] = S[j], S[i]

 print(k, " ", end ="")

 print(S)

 t = (S[i]+S[j]) % N

 key_stream.append(S[t])

 

 # Print the key stream

 print("Key stream : ", key_stream)

 print(" ")

 

 print("PGRA iterations : ")

 print(" ")

 PGRA()

 

 # Performing XOR between generated

 # key stream and plain text

 def XOR():

 global cipher_text

 cipher_text = []

 for i in range(len(pt)):

 c = key_stream[i] ^ pt[i]

 cipher_text.append(c)

 

 XOR()

 

 # Convert the encrypted text to

 # bits form

 encrypted_to_bits = ""

 for i in cipher_text:

 encrypted_to_bits +=
'0'*(n-len(bin(i)[2:]))+bin(i)[2:]

 

 print(" ")

 print("Cipher text : ", encrypted_to_bits)

 

 

encryption()

 

print("---------------------------------------------------------")

 

# Function for decryption of data

def decryption():

 

 # The initial state vector array

 S = [i for i in range(0, 2**n)]

 

 key_list = [key[i:i + n] for i in range(0,
len(key), n)]

 

 # Convert to key_stream to decimal

 for i in range(len(key_list)):

 key_list[i] = int(key_list[i], 2)

 

 # Convert to plain_text to decimal

 global pt

 

 pt = [plain_text[i:i + n] for i in range(0,
len(plain_text), n)]

 

 for i in range(len(pt)):

 pt[i] = int(pt[i], 2)

 

 # making key_stream eqaul

 # to length of state vector

 diff = int(len(S)-len(key_list))

 

 if diff != 0:

 for i in range(0, diff):

 key_list.append(key_list[i])

 

 print(" ")

 

 # KSA algorithm

 def KSA():

 j = 0

 N = len(S)

 

 # Iterate over the range [0, N]

 for i in range(0, N):

 j = (j + S[i]+key_list[i]) % N

 

 # Update S[i] and S[j]

 S[i], S[j] = S[j], S[i]

 print(i, " ", end ="")

 print(S)

 

 initial_permutation_array = S

 print(" ")

 print("The initial permutation array is : ",

 initial_permutation_array)

 

 print("KSA iterations : ")

 print(" ")

 KSA()

 print(" ")

 

 # Perform PRGA algorithm

 def do_PGRA():

 

 N = len(S)

 i = j = 0

 global key_stream

 key_stream = []

 

 # Iterate over the range

 for k in range(0, len(pt)):

 i = (i + 1) % N

 j = (j + S[i]) % N

 

 # Update S[i] and S[j]

 S[i], S[j] = S[j], S[i]

 print(k, " ", end ="")

 print(S)

 t = (S[i]+S[j]) % N

 key_stream.append(S[t])

 

 print("Key stream : ", key_stream)

 print(" ")

 

 print("PGRA iterations : ")

 print(" ")

 do_PGRA()

 

 # Perform XOR between generated

 # key stream and cipher text

 def do_XOR():

 global original_text

 original_text = []

 for i in range(len(cipher_text)):

 p = key_stream[i] ^ cipher_text[i]

 original_text.append(p)

 

 do_XOR()

 

 # convert the decrypted text to

 # the bits form

 decrypted_to_bits = ""

 for i in original_text:

 decrypted_to_bits +=
'0'*(n-len(bin(i)[2:]))+bin(i)[2:]

 

 print(" ")

 print("Decrypted text : ",

 decrypted_to_bits)

 

# Driver Code

decryption()  
  
---  
  
 __

 __

 **Output:**

    
    
    Plain text :  001010010010
    Key :  101001000001
    n :  3
     
    S :  [0, 1, 2, 3, 4, 5, 6, 7]
    Plain text ( in array form ):  [1, 2, 2, 2]
    Key list :  [5, 1, 0, 1, 5, 1, 0, 1]
     
    KSA iterations : 
     
    0  [5, 1, 2, 3, 4, 0, 6, 7]
    1  [5, 7, 2, 3, 4, 0, 6, 1]
    2  [5, 2, 7, 3, 4, 0, 6, 1]
    3  [5, 2, 7, 0, 4, 3, 6, 1]
    4  [5, 2, 7, 0, 6, 3, 4, 1]
    5  [5, 2, 3, 0, 6, 7, 4, 1]
    6  [5, 2, 3, 0, 6, 7, 4, 1]
    7  [1, 2, 3, 0, 6, 7, 4, 5]
     
    The initial permutation array is :  [1, 2, 3, 0, 6, 7, 4, 5]
     
    PGRA iterations : 
     
    0  [1, 3, 2, 0, 6, 7, 4, 5]
    1  [1, 3, 6, 0, 2, 7, 4, 5]
    2  [1, 3, 6, 2, 0, 7, 4, 5]
    3  [1, 3, 6, 2, 0, 7, 4, 5]
    Key stream :  [7, 1, 6, 1]
     
     
    Cipher text :  110011100011
    ---------------------------------------------------------
     
    KSA iterations : 
     
    0  [5, 1, 2, 3, 4, 0, 6, 7]
    1  [5, 7, 2, 3, 4, 0, 6, 1]
    2  [5, 2, 7, 3, 4, 0, 6, 1]
    3  [5, 2, 7, 0, 4, 3, 6, 1]
    4  [5, 2, 7, 0, 6, 3, 4, 1]
    5  [5, 2, 3, 0, 6, 7, 4, 1]
    6  [5, 2, 3, 0, 6, 7, 4, 1]
    7  [1, 2, 3, 0, 6, 7, 4, 5]
     
    The initial permutation array is :  [1, 2, 3, 0, 6, 7, 4, 5]
     
    Key stream :  [7, 1, 6, 1]
     
    PGRA iterations : 
     
    0  [1, 3, 2, 0, 6, 7, 4, 5]
    1  [1, 3, 6, 0, 2, 7, 4, 5]
    2  [1, 3, 6, 2, 0, 7, 4, 5]
    3  [1, 3, 6, 2, 0, 7, 4, 5]
     
    Decrypted text :  001010010010
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

