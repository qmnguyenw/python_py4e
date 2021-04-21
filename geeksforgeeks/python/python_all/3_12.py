Python program to print words from a sentence with highest and lowest ASCII
value of characters



Given a string **S** of length **N** , representing a sentence, the task is to
print the words with the highest and lowest average of ASCII values of
characters.

 **Examples:**

>  **Input:** S = “every moment is fresh beginning”  
>  **Output:**  
>  Word with minimum average ASCII values is “beginning”.  
> Word with maximum average ASCII values is “every”.  
>  **Explanation:**  
>  The average of ASCII values of characters of the word “every” =
> ((101+118+101+114+121)/5 =111)  
> The average of ASCII values of characters of the word “moment” =: ((
> 109+111+109+101+110+116)/6 = 109.33333)  
> The average of ASCII values of characters of the word “is” = ((105+115)/2 =)  
> The average of ASCII values of characters of the word “fresh” =
> ((102+114+101+115+104)/5 = 110)  
> The average of ASCII values of characters of the word “beginning” =
> ((98+101+103+105+110+110+105+110+103)/9 =105).  
> Therefore, the word with minimum of average of ASCII values is “beginning”
> and maximum of average ASCII values is “every”.
>
>  **Input:** S = “sky is blue”  
>  **Output:**  
>  Word with minimum average ASCII values is “blue”.  
> Word with maximum average ASCII values is “sky”.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use the split() function. Follow the steps below
to solve the problem:

  

  

  * Split all the words of the string separated by spaces using the split() function. Store it in a **list**, say **lis[].**
  * Initialize four variables say **maxi, mini, maxId,** and **minId** , **** to store the maximum of average of ASCII values, the minimum average ASCII value, the index of the word with the maximum average ASCII value in the list lis, and the index of the word with the minimum average ASCII value in the list **lis[]** respectively.
  * Define a function, say **averageValue(),** to find the average ASCII value of a string.
  * Traverse the list **lis[]** and perform the following operations:
    * For every **i th **word in the list **lis[]** , **** and store it in a variable, say **curr.**
    * If **curr > maxi, **then update **maxi** as **maxi = curr** and assign **maxId = i.**
    * If **curr < mini,** then update **mini** as **mini = curr** and assign **minId = i.**
  * After completing the above steps, print the words **lis[minId]** and **lis[maxId]** with minimum and maximum average of ASCII value of its characters **.**

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of the above approach

 

# Function to find the average

# of ASCII value of a word

def averageValue(s):

 

 # Stores the sum of ASCII

 # value of all characters

 sumChar = 0

 

 # Traverse the string

 for i in range(len(s)):

 

 # Increment sumChar by ord(s[i])

 sumChar += ord(s[i])

 

 # Return the average

 return sumChar // len(s)

 

# Function to find words with maximum

# and minimum average of ascii values

def printMinMax(string):

 

 # Stores the words of the

 # string S seprated by spaces

 lis = list(string.split(" "))

 

 # Stores the index of word in

 # lis[] with maximum average

 maxId = 0

 

 # Stores the index of word in

 # lis[] with minimum average

 minId = 0

 

 # Stores the maximum average

 # of ASCII value of characters

 maxi = -1

 

 # Stores the minimum average

 # of ASCII value of characters

 mini = 1e9

 

 # Traverse the list lis

 for i in range(len(lis)):

 

 # Stores the average of

 # word at index i

 curr = averageValue(lis[i])

 

 # If curr is greater than maxi

 if(curr > maxi):

 

 # Update maxi and maxId

 maxi = curr

 maxId = i

 

 # If curr is lesser than mini

 if(curr < mini):

 

 # Update mini and minId

 mini = curr

 minId = i

 

 # Print string at minId in lis

 print("Minimum average ascii word = ", lis[minId])

 

 # Print string at maxId in lis

 print("Maximum average ascii word = ", lis[maxId])

 

 

# Driver Code

 

S = "every moment is fresh beginning"

printMinMax(S)  
  
---  
  
 __

 __

 **Output:**

    
    
    Minimum average ascii word =  beginning
    Maximum average ascii word =  every
    

_**Time Complexity:** O(N)_  
 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

