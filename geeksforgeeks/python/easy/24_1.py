Python – Find all duplicate characters in string



Given a string, find all the duplicate characters which are similar to each
others.

Let’s look at the example.  
Examples:

    
    
    Input : hello
    Output : l
    
    Input : geeksforgeeeks
    Output : e g k s
    

We have discussed a solution in below post.  
Print all the duplicates in the input string

We can solve this problem quickly using python Counter() method. Approach is
very simple.

1) First create a dictionary using Counter method having strings as keys and
their frequencies as values.  
2) Declare a temp variable.  
3) Print all the indexes from the keys which have value greater than 1.  

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

def find_dup_char(input):

 

 # now create dictionary using counter method

 # which will have strings as key and their 

 # frequencies as value

 WC = Counter(input)

 j = -1

 

 

 # Finding no. of occurrence of a character

 # and get the index of it.

 for i in WC.values():

 j = j + 1

 if( i > 1 ):

 print WC.keys()[j],

 

# Driver program

if __name__ == "__main__":

 input = 'geeksforgeeks'

 find_dup_char(input)  
  
---  
  
 __

 __

Output:

    
    
    e g k s
    

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

