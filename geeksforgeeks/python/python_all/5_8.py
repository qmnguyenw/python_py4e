Python Program to check for almost similar Strings



Given two strings, the task here is to write a python program that can test if
they are almost similar. Similarity of strings is being checked on the
criteria of frequency difference of each character which should be greater
than a threshold here represented by K.

>  **Input :** test_str1 = ‘aabcdaa’, test_str2 = “abbaccd”, K = 2
>
>  **Output :** True
>
>  **Explanation :** ‘a’ occurs 4 times in str1, and 2 times in str2, 4 – 2 =
> 2, in range, similarly, all chars in range, hence true.
>
>  **Input :** test_str1 = ‘aabcdaaa’, test_str2 = “abbaccda”, K = 3
>
>  
>
>
>  
>
>
>  **Output :** True
>
>  **Explanation :** ‘a’ occurs 5 times in str1, and 3 times in str2, 5 – 3 =
> 2, in range, similarly, all chars in range, hence true.

 **Method 1 :** _Using_ _ascii_lowecase_ _,_ _dictionary comprehension_ _,_
_loop_ _and_ _abs()_

In this, we compute all the frequencies of all the characters in both strings
using dictionary comprehension and loop. Next, each character is iterated from
alphabetic lowercase ascii characters and tested for frequency difference in
both strings using abs(), if any difference computes to greater than K, result
is flagged off.

 **Example**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from string import ascii_lowercase

 

# function to compute frequencies

 

 

def get_freq(test_str):

 

 # starting at 0 count

 freqs = {char: 0 for char in ascii_lowercase}

 

 # counting frequencies

 for char in test_str:

 freqs[char] += 1

 return freqs

 

 

# initializing strings

test_str1 = 'aabcdaa'

test_str2 = "abbaccd"

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing K

K = 2

 

# getting frequencies

freqs_1 = get_freq(test_str1)

freqs_2 = get_freq(test_str2)

 

# checking for frequencies

res = True

for char in ascii_lowercase:

 if abs(freqs_1[char] - freqs_2[char]) > K:

 res = False

 break

 

# printing result

print("Are strings similar ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string 1 is : aabcdaa
>
> The original string 2 is : abbaccd
>
>  
>
>
>  
>
>
> Are strings similar ? : True

 **Method 2 :** _Using_ _Counter()_ _and_ _max()_

In this, we perform task of getting individual characters’ frequency using
Counter() and get the maximum difference using max(), if greater than K, then
result is flagged off.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

# initializing strings

test_str1 = 'aabcdaa'

test_str2 = "abbaccd"

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing K

K = 2

 

# extracting frequencies

cnt1 = Counter(test_str1.lower())

cnt2 = Counter(test_str2.lower())

 

# getting maximum difference

res = True

if max((cnt1 - cnt2).values()) > K or max((cnt2 -
cnt1).values()) > K:

 res = False

 

# printing result

print("Are strings similar ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string 1 is : aabcdaa
>
> The original string 2 is : abbaccd
>
> Are strings similar ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

