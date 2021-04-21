Count the number of unique characters in a string in Python



Given a string **S** consisting of lowercase English alphabets, the task is to
find the number of unique characters present in the string.

 **Examples:**

>  **Input:** S = “geeksforgeeks”  
>  **Output:** 7  
>  **Explanation:** The given string “geeksforgeeks” contains 6 unique
> characters {‘g’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’}.
>
>  **Input:** S = “madam”  
>  **Output:** 3

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea to solve the given problem is to initialize a Set() in
python to store all distinct characters of the given string and then, print
the size of the set as the required answer.

  

  

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for the above approach

# Function to count the number of distinct

# characters present in the string str

def countDis(str):

 # Stores all distinct characters

 s = set(str)

 # Return the size of the set

 return len(s)

# Driver Code

if __name__ == "__main__":

 # Given string S

 S = "geeksforgeeks"

 print(countDis(S))  
  
---  
  
 __

 __

 **Output:**

    
    
    7

_**Time Complexity:** O(N)_  
 _ **Auxiliary Space:** O(1)_

#### Method 2: Using **Counter**function:

Count the frequencies of all elements using Counter function and number of
keys of this frequency dictionary gives the result.

Below is the implementation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for the above approach

from collections import Counter

# Function to count the number of distinct

# characters present in the string str

def countDis(str):

 # Stores all frquencies

 freq = Counter(str)

 # Return the size of the freq dictionary

 return len(freq)

# Driver Code

if __name__ == "__main__":

 # Given string S

 S = "geeksforgeeks"

 print(countDis(S))

 

# This code is contributed by vikkycirus  
  
---  
  
 __

 __

 **Output:**

    
    
    7

 **Time Complexity:** O(N)

 **Auxiliary Space:** O(N)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

