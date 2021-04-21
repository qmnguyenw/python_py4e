Python | Print all string combination from given numbers



Given an integer _N_ as input, the task is to print the all the string
combination from it in lexicographical order.

 **Examples:**

    
    
    **Input :**  191
    **Output :** aia sa
    **Explanation:** 
    The Possible String digit are 
    1, 9 and 1 --> aia
    19 and 1 --> sa
    
    **Input :** 1119
    **Output :** aaai aas aki kai ks
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Get the String and find all its combination list in the given order.
  * Find the list whose integers lies in the range of 0 to 25.
  * Convert the integers to the alphabets.
  * Sort it in lexicographical order.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print all string

# combination from given numbers

 

# Function to find the combination

def Number_to_String(String):

 

 # length of string 

 length = len(String)

 

 # temporary lists

 temp1 =[]

 temp2 =[]

 

 # alphabets Sequence

 alphabet ="abcdefghijklmnopqrstuvwxyz"

 

 # Power variable

 power = 2**(length-1)

 

 for i in range(0, power):

 

 # temporary String

 sub = ""

 Shift = i 

 x = 0

 sub += String[x]

 x += 1

 for j in range(length - 1):

 if Shift&1:

 sub+=" "

 Shift = Shift>>1

 sub += String[x]

 x += 1

 temp1.append(list(map(int, sub.split())))

 

 # Integer to String 

 for index in temp1: 

 substring =""

 for j in index:

 if j > 0 and j <= 26: 

 substring += alphabet[j-1]

 if len(substring) == len(index):

 temp2.append(substring)

 

 # lexicographical order sorting

 print(*sorted(temp2), sep =" ")

 

# Driver Code

Number_to_String("191")

Number_to_String("1991")

Number_to_String("1532")

Number_to_String("1191")  
  
---  
  
 __

 __

 **Output:**

    
    
    aia sa
    aiia sia
    aecb ocb
    aaia asa kia
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

