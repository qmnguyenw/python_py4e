Python program to check if a string is palindrome or not



Given a string, write a python function to check if it is palindrome or not. A
string is said to be palindrome if the reverse of the string is the same as
string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

 **Examples:**

    
    
    **Input :** malayalam
    **Output :** Yes
    
    **Input :** geeks
    **Output :** No

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method #1**

  1. Find reverse of string
  2. Check if reverse and original are same or not.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# function which return reverse of a string

def isPalindrome(s):

 return s == s[::-1]

# Driver code

s = "malayalam"

ans = isPalindrome(s)

if ans:

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output :**

    
    
    Yes

 **Iterative Method:** This method is contributed by _**Shariq Raza**_. Run a
loop from starting to length/2 and check the first character to the last
character of the string and second to second last one and so on …. If any
character mismatches, the string wouldn’t be a palindrome.

  

  

Below is the implementation of above approach:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# function to check string is

# palindrome or not

def isPalindrome(str):

 # Run loop from 0 to len/2

 for i in range(0, int(len(str)/2)):

 if str[i] != str[len(str)-i-1]:

 return False

 return True

# main function

s = "malayalam"

ans = isPalindrome(s)

if (ans):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

 **Method using the** **inbuilt function to reverse a string:** This method is
contributed by _**Shariq Raza**_. In this method, predefined function **‘
‘.join(reversed(string))** is used to reverse string.

Below is the implementation of the above approach:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# function to check string is

# palindrome or not

def isPalindrome(s):

 

 # Using predefined function to

 # reverse to string print(s)

 rev = ''.join(reversed(s))

 # Checking if both string are

 # equal or not

 if (s == rev):

 return True

 return False

# main function

s = "malayalam"

ans = isPalindrome(s)

if (ans):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

 **Method using one extra variable:** In this method user take a character of
string one by one and store in an empty variable. After storing all the
character user will compare both the string and check whether it is palindrome
or not.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check

# if a string is palindrome

# or not

x = "malayalam"

w = ""

for i in x:

 w = i + w

if (x == w):

 print("Yes")

else:

 print("No")

   
  
---  
  
__

__

**Output:**

    
    
    Yes

 **Method using flag:** In this method user compare each character from
starting and ending in a for loop and if the character does not match then it
will change the status of the flag. Then it will check the status of flag and
accordingly and print whether it is a palindrome or not.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check

# if a string is palindrome

# or not

st = 'malayalam'

j = -1

flag = 0

for i in st:

 if i != st[j]:

 j = j - 1

 flag = 1

 break

 j = j - 1

if flag == 1:

 print("NO")

else:

 print("Yes")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

 **Method using recursion** :

This method compares the first and the last element of the string and gives
the rest of the substring to a recursive call to itself.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Recursive function to check if a

# string is palindrome

def isPalindrome(s):

 

 #to change it the string is similar case

 s = s.lower()

 # length of s

 l = len(s)

 

 # if length is less than 2

 if l < 2:

 return True

 # If s[0] and s[l-1] are equal

 elif s[0] == s[l - 1]:

 

 # Call is pallindrome form substring(1,l-1)

 return isPalindrome(s[1: l - 1])

 else:

 return False

# Driver Code

s = "MalaYaLam"

ans = isPalindrome(s)

if ans:

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output**

    
    
    Yes

This article is contributed by **Sahil Rajput**. If you like GeeksforGeeks and
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

