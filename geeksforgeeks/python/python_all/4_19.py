Python program to find the smallest word in a sentence



Given a string **S** of lowercase English alphabets, the task is to print the
smallest word in the given string.

 **Examples:**

>  **Input:** S = “sky is blue”  
>  **Output:** “is”  
>  **Explanation:**  
> Length of “sky” is 3.  
> Length of is “is” 2.  
> Length of “blue” is 4.  
> Therefore, the smallest word is “is”.
>
>  **Input:** S = “geeks for geeks”  
>  **Output:** “for”

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Searching-based Approach:** Refer to _this_ article to solve this problem
by performing the following steps:

  

  

  * Iterate over the characters of the string.
  * Check if the current character encountered is a space or end of the string is reached.
  * If the current character is found to be so, update the maximum length of a word obtained.
  * Finally, print the longest word obtained using _substr()_method.

 _ **Time Complexity:** O(N), where N is the length of the string._  
 _ **Auxiliary Space:** O(1)_

 **Approach using** ** _sorted()_** **method:** The idea is to _split_ the
words of the string into a list and sort the list in increasing order of
length of words using the sorted() method. Finally, print the first string
present in the list.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for the above approach

 

# Function to print the

# smallest word in the string s

 

 

def smallestWord(s):

 

 # Using sorted() method

 s = sorted(s, key = len)

 

 # Print first word

 print(s[0])

 

 

# Driver Code

if __name__ == "__main__":

 

 # Given string

 s = "sky is blue"

 

 # Convert string to list

 l = list(s.split(" "))

 

 smallestWord(l)  
  
---  
  
 __

 __

 **Output:**

    
    
    is
    

_**Time Complexity:** O(N * LogN)_  
 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

