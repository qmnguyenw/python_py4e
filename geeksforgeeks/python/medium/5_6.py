SHA3 in Python



A **cryptographic hash function** is an exceptional class of hash function
that has certain properties that make it appropriate for use in cryptography.
It is a numerical algorithm that maps information of self-assertive size to a
piece line of a fixed size (a hash function) which is intended to likewise be
a one-way output function, that is, a function which is infeasible to revert.

## hashlib module

To calculate the cryptographic hash value in Python, “hashlib” Module is used.
The _hashlib_ gives the following cryptographic hash functions to discover the
hash output of a text as follows:

  * sha3_224 – 28 bit Digest-Size
  * sha3_256 – 32 bit Digest-Size
  * sha3_384 – 48 bit Digest-Size
  * sha3_512 – 64 bit Digest-Size

This module actualizes a typical interface to various secure hash and message
digest calculations. Included are the FIPS secure hash calculations SHA1,
SHA224, SHA256, SHA384, and SHA512 just as RSA’s MD5 calculation
(characterized in Internet RFC 1321). Earlier calculations were called message
digests, but today it is secure hash.

Python has a bountiful help for hash code calculations through the library
module _hashlib_. You can utilize the “hashlib.algorithms_available” to get
the rundown of all accessible hash calculations in your variant of Python.

Hashlib provides the following constant attributes:

  

  

  * “hashlib.algorithms_guaranteed” – A set which contains all the hashing algorithms which are guaranteed to be supported by this module on all platforms.
  * “hashlib.algorithms_available” – A set that contains all the names of the hashing algorithms that are currently available in the interpreter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import hashlib 

 

print(hashlib.algorithms_guaranteed)

print(hashlib.algorithms_available)  
  
---  
  
 __

 __

 **Output :**

> {‘blake2b’, ‘shake_256’, ‘sha512’, ‘sha3_224’, ‘sha384’, ‘sha3_512’,
> ‘sha3_256’, ‘sha3_384’, ‘md5’, ‘sha256’, ‘sha224’, ‘sha1’, ‘blake2s’,
> ‘shake_128’}  
>
>
> {‘SHA512’, ‘md5’, ‘blake2s’, ‘sha512’, ‘DSA-SHA’, ‘whirlpool’, ‘sha224’,
> ‘sha3_256’, ‘DSA’, ‘blake2b’, ‘MD5’, ‘SHA256’, ‘ecdsa-with-SHA1’,
> ‘dsaWithSHA’, ‘sha384’, ‘md4’, ‘sha3_384’, ‘MD4’, ‘sha3_512’, ‘sha256’,
> ‘RIPEMD160’, ‘ripemd160’, ‘shake_256’, ‘SHA’, ‘sha3_224’, ‘dsaEncryption’,
> ‘SHA224’, ‘sha’, ‘SHA1’, ‘sha1’, ‘shake_128’, ‘SHA384’}

### Constant attributes

  *  **hash.digest_size:** The size of the subsequent hash in bytes.
  *  **hash.block_size:** The inside square size of the hash calculation in bytes.
  *  **hash.name** : The sanctioned name of this hash, consistently lowercase and always appropriate as a boundary to new() to make another hash of this sort.

### Methods in hashlib

  *  **hash.update(data):** Update the hash object with the bytes-like object.
  *  **hash.digest():** Return the condensation of the information went to the update() method up until now. This is a bytes object of size digest_size and can contain bytes ranging in number from 0 to 255.
  *  **hash.hexdigest():** Like digest() aside from the digest is returned as a string object of twofold length, containing just hexadecimal digits.
  *  **hash.copy():** Return a duplicate (“clone”) of the hash object. This can be utilized to effectively figure the overviews of information sharing a typical beginning sub-string.

### SHAKE variable-length digests

  *  **shake.digest(length):** Returns the condensation of the information passed to the update() function . This is a bytes object of size which may contain bytes in the entire range from 0 to 255.
  *  **shake.hexdigest(length):** Like overview() aside from the condensation is returned as a string object of twofold length, containing just hexadecimal digits.

## SHA – a brief

The Secure Hash Algorithms are a group of cryptographic hash functions
proposed by the National Institute of Standards and Technology (NIST) and
include:

  *  **SHA-0:** A word applied to the first form of the 160-bit hash function produced in 1993 under the name “SHA”. It was pulled back soon after production because of an undisclosed “noteworthy blemish” and supplanted by the marginally overhauled variant SHA-1.
  *  **SHA-1:** A 160-bit hash function which looks like the prior MD5. This was planned by the National Security Agency (NSA) to be essential for the Digital Signature Algorithm. Cryptographic shortcomings were found in SHA-1, and the standard was not, at this point endorsed for most cryptographic uses after 2010.
  *  **SHA-2:** A group of two comparative hash functions, with various bock sizes, known as SHA-256 and SHA-512, they contrast in the word size; SHA-256 utilizations are of 32-byte words where SHA-512’s are of 64-byte words.
  *  **SHA-3:** A hash function, once in the past called _Keccak_ , picked in 2012 after a public rivalry among non-NSA originators. It underpins similar hash lengths as SHA-2, and its inside structure varies altogether from the remainder of the SHA family.

## SHA-3 implementation

Secure Hash Algorithm-3 additionally called Keccak, is a unidirectional method
for creating computerized prints of the given length according to the
standards as 224, 256, 384, or 512 pieces from input information of any size,
created by a gathering of creators drove by Yoan Dimen in 2008 and embraced in
2015 as the new FIPS standard. The calculation works by methods for the
blending capacity in with compression to the chose size “cryptographic
sponge”.

 **Examples:**

>  **Input:** HelloWorld
>
>  **Output[sha3_224]:**
> c4797897c58a0640df9c4e9a8f30570364d9ed8450c78ed155278ac0
>
>  
>
>
>  
>
>
>  **Input:** HelloWorld  
>  **Output[sha3_256]:**
> 92dad9443e4dd6d70a7f11872101ebff87e21798e4fbb26fa4bf590eb440e71b
>
>  **Input:** HelloWorld
>
>  **Output[sha3_384]:**
> dc6104dc2caff3ce2ccecbc927463fc3241c8531901449f1b1f4787394c9b3aa55a9e201d0bb0b1b7d7f8892bc127216
>
>  **Input:** HelloWorld
>
>  **Output[sha3_512]:**
> 938315ec7b0e0bcac648ae6f732f67e00f9c6caa3991627953434a0769b0bbb15474a429177013ed8a7e48990887d1e19533687ed2183fd2b6054c2e8828ca1c  
>

The following programs show the implementation of SHA-3 hash in Python-3.8
using different methods: Implementation of _sha3_224_ using __ the _update_
method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

import hashlib

 

if sys.version_info < (3, 6):

 import sha3

 

# initiating the "s" object to use the

# sha3_224 algorithm from the hashlib module.

s = hashlib.sha3_224()

 

# will output the name of the hashing algorithm currently in use.

print(s.name)

 

# will output the Digest-Size of the hashing algorithm being used.

print(s.digest_size)

 

# providing the input to the hashing algorithm.

s.update(b"GeeksforGeeks")

 

print(s.hexdigest())  
  
---  
  
 __

 __

 **Output**

    
    
    sha3_224
    28
    11c044e8080ed87b3cf0643bc5880a38ae62dd4562390700000b1191
    

Implementation of _sha3_256_ using _encode_ method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import the library module

import sys

import hashlib

 

if sys.version_info < (3, 6):

 import sha3

 

# initialize a string

str = "GeeksforGeeks"

 

# encode the string

encoded_str = str.encode()

 

# create sha3-256 hash objects

obj_sha3_256 = hashlib.sha3_256(encoded_str)

 

# print in hexadecimal

print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())  
  
---  
  
 __

 __

 **Output:**

> SHA3-256 Hash:
> b05a48e99c60983b96b5a69efad8bb44e586702d484d43e592ab639ef64641ff

Implementation of _sha3_384_

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import the library module

import sys

import hashlib

 

if sys.version_info < (3, 6):

 import sha3

 

# initialize a string

str = "GeeksforGeeks"

 

# encode the string

encoded_str = str.encode()

 

# create sha3-384 hash objects

obj_sha3_384 = hashlib.sha3_384(encoded_str)

 

# print in hexadecimal

print("\nSHA3-384 Hash: ", obj_sha3_384.hexdigest())  
  
---  
  
 __

 __

 **Output:**

> SHA3-384 Hash:
> b92ecaaafd00472daa6d619b68010b5f66da7c090e32bd4f5a6b60899e8de3e2c859792ec07a33775cfca8d05c64f222

Implementation of _sha3_512_ using __ the _new_ method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

import hashlib

 

if sys.version_info < (3, 6):

 import sha3

 

str = "GeeksforGeeks"

 

# create a sha3 hash object

hash_sha3_512 = hashlib.new("sha3_512", str.encode())

 

print("\nSHA3-512 Hash: ", hash_sha3_512.hexdigest())  
  
---  
  
 __

 __

 **Output:**

> SHA3-512 Hash:
> 3706a96a8fa96b3fc5ff30cbca36ce666042e2d07762022a78a2ec82439848fc3695e83336ab71f47dddbc24b96454df2a437e343801a4e13faab89e8d0fda61

 **Applications of Hashing-Algorithms:**

  * Message Digest
  * Password Verification
  * Data Structures(Programming Languages)
  * Compiler Operation
  * Rabin-Karp Algorithm
  * Linking File name and path together

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

