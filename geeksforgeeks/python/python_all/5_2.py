Python program to find the longest word in a sentence



Given a string **S** consisting of lowercase English alphabets, the task is to
print the longest word present in the given string in python.

 **Examples:**

>  **Input:** S = “be confident and be yourself”  
>  **Output:** “confident”  
>  **Explanation:**  
>  Words present in the sentence are “be”, “confident”, “and”, “be” and
> “yourself”.  
> Length of each of the words are 2, 9, 3, 2, and 8 respectively.  
> Therefore, the longest word is “confident”.
>
>  **Input:** S = “geeks for geeks”  
>  **Output:** “geeks”

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Searching-based Approach:** Refer to this article to solve this problem by
performing the following steps:

  

  

  * Iterate over the characters of the string.
  * Check if the current character encountered is a space or end of the string is reached.
  * If the current character is found to be so, update the maximum length of a word obtained.
  * Finally, print the longest word obtained using substr() method.

 _ **Time Complexity:** O(N)  
 **Auxiliary Space:** O(1)_

 **Approach usingsorted() method:** The idea is to split the string into
separate words and store in a list. Then, sort the list in the order of
increasing length using the sorted() method. Print the last string in the
sorted list.

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

 

# Function to print the longest

# word in given sentence

def largestWord(s):

 

 # Sort the words in increasing

 # order of their lengths

 s = sorted(s, key = len)

 

 # Print last word

 print(s[-1])

 

 

# Driver Code

if __name__ == "__main__":

 

 # Given string

 s = "be confident and be yourself"

 

 # Split the string into words

 l = list(s.split(" "))

 

 largestWord(l)  
  
---  
  
 __

 __

 **Output:**

    
    
    confident
    

_**Time Complexity:** O(N * logN)_  
 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

