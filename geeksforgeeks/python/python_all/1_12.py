Generate all possible permutations of words in a Sentence



Given a string **S** , the task is to print permutations of all words in a
sentence.

 **Examples:**

>  **Input:** S = “sky is blue”  
>  **Output:**  
>  sky is blue  
> sky blue is  
> is sky blue  
> is blue sky  
> blue sky is  
> blue is sky
>
>  **Input:** S =” Do what you love”  
>  **Output:**  
>  Do what you love  
> Do what love you  
> Do you what love  
> Do you love what  
> Do love what you  
> Do love you what  
> what Do you love  
> what Do love you  
> what you Do love  
> what you love Do  
> what love Do you  
> what love you Do  
> you Do what love  
> you Do love what  
> you what Do love  
> you what love Do  
> you love Do what  
> you love what Do  
> love Do what you  
> love Do you what  
> love what Do you  
> love what you Do  
> love you Do what  
> love you what Do

 **Approach:** The given problem can be solved using recursion. Follow the
steps below to solve the problem:

  

  

  1. Traverse the sentence and split the words present in the sentence by spaces using **split()** and store them in a list.
  2. Permute the list using built-in python functions **itertools.permutations()**.
  3. Traverse the permutations and convert each permutation to a **list.**
  4. Print these lists.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of

# the above approach

 

from itertools import permutations

 

 

# Function to generate permutations

# of all words in a sentence

def calculatePermutations(sentence):

 

 # Stores all words in the sentence

 lis = list(sentence.split())

 

 # Stores all possible permuations

 # of words in this list

 permute = permutations(lis)

 

 # Iterate over all permutations

 for i in permute:

 

 # Convert the current

 # permutation into a list

 permutelist = list(i)

 

 # Print the words in the

 # list separated by spaces

 for j in permutelist:

 print(j, end = " ")

 

 # Print a new line

 print()

 

 

# Driver Code

if __name__ == '__main__':

 

 sentence = "sky is blue"

 calculatePermutations(sentence)  
  
---  
  
 __

 __

 **Output:**

    
    
    sky is blue 
    sky blue is 
    is sky blue 
    is blue sky 
    blue sky is 
    blue is sky
    

_**Time Complexity:** O(N!), where N denotes the number of words in a
sentence._  
 _ **Auxiliary Space:** O(N!)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

