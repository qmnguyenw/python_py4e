Full domain Hashing with variable Hash size in Python



A cryptographic hash function is a special class of hash function that has
certain properties which make it suitable for use in cryptography. It is a
mathematical algorithm that maps data of arbitrary size to a bit string of a
fixed size (a hash function) which is designed to also be a one-way function,
that is, a function which is infeasible to invert. In this article, let us
understand one such type of hashing with variable hash size.

Traditional **RSA Signature schemes** are based on the following sequence of
steps:

  1. Obtain the message to be digitally signed – **M**
  2. Use SHA or some other hashing algorithm to generate the message digest – **H = Hash(M)**
  3. Encrypt the message digest using the signer’s private key. The encryption results is the signature of the message – **S = E(PrivateKey, H)**

One potential deficit in the above-illustrated scheme is that the **RSA system
ends up being underutilized**. Let us assume that the RSA modulus is of the
order of _2048_ bits. This means that the input can be any value with up to
_2048_ bits. However, in the signature scheme, the input to the RSA system is
consistently the same size, the size of the hash-digest. Therefore, if, for
instance, **SHA-512** is being utilized in the signature scheme, all inputs to
the RSA function will consistently be 512 bits. This leaves the majority ( **>
99%** in this case) of the RSA input space unutilized. This has the effect of
reducing the overall security level of the RSA system as a result of the input
space underutilization.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200516222659/DC4E865D-788B-49CF-AA2F-A598BA644930.png)

The **Full Domain Hashing** (FDH) scheme in RSA Signature schemes mitigates
this underutilization by hashing the message onto the full domain of the RSA
cryptosystem. The goal of FDH, therefore, is:

  

  

> Hash a message using a function whose image-size/digest-size equals the size
> of the RSA modulus

The two basic approaches to realize a function which can produce an arbitrary
size digest are:

  1. Repeatedly hashing the message (with slight modifications) and concatenating
  2. Using an **eXtendible Output Function (XOF)** hashing methods

 _ **Repeated Hashing with Concatenation**_

Although traditional hashing algorithms such as SHA1, SHA256, SHA512 do not
nearly have the sufficient range to cover the input domains of RSA systems, we
can construct a full domain hashing method through the repeated application of
these hash functions. The standard hash function, say SHA512, is applied to
the message repeatedly, concatenating the results each time. This is done
until the requisite number of bits is achieved.

To introduce the randomized behaviour of hash functions, instead of hashing
the same message repeatedly, some modifications are introduced to the message
at each iteration before performing the hashing. An example of such a
modification would be to concatenate the iteration count to the message,
before hashing. Thus, an FDH function is realized as:  
![   FDH\(m\) =\\ h\(m\\lvert\\lvert0\)\\ ||\\ h\(m||1\)\\ ||\\ h\(m||2\)\\ ||
\\dotso  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-9a7ff7dd0c74e9514aaa8c79595d98c1_l3.png)

If the SHA512 hash was computed and concatenated **N** times, the overall hash
will have a bit size of **N * 512**. Assuming that this value is greater than
the required number, **‘K’** , of bits, we can extract the leading **K** bits
to obtain the desired length hash.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# repeated hashing with 

# concatenation

 

import binascii

from math import ceil

from hashlib import sha256

 

# Function to perform Full Domain 

# Hash of 'message' using 

# SHA512 with a digest of 

# N bits

def fdh(message, n):

 

 

 result = []

 

 # Produce enough SHA512 digests 

 # to make a composite digest 

 # greater than or equal to N bits

 for i in range(ceil(n / 256)):

 

 # Append iteration count 

 # to the message

 currentMsg = str(message) + str(i)

 

 # Add currrent hash to results list

 result.append(sha256((currentMsg).encode()).hexdigest())

 

 # Append all the computed hashes

 result = ''.join(result)

 

 # Obtaining binary representating

 resAsBinary = ''.join(format(ord(x), 'b') for x in
result)

 

 # Trimming the hash to the 

 # required size by taking 

 # only the leading bits

 resAsBinary = resAsBinary[:n]

 

 # Converting back to the 

 # ASCII from binary format

 return binascii.unhexlify('00%x' % int(resAsBinary,
2)).hex()

 

# Driver code

if __name__ == '__main__':

 # Message to be hashed

 message = "GeeksForGeeks"

 

 # Generate a 600 bit

 # hash using SHA256

 print(fdh(message, 600))  
  
---  
  
 __

 __

 **Output:**

  

  

>
> 00cf161c36df4db9e30d79cf9cb3d72e1934cbaeb9eb8638f0d71f1872679e1df9c3932c77c70c98efa64d34e3166c5b698738b36d9b36b87261c5ae3c61873c98e19b362db1c73658f0e4c9

