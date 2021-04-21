Python – Replace vowels in a string with a specific character K



Given a string, replace all the vowels with character K.

>  _ **Input** : test_str = “Geeks for Geeks”; K=’#’_  
>  _ **Output** : “_G##ks f#r G##ks _”_  
>  _ **Explanation** : All the vowels in test_str are replaced by a give
> particular character._
>
>  _ **Input** : test_list = “GFG”; K=”$”_  
>  _ **Output** : GFG_  
>  _ **Explanation** : As test_str contained no vowel, so the same string is
> returned._

 **Method #1 : Using loop + replace()**

Initially create a string of vowels and then iterate through the given
_test_str_ , __ on detecting a vowel in _test_str_ replace the vowel with _K_
using _replace()_ method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Replace each vowel in

# the string with a specified character

def replaceVowelsWithK(test_str, K):

 

 # string of vowels

 vowels = 'AEIOUaeiou'

 

 # iterating to check vowels in string

 for ele in vowels:

 

 # replacing vowel with the specified character

 test_str = test_str.replace(ele, K)

 

 return test_str

 

 

 

# Driver Code

# input string

input_str = "Geeks for Geeks"

 

# specified character

K = "#"

 

# printing input

print("Given Sting:", input_str)

print("Given Specified Character:", K)

 

# printing output

print("Afer replacing vowels with the specified character:",

 replaceVowelsWithK(input_str, K))  
  
---  
  
 __

 __

 **Output:**

> Given Sting: Geeks for Geeks  
> Given Specified Character: #  
> Afer replacing vowels with the specified character: G##ks f#r G##ks
>
>  
>
>
>  
>

 **Method #2 : Using nested loop**

Here, we first convert the given string into a list and then create a list of
vowels and an empty list i.e _new_string_. After that elements of both
_string_list and vowel_list_ are compared and if the element is a vowel then
_K_ is appended to _new_string_ else the element of the given string is
appended. __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Replace each vowel

# in the string with a specified character

def replaceVowelsWithK(test_str, K):

 

 # creating list of vowels

 vowels_list = ['A', 'E', 'I', 'O', 'U', 'a',
'e', 'i', 'o', 'u']

 

 # creating empty list

 new_string = []

 

 # converting the given string to list

 string_list = list(test_str)

 

 # running 1st iteration for 

 # comparing all the

 # characters of string with 

 # the vowel characters

 for char in string_list:

 

 # running 2nd iteration for 

 # comparing all the characters 

 # of vowels with the string character

 for char2 in vowels_list:

 

 # comparing string character 

 # and vowel character

 if char == char2:

 

 # if condition is true then adding 

 # the specific character entered 

 # by the user in the new list

 new_string.append(K)

 break

 

 # else adding the character

 else:

 new_string.append(char)

 

 # return the converted list into string

 return(''.join(new_string))

 

 

 

# Driver Code

# input string

input_str = "Geeks for Geeks"

 

# specified character

K = "#"

 

# printing input

print("Given Sting:", input_str)

print("Given Specified Character:", K)

 

# printing output

print("Afer replacing vowels with the specified character:",

 replaceVowelsWithK(input_str, K))  
  
---  
  
 __

 __

 **Output:**

> Given Sting: Geeks for Geeks  
> Given Specified Character: #  
> Afer replacing vowels with the specified character: G##ks f#r G##ks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

