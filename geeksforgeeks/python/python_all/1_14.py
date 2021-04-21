Python program to sort Palindrome Words in a Sentence



Given a string **S** representing a sentence, the task is to reorder all the
palindromic words present in the sentence in sorted order.

 **Examples:**

>  **Input:** S = “Please refer to the madam to know the level”  
>  **Output:** Please level to the madam to know the refer  
>  **Explanation:** Here “refer”, “madam”, “level” are the palindromic words.
> Sorting them generates the sequence {“level”, “madam”, “refer”}.
>
>  **Input:** S = “refer to dad”  
>  **Output:** dad to refer

 **Approach:** Follow the steps below to solve the problem:

  

  

  * Iterate over the characters of the string.
  * Split the words in the sentence by spaces using **split()** and store it as a list, say **lis.**
  * Store all the palindromic words present in the sentence **S** in a list, say **newlis[].**
  * Sort the list **newlis[]** using sort() function.
  * Initialize a pointer, say **j = 0**.
  * Traverse the list **lis** and replace all the palindromic words with **newlis[j]** and increment **j** by **1**.
  * Print the updated sentence

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of above program

 

# Function to check if a

# string is a palindrome or not

def palindrome(string):

 if(string == string[::-1]):

 return True

 else:

 return False

 

# Function to print the updated sentence

def printSortedPalindromes(sentence):

 

 # Stores palindromic words

 newlist = []

 

 # Stores the words split by spaces

 lis = list(sentence.split())

 

 # Traversing the list

 for i in lis:

 

 # If current word is palindrome

 if(palindrome(i)):

 

 # Update newlist

 newlist.append(i)

 

 # Sort the words in newlist

 newlist.sort()

 

 # Pointer to iterate newlis

 j = 0

 

 # Traverse the list

 for i in range(len(lis)):

 

 # If current word is palindrome

 if(palindrome(lis[i])):

 

 # Replacing word with

 # current word in newlist

 lis[i] = newlist[j]

 

 # Increment j by 1

 j = j + 1

 

 # Print the updated sentence

 for i in lis:

 print(i, end =" ")

 

 

# Driver Code

 

sentence = "please refer to the madam to know the level"

 

printSortedPalindromes(sentence)  
  
---  
  
 __

 __

 **Output:**

    
    
    please level to the madam to know the refer
    

_**Time Complexity :** O(N * logN)_  
 _ **Auxiliary Space :** O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

