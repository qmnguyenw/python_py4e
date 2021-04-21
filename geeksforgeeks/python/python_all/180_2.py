Python program to find the most occurring character and its count



Given a string, write a python program to find the most occurrence character
and its number of occurrences.

Examples:

    
    
    Input : hello
    Output : ('l', 2)
    
    Input : geeksforgeeks
    Output : ('e', 4)
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We can solve this problem quickly in python using Counter() method. Simple
Approach is to  
1) Create a dictionary using Counter method having strings as keys and their
frequencies as values.  
2) Find the maximum occurrence of a character i.e. value and get the index of
it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the most occurring

# character and its count

from collections import Counter

 

def find_most_occ_char(input):

 

 # now create dictionary using counter method

 # which will have strings as key and their 

 # frequencies as value

 wc = Counter(input)

 

 # Finding maximum occurrence of a character 

 # and get the index of it.

 s = max(wc.values())

 i = wc.values().index(s)

 

 print wc.items()[i]

 

# Driver program

if __name__ == "__main__":

 input = 'geeksforgeeks'

 find_most_occ_char(input)  
  
---  
  
 __

 __

Output:

    
    
    ('e', 4)
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

