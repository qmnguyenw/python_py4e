Python program to check whether number formed by combining all elements of the
array is palindrome



Given an array arr[], the task is to combine all the elements in the array
sequentially and check if it is a palindrome.

 **Examples** :

>  **Input:** arr[] ={1 , 69 , 54 , 45 , 96 , 1}
>
>  **Output:** palindrome
>
>  **Explaination:** The number formed by combining all the elements is
> **“1695445961”** which is a palindrome
>
>  
>
>
>  
>
>
>  **Input** : arr[] ={2 , 73 , 95 , 59 , 96 , 2}
>
>  **Output:** not palindrome
>
>  **Explaination** : The number formed by combining all the elements is
> **“2739559962”** which is not a palindrome

 **Method 1:** Using map() and join()

  * Convert each element of the list to a string using ******map()** function.
  * Join the list using ******join()** function.
  * Check if it is a palindrome.
  * If yes then print palindrome.
  * If no print, not a palindrome.

 **Below is the implementation of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to check palindrome

def checkPalindrome(string):

 

 # reverse the string

 rev = string[::-1]

 

 # checking if string is equal to reverse

 if(string == rev):

 return True

 else:

 return False

 

# function to convert list to single number string

def joinArray(lis):

 

 # convert the elements of list to string

 lis = list(map(str, lis))

 

 # converting list to string

 number = ''.join(lis)

 

 # checking if it is palindrome

 if(checkPalindrome(number)):

 return True

 else:

 return False

 

# Driver code

lis = [1, 76, 39, 93, 67, 1]

if(joinArray(lis)):

 print("Palindrome")

else:

 print("not Palindrome")  
  
---  
  
 __

 __

 **Output:**

    
    
    Palindrome

 **Time Complexity:** O(n)

**Method 2:** Using type casting and string concatenation

  * Take an empty string say **str.**
  * Traverse through the list and convert each element to string using type casting
  * Add this to **str** using string concatenation
  * Check if **str** is **** a palindrome

 **Below is the implementation of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to check palindrome

def checkPalindrome(string):

 

 # reverse the string

 rev = string[::-1]

 

 # checking if string is equal to reverse

 if(string == rev):

 return True

 else:

 return False

 

# function to convert list to single number string

def joinArray(lis):

 

 # defining empty string as number

 number = ""

 

 # convert the elements of list to string using type conversion

 for i in lis:

 

 # converting to string

 i = str(i)

 

 # concat this to string

 number = number + i

 

 # checking if it is palindrome

 if(checkPalindrome(number)):

 return True

 else:

 return False

 

# Driver code

lis = [1, 76, 39, 93, 67, 1]

 

if(joinArray(lis)):

 print("Palindrome")

else:

 print("not Palindrome")  
  
---  
  
 __

 __

 **Output:**

    
    
    Palindrome

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

