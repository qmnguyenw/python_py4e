Python – Reverse String except punctuations



Given a string with punctuations, perform string reverse, leaving punctuations
at their places.

>  **Input** : test_str = ‘geeks@#for&%%gee)ks’  
>  **Output** : skeeg@#rof&%%ske)eg  
>  **Explanation** : Whole string is reveresed, except the punctuations.
>
>  **Input** : test_str = ‘geeks@#for&%%gee)ks’ [ only substring reversal ]  
>  **Output** : skeeg@#rof&%%eeg)sk  
>  **Explanation** : Only substrings are reversed.

 **Method #1 : Using loop + stack + punctuation + split()**

In this, we use stack to perform string reversal, checking for punctuation, if
current character is one, we append that. The split method is used to handle
cases of spaces, which needs to be ignored while reverse.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse String except punctuations

# Using loop + stack + punctuation + split()

from string import punctuation

 

# initializing string

test_str = 'geeks# for&%% gee)ks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting punctuations

punc_set = set(punctuation)

res = []

for sub in test_str.split(' '):

 

 # getting all aphabets

 alphas = [chr for chr in sub if chr not in
punc_set]

 for chr in sub:

 

 # checking for punctuations

 if chr not in punc_set:

 res.append(alphas.pop())

 continue

 else:

 res.append(chr)

 

 # handling spaces

 res.append(' ')

res = "".join(res)

 

# printing result 

print("The Reversed String ignoring punctuation : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks#for&%%gee)ks
    The Reversed String ignoring punctuation : skeeg#rof&%%ske)eg 
    
    

**Method #2 : Using groupby() + isalnum() [ for substing specific reversal ]**

In this, we form grouping of each of substring between punctuations, and
reverse them among them, not whole. The isalnum() is used to check for all
alphabets

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse String except punctuations

# Using groupby() + isalnum() [ for substing specific reversal ]

from itertools import groupby

 

# initializing string

test_str = 'geeks# for&%% gee)ks'

 

# printing original string

print("The original string is : " + str(test_str))

 

res = ''

 

# grouping all sections

for ele, sub in groupby(test_str, str.isalnum):

 sub = list(sub)

 

 # reversal on alphanumeric occurrence

 if ele:

 sub = sub[::-1]

 

 # joining all subparts

 res += ''.join(sub)

 

 

# printing result 

print("The Reversed String ignoring punctuation [substring] : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks#for&%%gee)ks
    The Reversed String ignoring punctuation [substring] : skeeg#rof&%%eeg)sk
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

