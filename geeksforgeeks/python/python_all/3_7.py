Python Program to print all distinct uncommon digits present in two given
numbers



Given two positive integers **A** and **B** , the task is to print the
distinct digits in descending order, which are not common in the two numbers.

 **Examples:**

>  **Input:** A = 378212, B = 78124590  
>  **Output:** 9 5 4 3 0  
>  **Explanation:** All distinct digits present in the two numbers are {0, 1,
> 2, 3, 4, 5, 6, 7, 8, 9}. The digits {1, 2, 6, 7} are common in both numbers.
>
>  **Input:** A = 100, B = 273  
>  **Output:** 7 3 2 1 0  
>  **Explanation:** All distinct digits present in the two numbers are {0, 1,
> 2, 3, 7}. The digits {0, 1, 2, 3, 7} are common in both numbers.

 **Approach:** The problem can be solved using sets, and lists in python.
Follow the steps below to solve the problem:

  

  

  * Convert both integers into strings.
  * Now, store the equivalent integer values of the characters of the strings **A** and **B** in the lists **lis1** and **lis2** , using map() function.
  * Convert both the lists **lis1** and **lis2** to set **lis1** and **lis2** using the set() method.
  * Now, find the uncommon digits of both sets **lis1** and **lis2** using the function symmetric_difference() and store it in a set, say **lis**.
  * After completing the above steps, convert the set **lis** into list **lis** using list() method.
  * Finally, Sort the list in descending order and print the list **lis** as the answer.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation

# of the above approach

 

# Function to print uncommon digits

# of two numbers in descending order

def disticntUncommonDigits(A, B):

 

 # Stores digits of A as string

 A = str(A)

 

 # Stores digits of B as string

 B = str(B)

 

 # Stores the characters

 # of A in a integer list

 lis1 = list(map(int, A))

 

 # Stores the characters

 # of B in a integer list

 lis2 = list(map(int, B))

 

 # Converts lis1 to set

 lis1 = set(lis1)

 

 # Converts lis2 to set

 lis2 = set(lis2)

 

 # Stores the uncommon digits present

 # in the sets lis1 and lis2

 lis = lis1.symmetric_difference(lis2)

 

 # Converts lis to list

 lis = list(lis)

 

 # Sort the list in descending order

 lis.sort(reverse = True)

 

 # Print the list lis

 for i in lis:

 print(i, end =" ")

 

# Driver Code

 

 

# Input

A = 378212

B = 78124590

 

disticntUncommonDigits(A, B)  
  
---  
  
 __

 __

 **Output:**

    
    
    9 5 4 3 0
    

_**Time Complexity:** O(log10(A) + log10(B))  
 **Auxiliary Space:** O(log10(A) + log10(B))_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

