Python | Sort tuple based on occurrence of first element



Given a list of tuples, write a Python program to sort the list based on the
occurrence of first element of tuples.

 **Examples:**

    
    
    **Input :** [(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]
    **Output :** [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]
    
    **Input :** [('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]
    **Output :** [('a', 'arm', 'ant', 2), ('b', 'ball', 'b', 2)]
    

**Approach #1 :** using dict.fromkeys

The fromkeys() method returns a new dictionary with the given sequence of
elements as the keys of the dictionary. Now once we store the new dictionary
in ‘dct’ we can easily iterate over ‘dct’ elements and output the desired
elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Sort tuple based

# on occurrence of first element

def sortOnOccurence(lst):

 dct = {}

 for i, j in lst:

 dct.setdefault(i, []).append(j)

 return([(i, *dict.fromkeys(j), len(j))

 for i, j in dct.items()])

 

# Driver code

lst = [(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]

print(sortOnOccurence(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(1, 'Cara', 'Jake', 2), (2, 'Bob', 1)]
    

