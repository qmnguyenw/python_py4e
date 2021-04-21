Python program to count number of vowels using sets in given string



Given a string, count the number of vowels present in given string using Sets.

 **Prerequisite:**Sets in Python

Examples:

    
    
    Input : GeeksforGeeks
    Output : No. of vowels : 5
    
    Input : Hello World
    Output : No. of vowels :  3
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
1\. Create a set of vowels using set() and initialize a count variable to 0.  
2\. Traverse through the alphabets in the string and check if the letter in
the string is present in set vowel.  
3\. If it is present, the vowel count is incremented.

Below is the implementation of above approach:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to count vowel in

# a string using set

 

# Function to count vowel

def vowel_count(str):

 

 # Initializing count variable to 0

 count = 0

 

 # Creating a set of vowels

 vowel = set("aeiouAEIOU")

 

 # Loop to traverse the alphabet

 # in the given string

 for alphabet in str:

 

 # If alphabet is present

 # in set vowel

 if alphabet in vowel:

 count = count + 1

 

 print("No. of vowels :", count)

 

# Driver code 

str = "GeeksforGeeks"

 

# Function Call

vowel_count(str)  
  
---  
  
 __

 __

Output:

    
    
    No. of vowels : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

