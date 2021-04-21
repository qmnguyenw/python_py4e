Python program to count Even and Odd numbers in a Dictionary



Given a python dictionary, the task si to count even and odd numbers present
in the dictionary.

 **Examples:**

>  **Input** : {‘a’: 1, ‘b’: 2, ‘c’: 3, ‘d’: 4, ‘e’ : 5}  
>  **Output** : Even = 2, odd = 3
>
>  **Input** : {‘x’: 4, ‘y’:9, ‘z’:16}  
>  **Output** : Even = 2, odd = 1

 **Approach using** **values()** **Function:** Traverse the dictionary and
extract its elements using values() function and for each extracted value,
check if it is even or odd. Finally, print the respective counts.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to count even and

# odd numbers present in a dictionary

 

# Function to count even and odd

# numbers present in a dictionary

def countEvenOdd(dict):

 

 # Stores count of even

 # and odd elements

 even = 0

 odd = 0

 

 # Traverse the dictionary

 for i in dict.values():

 

 if i % 2 == 0:

 even = even + 1

 else:

 odd = odd + 1

 

 print("Even Count: ", even)

 print("Odd Count: ", odd)

 

# Driver Code

 

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
'e': 5}

countEvenOdd(dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Even Count:  2
    Odd Count:  3
    

_**Time Complexity:** O(N)_  
 _ **Auxiliary Space:** O(1)_

 **Alternate Approach:** Iterate over each item in the dictionary, and for
each element, check if it is even or odd. Finally, print the respective
counts.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to count even

# and odd elements in a dictionary

 

# Function to count even and

# odd elements in a dictionary

def countEvenOdd(dict):

 even = 0

 odd = 0

 

 # Iterate over the dictionary

 for i in dict:

 

 # If current element is even

 if dict[i] % 2 == 0:

 

 # Increase count of even

 even = even + 1

 

 # Otherwise

 else:

 

 # Increase count of odd

 odd = odd + 1

 

 print("Even count: ", even)

 print("Odd count: ", odd)

 

# Driver Code

 

# Given Dictionary

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
'e': 5}

 

countEvenOdd(dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Even count:  2
    Odd count:  3
    

_**Time Complexity:** O(N)_  
 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

