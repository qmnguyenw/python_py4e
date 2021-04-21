Python | Count occurrences of an element in a list



Given a list in Python and a number x, count number of occurrences of x in the
given list.

Examples:

    
    
    Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
             x = 10
    Output : 3 
    10 appears three times in given list.
    
    Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
            x = 16
    Output : 0
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1 (Simple approach)**  
We keep a counter that keeps on increasing if the esquired element is found in
the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count the number of occurrences

def countX(lst, x):

 count = 0

 for ele in lst:

 if (ele == x):

 count = count + 1

 return count

 

# Driver Code

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

x = 8

print('{} has occurred {} times'.format(x, countX(lst, x)))  
  
---  
  
 __

 __

    
    
    Output:
    8 has occurred 5 times

 **Method 2 (Using count())**  
The idea is to use list method count() to count number of occurrences.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count the number of occurrences

def countX(lst, x):

 return lst.count(x)

 

# Driver Code

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

x = 8

print('{} has occurred {} times'.format(x, countX(lst, x)))  
  
---  
  
 __

 __

    
    
    Output:
    8 has occurred 5 times

 **Method 2 (Using Counter())**  
Counter method returns a dictionary with occurrences of all elements as a key-
value pair, where key is the element and value is the number of times that
element has occurred.

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

# declaring the list

l = [1, 1, 2, 2, 3, 3, 4, 4, 5,
5]

 

# driver program

x = 3

d = Counter(l)

print('{} has occurred {} times'.format(x, d[x]))  
  
---  
  
 __

 __

    
    
    Output:
    3 has occurred 2 times

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

