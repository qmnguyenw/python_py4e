Python program to check whether the string is Symmetrical or Palindrome



Given a string. the task is to check if the string is symmetrical and
palindrome or not. A string is said to be symmetrical if both the halves of
the string are the same and a string is said to be a palindrome string if one
half of the string is the reverse of the other half or if a string appears
same when read forward or backward.

 **Example:**

    
    
    **Input:** khokho
    **Output:** 
    The entered string is symmetrical
    The entered string is not palindrome
    
    **Input:** amaama
    **Output:**
    The entered string is symmetrical
    The entered string is palindrome
    

**Approach:** The approach is very naive. In the case of palindrome, a loop is
run to the mid of the string and the first and last character are matched. If
the characters are not similar then the loop breaks and the string is not
palindrome otherwise the string is a palindrome. In the case of symmetry, if
the string length is even then the string is broken into two halves and the
loop is run, checking the characters of the strings of both the half. If the
characters are not similar then the loops break and the string is not
symmetrical otherwise the string is symmetrical. If the string length is odd
then the string is broken into two halves in such a way that the middle
element is left unchecked, and the above same step is repeated.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# symmetry and palindrome of the

# string

 

 

# Function to check whether the

# string is plaindrome or not

def palindrome(a):

 

 # finding the mid, start 

 # and last index of the string

 mid = (len(a)-1)//2

 start = 0

 last = len(a)-1

 flag = 0

 

 # A loop till the mid of the

 # string

 while(start<mid):

 

 # comparing letters from right

 # from the letters from left

 if (a[start]== a[last]):

 

 start += 1

 last -= 1

 

 else:

 flag = 1

 break;

 

 # Checking the flag variable to 

 # check if the string is palindrome

 # or not

 if flag == 0:

 print("The entered string is palindrome")

 else:

 print("The entered string is not palindrome")

 

# Function to check whether the

# string is symmetrical or not 

def symmetry(a):

 

 n = len(a)

 flag = 0

 

 # Check if the string's length

 # is odd or even

 if n%2:

 mid = n//2 +1

 else:

 mid = n//2

 

 start1 = 0

 start2 = mid

 

 while(start1 < mid and start2 < n):

 

 if (a[start1]== a[start2]):

 start1 = start1 + 1

 start2 = start2 + 1

 else:

 flag = 1

 break

 

 # Checking the flag variable to 

 # check if the string is symmetrical

 # or not

 if flag == 0:

 print("The entered string is symmetrical")

 else:

 print("The entered string is not symmetrical")

 

# Driver code

string = 'amaama'

palindrome(string)

symmetry(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    The entered string is palindrome
    The entered string is symmetrical

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

